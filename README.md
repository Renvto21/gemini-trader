# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-10 01:50:45`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.14 USD** | **$20.76 USD** | **$38.89 USD** | 🔴 **-2.76%** ($-1.11) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $350.69 | $6.60 | 📈 +1.55% | 4d 8h |
| `MSFT` | 0.013089 | $534.82 | $545.18 | $7.14 | 📈 +1.94% | 3d 12h |
| `GLD` | 0.018501 | $378.35 | $379.53 | $7.02 | 📈 +0.31% | 14h 19m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The traditional stock market (AAPL, MSFT, GLD, QQQ, SPY, NVDA) is currently closed (CERRADO). Key equity positions in AAPL and MSFT remain solid and profitable in confirmed uptrends above their SMA20. GLD is slightly positive. Cryptocurrencies (BTC-USD, ETH-USD, SOL-USD) are open (24/7) but are currently sitting in bearish trends below their SMA20. Following strict rules, falling knives in crypto are avoided, and closed equity markets prevent any transactions today."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): Asset is in a confirmed uptrend above SMA20 and market is closed. Adhering to equity holding patience rule.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain current equity holdings in AAPL, MSFT, and GLD as they remain in solid uptrends above their SMA20. Continue to monitor stop-loss levels strictly at -2.0% and prepare to take profits once positions reach +3.0% to +5.0%. Keep crypto sidelined until a confirmed daily trend reversal occurs above the SMA20."
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
