# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-21 09:10:41`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.97 USD** | **$39.10 USD** | 🔴 **-2.25%** ($-0.90) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $339.50 | $9.97 | 📉 -0.33% | 21h 9m |
| `ETH-USD` | 0.004058 | $2452.17 | $2466.29 | $10.01 | 📈 +0.58% | 19h 19m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Wall Street equities and ETFs (AAPL, MSFT, SPY, QQQ, NVDA, GLD) are currently closed, with market status showing CERRADO. Therefore, active trading must focus on open crypto assets (24/7). ETH-USD is currently showing a minor positive profit (+0.58%), but its trend is listed as BAJISTA (below SMA20) although its 1h RSI is strong at 59.6. AAPL is holding steady in equity with a small -0.33% loss, which must be maintained in accordance with patience rules. BTC-USD is currently in an uptrend (ALCISTA, above SMA20) with positive momentum, but we already hold ETH-USD and anti-correlation constraints limit us to ONE crypto position at a time. No take-profit or stop-loss triggers have been hit yet, so holding current positions is the most disciplined approach."

**Cycle Actions:**
- **[HOLD] ETH-USD** (Confidence: 80%): ETH-USD is currently showing positive performance (+0.58%) but has not yet reached our take-profit threshold (+3.0% to +5.0%) or stop-loss level. Holding in accordance with asymmetric risk/reward rules.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing AAPL equity position following equity holding patience rules. Monitor ETH-USD position closely: hold until take-profit target reaches +3.0% to +5.0% or stop-loss triggers at -2.0%. Keep cash reserves intact and wait for high-quality uptrend pullbacks on crypto or market-open equities when conditions align."
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
