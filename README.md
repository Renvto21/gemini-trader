# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-20 19:00:57`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.92 USD** | **$39.05 USD** | 🔴 **-2.38%** ($-0.95) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $339.50 | $9.97 | 📉 -0.33% | 6h 59m |
| `ETH-USD` | 0.004058 | $2452.17 | $2454.17 | $9.96 | 📈 +0.08% | 5h 9m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The traditional equity markets are currently closed, rendering most stock assets inactive. Active liquidity is focused on the 24/7 crypto markets, where ETH-USD and BTC-USD show solid 24-hour performance but are consolidating slightly in the current 1-hour interval. AAPL remains stable as an equity holding above its SMA20 trend line, while ETH-USD is held under our single crypto constraint, awaiting either a take-profit target between +3.0% and +5.0% or an RSI(1h) exceeding 72. No new positions are opened due to strict anti-correlation constraints and market status filters."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 80%): AAPL is an equity holding moving slower than crypto, showing stability. Following the equity holding patience rule, we give the stock time to play out without rotating or selling prematurely.
- **[HOLD] ETH-USD** (Confidence: 85%): ETH-USD is currently profitable and progressing toward our asymmetric take-profit target of +3.0% to +5.0%. Holding under the single crypto constraint and maintaining strict stop-loss protection.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing positions in AAPL and ETH-USD. AAPL is an equity holding showing stability above SMA20; maintain patience and let the trade play out according to equity holding rules. ETH-USD is currently held under the single crypto position constraint; monitor for a take-profit target between +3.0% and +5.0% or an RSI(1h) exceeding 72, while strictly enforcing the stop-loss limit between -1.8% and -2.0%. Do not open new positions until the next market session opens or clear pullback setups appear."
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
