# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-12 11:41:04`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$31.84 USD** | **$6.72 USD** | **$38.56 USD** | 🔴 **-3.59%** ($-1.44) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $357.10 | $6.72 | 📈 +3.40% | 6d 18h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market is experiencing generalized downward pressure with major indices and equities trading below their SMA20 trends, compounded by significant macro volatility such as the leadership transition news at Nvidia. AAPL remains a distinct outlier, holding a strong bullish trend above its SMA20, currently showing solid gains with a high 1H RSI of 96.5. Other assets are either in strong downtrends or fail to meet our strict reversal and trend criteria."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is in a confirmed uptrend above the SMA20 with a current profit of +3.4%. Following equity holding patience and asymmetric reward principles, we hold the position to capture full upside while monitoring the extreme 1H RSI for profit-taking windows.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding our single winning position in AAPL in adherence with equity holding patience rules. AAPL's profit is currently +3.4% with an overbought 1H RSI of 96.5; we will monitor closely to lock in profits if momentum stalls or take-profit targets between +3.0% and +5.0% are fully realized. No new buys are executed as all other market assets remain below the SMA20 trend filter or fail to confirm safe pullback criteria."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **91** | 🎯 **41.8%** (38W / 38L / 15BE) | 🔴 **$-1.52 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-11 12:20` | 🔴 SELL (-0.17$) | `MSFT` | $6.83 | $521.92 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -2.41% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-10 11:31` | 🔴 SELL (-0.12$) | `GLD` | $6.87 | $371.60 | GLD has fallen below its SMA20 trend line and its current PnL is approaching the strict st... |
| `2026-11-09 11:30` | 🟢 BUY | `GLD` | $7.00 | $378.35 | GLD is in a confirmed uptrend above its SMA20, market status is open, 1-hour momentum is s... |
| `2026-11-06 13:10` | 🟢 BUY | `MSFT` | $7.00 | $534.82 | MSFT is in a confirmed uptrend above its SMA20, market status is open, 1-hour RSI has reco... |
| `2026-11-05 17:40` | 🟢 BUY | `AAPL` | $6.50 | $345.35 | AAPL is in a confirmed uptrend above its SMA20, market status is open, and 1-hour momentum... |

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
