import os
from datetime import datetime
from typing import Dict, Any, List, Optional

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
README_FILE = os.path.join(BASE_DIR, "README.md")

def get_chile_now():
    try:
        from zoneinfo import ZoneInfo
        return datetime.now(ZoneInfo("America/Santiago"))
    except Exception:
        from datetime import timezone, timedelta
        return datetime.now(timezone(timedelta(hours=-3)))

def update_readme_dashboard(
    summary: Dict[str, Any],
    decision_summary: str,
    actions: List[Any],
    history: List[Dict[str, Any]],
    memory_notes: str = "",
    stats: Optional[Dict[str, Any]] = None,
    lang: str = "en"
):
    pnl = summary.get('total_pnl_usd', 0.0)
    pnl_pct = summary.get('total_pnl_pct', 0.0)
    pnl_icon = "🟢" if pnl >= 0 else "🔴"
    
    now_str = get_chile_now().strftime("%Y-%m-%d %H:%M:%S")
    is_en = (lang.lower() == "en")
    
    positions = summary.get("positions", [])
    if positions:
        pos_rows = []
        for p in positions:
            p_pnl = p.get('pnl_pct', 0.0)
            p_icon = "📈" if p_pnl >= 0 else "📉"
            holding = p.get('holding_time', 'Recent' if is_en else 'Reciente')
            pos_rows.append(
                f"| `{p['ticker']}` | {p['shares']:.6f} | ${p['avg_price']:.2f} | ${p['current_price']:.2f} | ${p['current_value']:.2f} | {p_icon} {p_pnl:+.2f}% | {holding} |"
            )
        pos_table = "\n".join(pos_rows)
    else:
        empty_msg = "*(No open positions - 100% in cash)*" if is_en else "*(Ninguna posición abierta - 100% en efectivo)*"
        pos_table = f"| {empty_msg} | - | - | - | - | - | - |"

    # Acciones decididas en este ciclo
    action_texts = []
    for a in actions:
        ticker = getattr(a, 'ticker', None) or (a.get('ticker') if isinstance(a, dict) else '')
        act = getattr(a, 'action', None) or (a.get('action') if isinstance(a, dict) else '')
        conf = getattr(a, 'confidence', 0.0) or (a.get('confidence', 0.0) if isinstance(a, dict) else 0.0)
        reason = getattr(a, 'reasoning', '') or (a.get('reasoning', '') if isinstance(a, dict) else '')
        label_conf = "Confidence" if is_en else "Confianza"
        action_texts.append(f"- **[{act}] {ticker}** ({label_conf}: {conf*100:.0f}%): {reason}")
    
    no_actions_msg = "- *No changes this cycle (HOLD)*" if is_en else "- *Sin cambios en este ciclo (HOLD)*"
    actions_formatted = "\n".join(action_texts) if action_texts else no_actions_msg

    # Sección de bitácora / memoria para próximos ciclos
    memory_section = ""
    if memory_notes:
        mem_title = "### 📝 Operational Memory & Journal (Next Cycles)" if is_en else "### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)"
        memory_section = f"""---

{mem_title}

> \"{memory_notes}\"
"""

    # Sección de estadísticas quant
    stats_section = ""
    if stats:
        best = stats.get("best_trade")
        worst = stats.get("worst_trade")
        prep = "on" if is_en else "en"
        best_str = f"+${best['pnl_usd']:.2f} ({best['pnl_pct']:+.1f}%) {prep} {best['ticker']}" if best else "-"
        worst_str = f"${worst['pnl_usd']:.2f} ({worst['pnl_pct']:+.1f}%) {prep} {worst['ticker']}" if worst else "-"
        realized_icon = "🟢" if stats['realized_pnl_usd'] >= 0 else "🔴"
        
        if is_en:
            stats_section = f"""---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **{stats['total_closed_trades']}** | 🎯 **{stats['win_rate_pct']:.1f}%** ({stats['wins']}W / {stats['losses']}L / {stats['breakevens']}BE) | {realized_icon} **${stats['realized_pnl_usd']:+.2f} USD** | 🏆 `{best_str}` | 🛡️ `{worst_str}` |
"""
        else:
            stats_section = f"""---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **{stats['total_closed_trades']}** | 🎯 **{stats['win_rate_pct']:.1f}%** ({stats['wins']}W / {stats['losses']}L / {stats['breakevens']}BE) | {realized_icon} **${stats['realized_pnl_usd']:+.2f} USD** | 🏆 `{best_str}` | 🛡️ `{worst_str}` |
"""

    # Historial de últimos 5 movimientos
    recent_history = list(reversed(history))[:5]
    if recent_history:
        hist_rows = []
        for h in recent_history:
            t = h.get("timestamp", "")[:16].replace("T", " ")
            act = h.get("action", "")
            if act == "BUY":
                badge = "🟢 BUY"
            elif act == "SELL":
                pnl_u = h.get("pnl_usd")
                badge = f"🔴 SELL ({pnl_u:+.2f}$)" if pnl_u is not None else "🔴 SELL"
            elif act == "DEPOSIT":
                badge = "💵 DEPOSIT"
            else:
                badge = f"ℹ️ {act}"
            hist_rows.append(
                f"| `{t}` | {badge} | `{h.get('ticker')}` | ${h.get('amount_usd', 0):.2f} | ${h.get('price', 0):.2f} | {h.get('reason', '')[:90]}... |"
            )
        hist_table = "\n".join(hist_rows)
    else:
        empty_hist = "*(No movements recorded yet)*" if is_en else "*(Sin movimientos aún)*"
        hist_table = f"| {empty_hist} | - | - | - | - | - |"

    if is_en:
        readme_content = f"""# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `{now_str}`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **${summary['initial_capital']:.2f} USD** | **${summary['cash']:.2f} USD** | **${summary['positions_value']:.2f} USD** | **${summary['total_equity']:.2f} USD** | {pnl_icon} **{pnl_pct:+.2f}%** (${pnl:+.2f}) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
{pos_table}

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> \"{decision_summary}\"

**Cycle Actions:**
{actions_formatted}

{memory_section}{stats_section}---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
{hist_table}

---

<details>
<summary>⚙️ View technical configuration and local commands</summary>

### Available commands
* **Check current status:** `python main.py --status --lang en`
* **Run 1 test cycle:** `python main.py --run-once --lang en`
* **Run continuous loop:** `python main.py --loop --interval 300 --lang en`

### System modules
* `main.py`: Main orchestrator and risk filter guards.
* `dashboard.py`: Dynamic README dashboard generator (EN/ES).
* `agent.py`: Gemini Flash decision engine and quantitative prompt.
* `portfolio.py`: Portfolio ledger, PnL calculations, and Circuit Breakers.
* `market_data.py`: Real-time market data, SMA20, and 1H/daily RSI via yfinance.
* `portfolio.json`: Portfolio database and operational journal.
</details>
"""
    else:
        readme_content = f"""# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `{now_str}`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **${summary['initial_capital']:.2f} USD** | **${summary['cash']:.2f} USD** | **${summary['positions_value']:.2f} USD** | **${summary['total_equity']:.2f} USD** | {pnl_icon} **{pnl_pct:+.2f}%** (${pnl:+.2f}) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
{pos_table}

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> \"{decision_summary}\"

**Operaciones del ciclo:**
{actions_formatted}

{memory_section}{stats_section}---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
{hist_table}

---

<details>
<summary>⚙️ Ver configuración técnica y comandos locales</summary>

### Comandos disponibles
* **Ver estado actual:** `python main.py --status`
* **Ejecutar 1 ciclo de prueba:** `python main.py --run-once`
* **Ejecutar en bucle local:** `python main.py --loop --interval 300`

### Módulos del sistema
* `main.py`: Orquestador principal del bot y guardas de riesgo.
* `dashboard.py`: Generador del panel dinámico en README (EN/ES).
* `agent.py`: Conexión con Gemini Flash y reglas cuantitativas.
* `portfolio.py`: Registro de operaciones, cálculo de saldo y Circuit Breakers.
* `market_data.py`: Descarga y cálculo técnico con yfinance (SMA20, RSI 1H/Diario).
* `portfolio.json`: Base de datos de posiciones y bitácora.
</details>
"""

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(readme_content)

def trim_trading_log(file_path: str = None, max_lines: int = 150):
    if file_path is None:
        file_path = os.path.join(BASE_DIR, "trading.log")
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
            if len(lines) > max_lines:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.writelines(lines[-max_lines:])
        except Exception:
            pass
