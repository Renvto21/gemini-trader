# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-21 05:30:43`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.92 USD** | **$39.04 USD** | 🔴 **-2.39%** ($-0.96) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $339.50 | $9.97 | 📉 -0.33% | 17h 29m |
| `ETH-USD` | 0.004058 | $2452.17 | $2452.43 | $9.95 | 📈 +0.01% | 15h 39m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market condition remains cautious, with major US equities and crypto assets showing mixed performance and many trading below their SMA20 trend lines. Specifically, AAPL is currently closed and maintains a bullish stance above SMA20 with low volatility, while ETH-USD is flat to slightly negative on the 1-hour timeframe (change_1h_pct: -0.05) and trading below the SMA20 trend line. Given the strict trend filter and reversal confirmation rules, we maintain our current positions while monitoring for take-profit or stop-loss triggers."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 80%): AAPL is in an uptrend (above SMA20) and market status is closed. Adhering to equity holding patience to let the position play out.
- **[HOLD] ETH-USD** (Confidence: 80%): ETH-USD is currently flat on the 1-hour change (-0.05%) and does not trigger stop-loss or take-profit targets yet. Holding position per asymmetric risk rules.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Hold AAPL in line with equity holding patience guidelines. Monitor ETH-USD for a profit target between +3% and +5% or stop-loss execution near -1.8%. No new crypto purchases will be made as ETH-USD is already held, respecting the single crypto holding constraint and trend filters."
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
