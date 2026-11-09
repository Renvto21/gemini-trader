# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-09 19:40:43`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.14 USD** | **$20.76 USD** | **$38.89 USD** | 🔴 **-2.76%** ($-1.11) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $350.69 | $6.60 | 📈 +1.55% | 4d 1h |
| `MSFT` | 0.013089 | $534.82 | $545.18 | $7.14 | 📈 +1.94% | 3d 6h |
| `GLD` | 0.018501 | $378.35 | $379.53 | $7.02 | 📈 +0.31% | 8h 9m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The current equity markets (AAPL, MSFT, GLD, SPY, QQQ) are closed with frozen prices. Our active positions in AAPL (+1.55%), MSFT (+1.94%), and GLD (+0.31%) continue to hold steady above their respective SMA20 lines in healthy uptrends, requiring patience. Meanwhile, crypto markets remain open (BTC-USD, SOL-USD, ETH-USD) but are currently in a confirmed bear trend (below SMA20), violating our strict trend-following filter. Therefore, no trades should be executed during this cycle, maintaining our current allocation and cash reserves."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): Asset is in a confirmed uptrend above SMA20 with positive PnL (+1.55%). Market is closed. Maintaining position per equity holding patience rule.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL, MSFT, and GLD patiently as they remain in solid uptrends above the SMA20 while equity markets are closed. Will monitor for profit-taking targets between +3.0% and +5.0% or circuit breaker stop-loss levels at -2.0% once Wall Street reopens. Avoid all crypto assets as they remain trapped in downtrends below the SMA20."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **89** | 🎯 **42.7%** (38W / 36L / 15BE) | 🔴 **$-1.23 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-09 11:30` | 🟢 BUY | `GLD` | $7.00 | $378.35 | GLD is in a confirmed uptrend above its SMA20, market status is open, 1-hour momentum is s... |
| `2026-11-06 13:10` | 🟢 BUY | `MSFT` | $7.00 | $534.82 | MSFT is in a confirmed uptrend above its SMA20, market status is open, 1-hour RSI has reco... |
| `2026-11-05 17:40` | 🟢 BUY | `AAPL` | $6.50 | $345.35 | AAPL is in a confirmed uptrend above its SMA20, market status is open, and 1-hour momentum... |
| `2026-11-05 11:20` | 🔴 SELL (-0.15$) | `ETH-USD` | $6.85 | $2374.60 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -2.10% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-05 01:41` | 🟢 BUY | `ETH-USD` | $7.00 | $2425.59 | ETH-USD is in a confirmed uptrend above its SMA20, market status is open 24/7, 1-hour RSI ... |

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
