import os
from datetime import datetime
from typing import Dict, Any, List

def get_chile_now():
    try:
        from zoneinfo import ZoneInfo
        return datetime.now(ZoneInfo("America/Santiago"))
    except Exception:
        from datetime import timezone, timedelta
        return datetime.now(timezone(timedelta(hours=-3)))

def update_readme_dashboard(summary: Dict[str, Any], decision_summary: str, actions: List[Any], history: List[Dict[str, Any]]):
    pnl = summary.get('total_pnl_usd', 0.0)
    pnl_pct = summary.get('total_pnl_pct', 0.0)
    pnl_icon = "🟢" if pnl >= 0 else "🔴"
    
    now_str = get_chile_now().strftime("%Y-%m-%d %H:%M:%S")
    
    positions = summary.get("positions", [])
    if positions:
        pos_rows = []
        for p in positions:
            p_pnl = p.get('pnl_pct', 0.0)
            p_icon = "📈" if p_pnl >= 0 else "📉"
            pos_rows.append(
                f"| `{p['ticker']}` | {p['shares']:.6f} | ${p['avg_price']:.2f} | ${p['current_price']:.2f} | ${p['current_value']:.2f} | {p_icon} {p_pnl:+.2f}% |"
            )
        pos_table = "\n".join(pos_rows)
    else:
        pos_table = "| *(Ninguna posición abierta - 100% en efectivo)* | - | - | - | - | - |"

    # Acciones decididas en este ciclo
    action_texts = []
    for a in actions:
        ticker = getattr(a, 'ticker', None) or (a.get('ticker') if isinstance(a, dict) else '')
        act = getattr(a, 'action', None) or (a.get('action') if isinstance(a, dict) else '')
        conf = getattr(a, 'confidence', 0.0) or (a.get('confidence', 0.0) if isinstance(a, dict) else 0.0)
        reason = getattr(a, 'reasoning', '') or (a.get('reasoning', '') if isinstance(a, dict) else '')
        action_texts.append(f"- **[{act}] {ticker}** (Confianza: {conf*100:.0f}%): {reason}")
    actions_formatted = "\n".join(action_texts) if action_texts else "- *Sin cambios en este ciclo (HOLD)*"

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
                badge = "🔴 SELL"
            elif act == "DEPOSIT":
                badge = "💵 DEPOSIT"
            else:
                badge = f"ℹ️ {act}"
            hist_rows.append(
                f"| `{t}` | {badge} | `{h.get('ticker')}` | ${h.get('amount_usd', 0):.2f} | ${h.get('price', 0):.2f} | {h.get('reason', '')[:90]}... |"
            )
        hist_table = "\n".join(hist_rows)
    else:
        hist_table = "| *(Sin movimientos aún)* | - | - | - | - | - |"

    readme_content = f"""# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `{now_str}`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **${summary['initial_capital']:.2f} USD** | **${summary['cash']:.2f} USD** | **${summary['positions_value']:.2f} USD** | **${summary['total_equity']:.2f} USD** | {pnl_icon} **{pnl_pct:+.2f}%** (${pnl:+.2f}) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
{pos_table}

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"{decision_summary}"*

**Operaciones del ciclo:**
{actions_formatted}

---

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
* `main.py`: Orquestador principal del bot.
* `dashboard.py`: Generador del panel dinámico en README.
* `agent.py`: Conexión con Gemini Flash y reglas de riesgo.
* `portfolio.py`: Registro de operaciones, cálculo de saldo y PnL.
* `market_data.py`: Descarga y cálculo técnico con yfinance.
* `portfolio.json`: Base de datos de posiciones.
</details>
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

def trim_trading_log(file_path: str = "trading.log", max_lines: int = 150):
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
            if len(lines) > max_lines:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.writelines(lines[-max_lines:])
        except Exception:
            pass
