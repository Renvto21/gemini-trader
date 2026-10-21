# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-21 11:01:39`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$29.20 USD** | **$10.02 USD** | **$39.21 USD** | 🔴 **-1.97%** ($-0.79) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $341.20 | $10.02 | 📈 +0.16% | 23h 0m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market shows a mix of conditions. Equities are currently open and showing moderate activity, while major cryptocurrencies like BTC-USD remain in an uptrend above the SMA20. However, current 1-hour change percentages for potential crypto targets like BTC-USD are negative or flat (change_1h_pct is -0.09%), failing to meet our strict reversal confirmation trigger of a positive 1-hour candle. For our existing equity position in AAPL, it has been held for roughly 23 hours in an uptrend and remains slightly positive (+0.16%), adhering to our equity holding patience rule since it has not hit stop-loss or profit targets."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in a confirmed uptrend above the SMA20 and is currently showing a slight positive return (+0.16%). Following equity holding patience rules, we maintain the position as it has not met stop-loss or take-profit criteria.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "AAPL will continue to be held patiently in accordance with equity holding rules. For crypto, BTC-USD is above SMA20 but lacks a confirmed green 1-hour candle (change_1h_pct is -0.09% with an RSI_1h of 69.8); we will wait for a proper pullback with a confirmed green candle before executing any crypto buy. Maintain cash reserves above $4.00 USD and strictly follow stop-loss and profit-target rules."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **83** | 🎯 **44.6%** (37W / 31L / 15BE) | 🔴 **$-0.67 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-21 10:10` | 🔴 SELL (+0.12$) | `ETH-USD` | $10.07 | $2481.87 | ETH-USD rsi_1h has surpassed 72 (currently 73.7) with a positive return of +1.21%, satisfy... |
| `2026-10-20 13:51` | 🟢 BUY | `ETH-USD` | $9.95 | $2452.17 | ETH-USD muestra un excelente impulso de corto plazo con change_1h_pct positivo (+0.55%) y ... |
| `2026-10-20 13:51` | 🔴 SELL (-0.05$) | `GLD` | $9.95 | $377.90 | GLD se encuentra estancado con un rendimiento ligeramente negativo (-0.47%) y un rsi_1h de... |
| `2026-10-20 12:01` | 🟢 BUY | `GLD` | $10.00 | $379.70 | GLD presenta un RSI de 1 hora en 31.4, acercándose a la zona ideal de sobreventa para acti... |
| `2026-10-20 12:01` | 🟢 BUY | `AAPL` | $10.00 | $340.64 | AAPL se encuentra en tendencia alcista diaria con un RSI de 1 hora en 33.1 (cercano a sobr... |

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
