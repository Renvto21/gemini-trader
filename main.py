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

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "trading.log")

def log_message(msg: str):
    print(msg, flush=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(msg + "\n")

def display_portfolio(summary: dict, lang: str = "en"):
    is_en = (lang.lower() == "en")
    header_title = " 📊 CURRENT PORTFOLIO STATUS" if is_en else " 📊 ESTADO ACTUAL DEL PORTAFOLIO"
    lbl_init = " Initial Capital:     " if is_en else " Capital Inicial:      "
    lbl_cash = " Available Cash:      " if is_en else " Efectivo Disponible:  "
    lbl_assets = " Assets Value:        " if is_en else " Valor en Activos:     "
    lbl_total = " Total Balance:       " if is_en else " Balance Total:        "
    lbl_pnl = " Net PnL:             " if is_en else " Ganancia/Pérdida:     "
    
    lines = [
        "\n" + "=" * 55,
        header_title,
        "=" * 55,
        f"{lbl_init}${summary['initial_capital']:.2f} USD",
        f"{lbl_cash}${summary['cash']:.2f} USD",
        f"{lbl_assets}${summary['positions_value']:.2f} USD",
        f"{lbl_total}${summary['total_equity']:.2f} USD"
    ]
    
    pnl = summary['total_pnl_usd']
    pnl_pct = summary['total_pnl_pct']
    icon = "🟢" if pnl >= 0 else "🔴"
    lines.append(f"{lbl_pnl}{icon} ${pnl:+.2f} USD ({pnl_pct:+.2f}%)")

    positions = summary.get("positions", [])
    if positions:
        pos_title = "\n 💼 Open Positions:" if is_en else "\n 💼 Posiciones Abiertas:"
        lines.append(pos_title)
        for p in positions:
            pnl_pos = p['pnl_usd']
            p_icon = "📈" if pnl_pos >= 0 else "📉"
            lbl_time = "Time" if is_en else "Tiempo"
            hold_info = f" [{lbl_time}: {p['holding_time']}]" if 'holding_time' in p else ""
            lines.append(f"   • {p['ticker']}: {p['shares']} u. | Buy: ${p['avg_price']} | Now: ${p['current_price']} | Total: ${p['current_value']} {p_icon} ({p['pnl_pct']:+.2f}%){hold_info}")
    else:
        empty_title = "\n 💼 Open Positions: (None, 100% in cash)" if is_en else "\n 💼 Posiciones Abiertas: (Ninguna, 100% en efectivo)"
        lines.append(empty_title)
    lines.append("=" * 55 + "\n")

    log_message("\n".join(lines))

def run_trading_cycle(agent: TradingAgent, portfolio: PortfolioManager, lang: str = "en"):
    is_en = (lang.lower() == "en")
    log_message(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 🔍 Starting analysis cycle..." if is_en else f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 🔍 Iniciando ciclo de análisis...")

    # 1. Obtener datos del mercado (con velas diarias e intradiarias de 1h)
    tickers_to_check = list(set(DEFAULT_WATCHLIST + list(portfolio.positions.keys())))
    log_message(f"📡 Downloading quotes & 1H intraday indicators for {len(tickers_to_check)} assets..." if is_en else f"📡 Descargando cotizaciones e indicadores intradiarios para {len(tickers_to_check)} activos...")
    snapshot = get_market_snapshot(tickers_to_check)

    if not snapshot:
        log_message("❌ Error downloading market data. Will retry next cycle.")
        return

    current_prices = {t: data["current_price"] for t, data in snapshot.items()}

    # 2. Circuit Breaker automático por código (Hard Stop-Loss a -2.0% y Take-Profit a +4.5%)
    cb_triggered = portfolio.check_and_execute_circuit_breakers(
        current_prices,
        stop_loss_pct=-2.0,
        take_profit_pct=4.5
    )
    if cb_triggered:
        log_message("\n🚨 AUTOMATIC CIRCUIT BREAKER TRIGGERED:" if is_en else "\n🚨 CIRCUIT BREAKER AUTOMÁTICO ACTIVADO:")
        for cb in cb_triggered:
            log_message(f"   • {cb['reason']}")

    # 3. Resumen actual del portafolio con precios reales
    summary = portfolio.get_summary(current_prices)
    display_portfolio(summary, lang=lang)

    # 4. Consultar al agente Gemini con memoria y bitácora operativa
    memory_context = {
        "previous_notes": portfolio.get_memory(),
        "recent_trades": portfolio.get_recent_history(3),
        "circuit_breakers": cb_triggered
    }
    log_message("🤖 Consulting Gemini for market analysis and trading decisions..." if is_en else "🤖 Consultando a Gemini para análisis y toma de decisiones...")
    decision = agent.evaluate_market_and_decide(summary, snapshot, memory_context=memory_context, lang=lang)

    log_message("\n🧠 GEMINI MARKET ANALYSIS:" if is_en else "\n🧠 ANÁLISIS DE MERCADO DE GEMINI:")
    log_message(f"\"{decision.market_analysis}\"\n")

    if decision.memory_notes:
        log_message("📝 OPERATIONAL JOURNAL / NOTES FOR NEXT CYCLES:" if is_en else "📝 BITÁCORA / NOTAS PARA PRÓXIMOS CICLOS:")
        log_message(f"\"{decision.memory_notes}\"\n")
        portfolio.update_memory(decision.memory_notes)

    # 5. Procesar y ejecutar decisiones de Gemini con guardas institucionales
    log_message("⚡ DECIDED ACTIONS:" if is_en else "⚡ ACCIONES DECIDIDAS:")
    for action in decision.actions:
        ticker = action.ticker
        act = action.action
        reason = action.reasoning
        confidence = action.confidence

        log_message(f"  • Action: [{act}] {ticker} (Confidence: {confidence*100:.0f}%)" if is_en else f"  • Acción: [{act}] {ticker} (Confianza: {confidence*100:.0f}%)")
        log_message(f"    Reason: {reason}" if is_en else f"    Razón: {reason}")

        market_info = snapshot.get(ticker, {})
        status = market_info.get("market_status", "")

        if act == "BUY":
            # Guarda 1: Horario de mercado
            if "CERRADO" in status:
                log_message(f"    ⚠️ Market closed for {ticker} ({status}). Order cancelled to preserve liquidity.")
                continue

            # Guarda 2: Filtro de Tendencia (Prohibido comprar cuchillos cayendo bajo SMA20)
            is_above_sma = market_info.get("is_above_sma20", True)
            if not is_above_sma:
                log_message(f"    🚫 Trend Filter Guard: {ticker} is below 20-day SMA (downtrend). Purchase blocked to avoid falling knives.")
                continue

            # Guarda 3: Regla Anti-Correlación (Máximo 1 posición cripto simultánea)
            if "-USD" in ticker:
                existing_crypto = [t for t in portfolio.positions.keys() if "-USD" in t and t != ticker]
                if existing_crypto:
                    log_message(f"    🚫 Anti-Correlation Guard: Already holding crypto ({', '.join(existing_crypto)}). Purchase blocked to prevent duplicate risk.")
                    continue

            price = current_prices.get(ticker)
            if not price:
                log_message(f"    ⚠️ No price available for {ticker}.")
                continue
            
            amount_to_spend = min(action.amount_usd, portfolio.cash)
            if amount_to_spend >= 1.0:
                success = portfolio.execute_buy(ticker, amount_to_spend, price, reason)
                if success:
                    log_message(f"    ✅ Buy executed: ${amount_to_spend:.2f} in {ticker} @ ${price:.2f}")
            else:
                log_message(f"    ⚠️ Insufficient cash or amount too small (${amount_to_spend:.2f}). Order not executed.")

        elif act == "SELL":
            if "CERRADO" in status:
                log_message(f"    ⚠️ Market closed for {ticker} ({status}). Cannot sell at this time.")
                continue

            price = current_prices.get(ticker)
            if not price or ticker not in portfolio.positions:
                log_message(f"    ⚠️ Do not hold {ticker} to sell.")
                continue
            
            shares = action.shares if action.shares > 0 else portfolio.positions[ticker]["shares"]
            success = portfolio.execute_sell(ticker, shares, price, reason)
            if success:
                log_message(f"    ✅ Sell executed: {shares} of {ticker} @ ${price:.2f}")

        elif act == "HOLD":
            log_message("    ⏸️ Holding current position without changes." if is_en else "    ⏸️ Manteniendo posición actual sin cambios.")

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
        stats=stats,
        lang=lang
    )
    trim_trading_log(max_lines=150)

    log_message("\n🏁 Cycle completed." if is_en else "\n🏁 Fin del ciclo.")
    log_message(f"Final Cycle Balance: ${updated_summary['total_equity']:.2f} USD (Cash: ${updated_summary['cash']:.2f} USD)" if is_en else f"Balance final del ciclo: ${updated_summary['total_equity']:.2f} USD (Cash: ${updated_summary['cash']:.2f} USD)")

