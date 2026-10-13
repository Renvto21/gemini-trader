import os
import sys

# Asegurar codificación UTF-8 en consola de Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

import time
import argparse
from datetime import datetime
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

from portfolio import PortfolioManager
from market_data import get_market_snapshot, DEFAULT_WATCHLIST
from agent import TradingAgent
from dashboard import update_readme_dashboard, trim_trading_log

def log_message(msg: str):
    print(msg, flush=True)
    with open("trading.log", "a", encoding="utf-8") as f:
        f.write(msg + "\n")

def display_portfolio(summary: dict):
    lines = [
        "\n" + "=" * 55,
        " 📊 ESTADO ACTUAL DEL PORTAFOLIO",
        "=" * 55,
        f" Capital Inicial:      ${summary['initial_capital']:.2f} USD",
        f" Efectivo Disponible:  ${summary['cash']:.2f} USD",
        f" Valor en Activos:     ${summary['positions_value']:.2f} USD",
        f" Balance Total:        ${summary['total_equity']:.2f} USD"
    ]
    
    pnl = summary['total_pnl_usd']
    pnl_pct = summary['total_pnl_pct']
    icon = "🟢" if pnl >= 0 else "🔴"
    lines.append(f" Ganancia/Pérdida:     {icon} ${pnl:+.2f} USD ({pnl_pct:+.2f}%)")

    positions = summary.get("positions", [])
    if positions:
        lines.append("\n 💼 Posiciones Abiertas:")
        for p in positions:
            pnl_pos = p['pnl_usd']
            p_icon = "📈" if pnl_pos >= 0 else "📉"
            hold_info = f" [Tiempo: {p['holding_time']}]" if 'holding_time' in p else ""
            lines.append(f"   • {p['ticker']}: {p['shares']} u. | Compra: ${p['avg_price']} | Actual: ${p['current_price']} | Total: ${p['current_value']} {p_icon} ({p['pnl_pct']:+.2f}%){hold_info}")
    else:
        lines.append("\n 💼 Posiciones Abiertas: (Ninguna, 100% en efectivo)")
    lines.append("=" * 55 + "\n")

    log_message("\n".join(lines))

