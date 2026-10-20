# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-20 20:00:50`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.92 USD** | **$39.04 USD** | 🔴 **-2.39%** ($-0.96) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $339.50 | $9.97 | 📉 -0.33% | 7h 59m |
| `ETH-USD` | 0.004058 | $2452.17 | $2452.76 | $9.95 | 📈 +0.02% | 6h 9m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The traditional stock market is currently closed, with major assets like AAPL, QQQ, NVDA, and SPY showing frozen prices. AAPL remains secure in an uptrend above its SMA20. In the 24/7 crypto markets, ETH-USD is holding steady near our entry price with an elevated 1-hour RSI approaching overbought territory (70.7), though its trend is currently classified as bearish below the SMA20. MSFT is the only equity asset showing an active bullish trend above its SMA20, but the market is closed. We maintain strict risk management and patience with existing holdings."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): AAPL is an equity holding in a confirmed uptrend (above SMA20) and market hours are closed. Following the rule of equity holding patience, we give the stock time to play out.
- **[HOLD] ETH-USD** (Confidence: 90%): ETH-USD is holding near our entry price with a strong 24-hour gain (+1.99%). We are waiting for the take-profit target of +3.0% to +5.0% or an RSI(1h) > 72 before exiting.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Monitor ETH-USD closely for profit-taking if RSI(1h) exceeds 72 or if gains reach the +3.0% to +5.0% target window. Maintain AAPL as it is a patient equity holding positioned above its SMA20 uptrend. Keep cash reserves above $4.00 USD and do not open any new crypto positions due to anti-correlation constraints."
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
