# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-06 12:20:42`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.14 USD** | **$6.44 USD** | **$38.58 USD** | 🔴 **-3.55%** ($-1.42) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $342.27 | $6.44 | 📉 -0.89% | 18h 39m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market is showing signs of stabilization following recent volatility, with several indices attempting a rebound. However, strict quantitative trend filters reveal that most assets remain in a downtrend (below their SMA20). Notably, MSFT is currently the only asset trading above its SMA20 in an uptrend, but it fails the reversal confirmation trigger due to a negative 1-hour change (-0.54%) and an RSI of 26.6. Our current holding, AAPL, has slipped below its SMA20 and is experiencing a minor pullback (-0.89% PnL), but adhering to the Equity Holding Patience rule, we maintain the position as it has not hit the hard stop-loss circuit breaker (-1.8% to -2.0%)."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is experiencing a minor pullback (-0.89%) but remains well above the strict -1.8% to -2.0% stop-loss threshold. Per the Equity Holding Patience rule, stocks should not be rotated prematurely based solely on short-term flatness or minor dips.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL position while closely monitoring the stop-loss circuit breaker (-1.8% to -2.0%). MSFT remains the sole asset in a confirmed uptrend (above SMA20), but will wait for a positive 1-hour momentum change and RSI >= 32 before considering any entry. No new crypto positions will be opened given the current lack of confirmed uptrends in digital assets."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **89** | 🎯 **42.7%** (38W / 36L / 15BE) | 🔴 **$-1.23 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-05 17:40` | 🟢 BUY | `AAPL` | $6.50 | $345.35 | AAPL is in a confirmed uptrend above its SMA20, market status is open, and 1-hour momentum... |
| `2026-11-05 11:20` | 🔴 SELL (-0.15$) | `ETH-USD` | $6.85 | $2374.60 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -2.10% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-05 01:41` | 🟢 BUY | `ETH-USD` | $7.00 | $2425.59 | ETH-USD is in a confirmed uptrend above its SMA20, market status is open 24/7, 1-hour RSI ... |
| `2026-11-04 22:00` | 🔴 SELL (-0.31$) | `MSFT` | $6.69 | $520.99 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -4.44% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-04 11:30` | 🟢 BUY | `MSFT` | $7.00 | $545.20 | MSFT is currently the only asset trading above its SMA20 in a confirmed uptrend with stron... |

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
