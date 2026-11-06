# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-06 16:40:34`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.14 USD** | **$13.46 USD** | **$38.59 USD** | 🔴 **-3.52%** ($-1.41) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $344.27 | $6.48 | 📉 -0.31% | 22h 59m |
| `MSFT` | 0.013089 | $534.82 | $533.03 | $6.98 | 📉 -0.33% | 3h 29m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market continues to exhibit mixed conditions with major indices like SPY and QQQ remaining in a bearish trend below their SMA20 lines. However, individual holdings AAPL and MSFT remain in confirmed uptrends above their SMA20 lines and are currently being held patiently. Crypto assets (BTC-USD, ETH-USD, SOL-USD) are largely in bearish trends below the SMA20, prompting strict adherence to the anti-correlation and trend rules. No new signals meet the strict reversal criteria for buying, and existing equity positions are being maintained according to the patience rule."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in a confirmed uptrend above its SMA20 and is being held patiently following equity rules. Current minor drawdown (-0.31%) is well within normal parameters, and we are waiting for profit targets (+3.0% to +5.0%).
- **[HOLD] MSFT** (Confidence: 85%): MSFT remains above its SMA20 in a confirmed uptrend. Position is being maintained patiently with an eye on the stop-loss and take-profit targets.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL and MSFT positions. Both are maintaining structural stability above their SMA20 lines despite minor intraday fluctuations. Awaiting +3.0% to +5.0% profit targets while strictly monitoring the -1.8% to -2.0% stop-loss limits. No new crypto or equity entries are warranted at this stage as reversal confirmation triggers are not fully met across alternate assets."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **89** | 🎯 **42.7%** (38W / 36L / 15BE) | 🔴 **$-1.23 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-06 13:10` | 🟢 BUY | `MSFT` | $7.00 | $534.82 | MSFT is in a confirmed uptrend above its SMA20, market status is open, 1-hour RSI has reco... |
| `2026-11-05 17:40` | 🟢 BUY | `AAPL` | $6.50 | $345.35 | AAPL is in a confirmed uptrend above its SMA20, market status is open, and 1-hour momentum... |
| `2026-11-05 11:20` | 🔴 SELL (-0.15$) | `ETH-USD` | $6.85 | $2374.60 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -2.10% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-05 01:41` | 🟢 BUY | `ETH-USD` | $7.00 | $2425.59 | ETH-USD is in a confirmed uptrend above its SMA20, market status is open 24/7, 1-hour RSI ... |
| `2026-11-04 22:00` | 🔴 SELL (-0.31$) | `MSFT` | $6.69 | $520.99 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -4.44% hit safety limit (-2.0%). Liquidated by code... |

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
