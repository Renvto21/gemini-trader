# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-21 09:40:44`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.98 USD** | **$39.11 USD** | 🔴 **-2.24%** ($-0.89) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $339.50 | $9.97 | 📉 -0.33% | 21h 39m |
| `ETH-USD` | 0.004058 | $2452.17 | $2467.85 | $10.01 | 📈 +0.64% | 19h 49m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The traditional stock market is currently closed with prices frozen, limiting our actions on equities like AAPL. Our AAPL position is holding steady near its entry point with minor fluctuation (-0.33%), complying with equity holding patience. ETH-USD is showing mild positive performance (+0.64%) but is currently classified in a downtrend (below SMA20). BTC-USD is currently the only major crypto asset in a confirmed uptrend (above SMA20) with positive momentum, but we already hold ETH-USD and are constrained by the single crypto exposure rule. Therefore, maintaining our current holdings is the optimal strategy."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): Adhering to equity holding patience rules. AAPL is showing minor drawdown (-0.33%) but has been open for less than 24 hours, so it should be given time to play out.
- **[HOLD] ETH-USD** (Confidence: 100%): ETH-USD is currently showing a small profit (+0.64%). Holding until the take-profit target of +3.0% to +5.0% is reached or stop-loss is triggered.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing AAPL and ETH-USD positions. Wait for ETH-USD to reach our take-profit target of +3.0% to +5.0% or hit the stop-loss limit at -2.0%. Hold AAPL patiently according to equity holding rules. Do not open new crypto positions due to the anti-correlation single crypto constraint."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **82** | 🎯 **43.9%** (36W / 31L / 15BE) | 🔴 **$-0.79 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-20 13:51` | 🟢 BUY | `ETH-USD` | $9.95 | $2452.17 | ETH-USD muestra un excelente impulso de corto plazo con change_1h_pct positivo (+0.55%) y ... |
| `2026-10-20 13:51` | 🔴 SELL (-0.05$) | `GLD` | $9.95 | $377.90 | GLD se encuentra estancado con un rendimiento ligeramente negativo (-0.47%) y un rsi_1h de... |
| `2026-10-20 12:01` | 🟢 BUY | `GLD` | $10.00 | $379.70 | GLD presenta un RSI de 1 hora en 31.4, acercándose a la zona ideal de sobreventa para acti... |
| `2026-10-20 12:01` | 🟢 BUY | `AAPL` | $10.00 | $340.64 | AAPL se encuentra en tendencia alcista diaria con un RSI de 1 hora en 33.1 (cercano a sobr... |
| `2026-10-20 11:10` | 🔴 SELL (+0.12$) | `BTC-USD` | $8.69 | $82949.93 | BTC-USD muestra un RSI de 1 hora en 72.2 (sobrecompra) y un rendimiento positivo de +1.45%... |

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