def run_trading_cycle(agent: TradingAgent, portfolio: PortfolioManager):
    log_message(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 🔍 Iniciando ciclo de análisis...")

    # 1. Obtener datos del mercado (con velas diarias e intradiarias de 1h)
    tickers_to_check = list(set(DEFAULT_WATCHLIST + list(portfolio.positions.keys())))
    log_message(f"📡 Descargando cotizaciones e indicadores intradiarios para {len(tickers_to_check)} activos...")
    snapshot = get_market_snapshot(tickers_to_check)

    if not snapshot:
        log_message("❌ Error al obtener datos de mercado. Reintentando en el próximo ciclo.")
        return

    current_prices = {t: data["current_price"] for t, data in snapshot.items()}

    # 2. Circuit Breaker automático por código (Hard Stop-Loss a -3.0% y Take-Profit a +4.0%)
    cb_triggered = portfolio.check_and_execute_circuit_breakers(
        current_prices,
        stop_loss_pct=-3.0,
        take_profit_pct=4.0
    )
    if cb_triggered:
        log_message("\n🚨 CIRCUIT BREAKER AUTOMÁTICO ACTIVADO:")
        for cb in cb_triggered:
            log_message(f"   • {cb['reason']}")

    # 3. Resumen actual del portafolio con precios reales
    summary = portfolio.get_summary(current_prices)
    display_portfolio(summary)

    # 4. Consultar al agente Gemini con memoria y bitácora operativa
    memory_context = {
        "previous_notes": portfolio.get_memory(),
        "recent_trades": portfolio.get_recent_history(3),
        "circuit_breakers": cb_triggered
    }
    log_message("🤖 Consultando a Gemini para análisis y toma de decisiones...")
    decision = agent.evaluate_market_and_decide(summary, snapshot, memory_context=memory_context)

    log_message("\n🧠 ANÁLISIS DE MERCADO DE GEMINI:")
    log_message(f"\"{decision.market_analysis}\"\n")

    if decision.memory_notes:
        log_message("📝 BITÁCORA / NOTAS PARA PRÓXIMOS CICLOS:")
        log_message(f"\"{decision.memory_notes}\"\n")
        portfolio.update_memory(decision.memory_notes)

    # 5. Procesar y ejecutar decisiones de Gemini
    log_message("⚡ ACCIONES DECIDIDAS:")
    for action in decision.actions:
        ticker = action.ticker
        act = action.action
        reason = action.reasoning
        confidence = action.confidence

        log_message(f"  • Acción: [{act}] {ticker} (Confianza: {confidence*100:.0f}%)")
        log_message(f"    Razón: {reason}")

        # Validar si el mercado está abierto
        market_info = snapshot.get(ticker, {})
        status = market_info.get("market_status", "")

        if act == "BUY":
            if "CERRADO" in status:
                log_message(f"    ⚠️ Mercado cerrado para {ticker} ({status}). Orden cancelada para proteger liquidez.")
                continue

            price = current_prices.get(ticker)
            if not price:
                log_message(f"    ⚠️ No hay precio disponible para {ticker}.")
                continue
            
            amount_to_spend = min(action.amount_usd, portfolio.cash)
            if amount_to_spend >= 1.0:
                success = portfolio.execute_buy(ticker, amount_to_spend, price, reason)
                if success:
                    log_message(f"    ✅ Compra ejecutada: ${amount_to_spend:.2f} en {ticker} a ${price:.2f}")
            else:
                log_message(f"    ⚠️ Saldo insuficiente o monto demasiado pequeño (${amount_to_spend:.2f}). No se ejecutó compra.")

        elif act == "SELL":
            if "CERRADO" in status:
                log_message(f"    ⚠️ Mercado cerrado para {ticker} ({status}). No se puede vender en este momento.")
                continue

            price = current_prices.get(ticker)
            if not price or ticker not in portfolio.positions:
                log_message(f"    ⚠️ No posees {ticker} para vender.")
                continue
            
            shares = action.shares if action.shares > 0 else portfolio.positions[ticker]["shares"]
            success = portfolio.execute_sell(ticker, shares, price, reason)
            if success:
                log_message(f"    ✅ Venta ejecutada: {shares} de {ticker} a ${price:.2f}")

        elif act == "HOLD":
            log_message(f"    ⏸️ Manteniendo posición actual sin cambios.")

    # Guardar y mostrar resumen actualizado
    updated_summary = portfolio.get_summary(current_prices)
    stats = portfolio.get_performance_stats()
    
    # Actualizar panel visual en README.md y recortar log antiguo
    update_readme_dashboard(
        summary=updated_summary,
        decision_summary=decision.market_analysis,
        actions=decision.actions,
        history=portfolio.data.get("history", []),
        memory_notes=portfolio.get_memory(),
        stats=stats
    )
    trim_trading_log(max_lines=150)

    log_message("\n🏁 Fin del ciclo.")
    log_message(f"Balance final del ciclo: ${updated_summary['total_equity']:.2f} USD (Cash: ${updated_summary['cash']:.2f} USD)")

def main():
    parser = argparse.ArgumentParser(description="Gemini Autonomous Trading Bot")
    parser.add_argument("--status", action="store_true", help="Muestra el estado del portafolio y sale")
    parser.add_argument("--run-once", action="store_true", help="Ejecuta un ciclo de trading y sale")
    parser.add_argument("--loop", action="store_true", help="Ejecuta el bot en bucle continuo")
    parser.add_argument("--interval", type=int, default=600, help="Intervalo en segundos para el bucle (default: 600 = 10 mins)")
    args = parser.parse_args()

    portfolio = PortfolioManager()

    if args.status:
        # Precios aproximados o directos
        snapshot = get_market_snapshot(list(portfolio.positions.keys()) or ["SPY"])
        prices = {k: v["current_price"] for k, v in snapshot.items()}
        summary = portfolio.get_summary(prices)
        display_portfolio(summary)
        stats = portfolio.get_performance_stats()
        update_readme_dashboard(
            summary=summary,
            decision_summary="Consulta manual del estado del portafolio.",
            actions=[],
            history=portfolio.data.get("history", []),
            memory_notes=portfolio.get_memory(),
            stats=stats
        )
        return

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key == "tu_api_key_aqui":
        print("\n" + "!" * 60)
        print("⚠️  ATENCIÓN: Falta configurar tu GEMINI_API_KEY")
        print("1. Abre o crea el archivo .env en esta carpeta:")
        print("   GEMINI_API_KEY=tu_clave_de_google_ai_studio")
        print("2. Puedes obtenerla gratis en: https://aistudio.google.com/app/apikey")
        print("!" * 60 + "\n")
        sys.exit(1)

    agent = TradingAgent(api_key=api_key)

    if args.loop:
        print(f"🚀 Bot iniciado en modo bucle. Intervalo: {args.interval} segundos ({args.interval/60:.0f} mins).")
        print("Presiona Ctrl+C para detenerlo en cualquier momento.\n")
        try:
            while True:
                run_trading_cycle(agent, portfolio)
                print(f"\n⏳ Esperando {args.interval} segundos para el siguiente ciclo...")
                time.sleep(args.interval)
        except KeyboardInterrupt:
            print("\n👋 Bot detenido por el usuario.")
    else:
        # Por defecto corre una vez
        run_trading_cycle(agent, portfolio)

if __name__ == "__main__":
    main()