def main():
    default_lang = os.getenv("TRADING_LANG", os.getenv("DASHBOARD_LANG", "en"))
    parser = argparse.ArgumentParser(description="Gemini Autonomous Trading Bot")
    parser.add_argument("--status", action="store_true", help="Display portfolio status and exit")
    parser.add_argument("--run-once", action="store_true", help="Execute 1 trading cycle and exit")
    parser.add_argument("--loop", action="store_true", help="Run bot in continuous loop")
    parser.add_argument("--interval", type=int, default=600, help="Loop interval in seconds (default: 600 = 10 mins)")
    parser.add_argument("--lang", type=str, default=default_lang, choices=["en", "es"], help="Dashboard and agent language (en or es)")
    args = parser.parse_args()

    portfolio = PortfolioManager()

    if args.status:
        snapshot = get_market_snapshot(list(portfolio.positions.keys()) or ["SPY"])
        prices = {k: v["current_price"] for k, v in snapshot.items()}
        summary = portfolio.get_summary(prices)
        display_portfolio(summary, lang=args.lang)
        stats = portfolio.get_performance_stats()
        update_readme_dashboard(
            summary=summary,
            decision_summary="Manual query of portfolio status." if args.lang == "en" else "Consulta manual del estado del portafolio.",
            actions=[],
            history=portfolio.data.get("history", []),
            memory_notes=portfolio.get_memory(),
            stats=stats,
            lang=args.lang
        )
        return

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key == "tu_api_key_aqui":
        print("\n" + "!" * 60)
        print("⚠️  ATTENTION: GEMINI_API_KEY is missing")
        print("1. Set GEMINI_API_KEY in your .env file or environment variables")
        print("2. You can get one for free at: https://aistudio.google.com/app/apikey")
        print("!" * 60 + "\n")
        sys.exit(1)

    agent = TradingAgent(api_key=api_key)

    if args.loop:
        print(f"🚀 Bot started in loop mode. Interval: {args.interval}s ({args.interval/60:.0f} mins). Lang: {args.lang}")
        print("Press Ctrl+C to stop at any time.\n")
        try:
            while True:
                run_trading_cycle(agent, portfolio, lang=args.lang)
                print(f"\n⏳ Waiting {args.interval} seconds for next cycle...")
                time.sleep(args.interval)
        except KeyboardInterrupt:
            print("\n👋 Bot stopped by user.")
    else:
        # Default: run once
        run_trading_cycle(agent, portfolio, lang=args.lang)

if __name__ == "__main__":
    main()
