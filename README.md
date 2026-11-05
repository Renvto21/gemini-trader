# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-05 06:10:47`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$31.78 USD** | **$6.96 USD** | **$38.74 USD** | 🔴 **-3.14%** ($-1.26) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.002886 | $2425.59 | $2411.75 | $6.96 | 📉 -0.57% | 4h 29m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Traditional equity and commodity markets are currently closed (CERRADO), leaving active trading opportunities restricted to 24/7 crypto assets. Within crypto, BTC-USD and ETH-USD maintain confirmed uptrends above their SMA20. ETH-USD is currently held in the portfolio, down slightly by 0.57%, but remains structurally sound above its moving average with a healthy 1-hour RSI. The 1-hour candle change for ETH-USD is currently slightly negative (-0.26%), meaning the reversal confirmation trigger is not yet met for adding more capital. Therefore, patience is required."

**Cycle Actions:**
- **[HOLD] ETH-USD** (Confidence: 85%): ETH-USD remains in a valid uptrend above the SMA20 and is experiencing a minor consolidation. The position is small and well within risk limits, so we maintain the holding and wait for a clear green 1-hour candle confirmation to add or let it run toward target.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding existing ETH-USD position. Monitor ETH-USD for a positive 1-hour candle change (> 0.0) combined with an RSI >= 32 before considering any add-on buys. Respect the stop-loss level at -1.8% to -2.0% and take-profit targets between +3.0% and +5.0%. Keep cash reserve secure."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **88** | 🎯 **43.2%** (38W / 35L / 15BE) | 🔴 **$-1.08 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-05 01:41` | 🟢 BUY | `ETH-USD` | $7.00 | $2425.59 | ETH-USD is in a confirmed uptrend above its SMA20, market status is open 24/7, 1-hour RSI ... |
| `2026-11-04 22:00` | 🔴 SELL (-0.31$) | `MSFT` | $6.69 | $520.99 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -4.44% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-04 11:30` | 🟢 BUY | `MSFT` | $7.00 | $545.20 | MSFT is currently the only asset trading above its SMA20 in a confirmed uptrend with stron... |
| `2026-11-02 11:40` | 🔴 SELL (-0.13$) | `AAPL` | $6.87 | $340.69 | AAPL has slipped further into a bearish trend below its SMA20 with a 1-hour RSI of 24.8 an... |
| `2026-10-28 13:21` | 🔴 SELL (-0.02$) | `MSFT` | $6.48 | $528.16 | MSFT has shifted to a bearish trend below its SMA20 and current performance is near our st... |

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
