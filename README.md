# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-10 15:00:58`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.01 USD** | **$13.49 USD** | **$38.50 USD** | 🔴 **-3.74%** ($-1.50) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $347.58 | $6.54 | 📈 +0.65% | 4d 21h |
| `MSFT` | 0.013089 | $534.82 | $531.04 | $6.95 | 📉 -0.71% | 4d 1h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market is experiencing a corrective phase with most major indices and stocks trading below their SMA20, reflecting ongoing macro concerns and hot inflation data. Notable tech stocks like NVDA and broad crypto assets are in severe downtrends. However, AAPL and MSFT remain resilient, maintaining their positions above their SMA20 trends. We maintain strict patience with our equity positions as per the equity holding patience rule, avoiding panic selling on minor fluctuations."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 80%): AAPL remains in a confirmed uptrend above its SMA20 with a positive PnL (+0.65%). Adhering to equity holding patience rules, we allow the position time to run.
- **[HOLD] MSFT** (Confidence: 75%): MSFT is still above its SMA20 trend line. Although experiencing a slight pullback, it has not breached our strict -1.8% to -2.0% stop-loss circuit breaker. We maintain the position.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain current holdings in AAPL and MSFT as they remain in a confirmed uptrend above the SMA20. Monitor MSFT closely since its current PnL is near -0.71%; prepare to cut losses if it approaches the strict -1.8% to -2.0% stop-loss threshold. Do not enter any new crypto or equity positions until clear reversal confirmations (1-hour candle turns green with RSI >= 32) emerge within confirmed uptrends."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **90** | 🎯 **42.2%** (38W / 37L / 15BE) | 🔴 **$-1.35 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-10 11:31` | 🔴 SELL (-0.12$) | `GLD` | $6.87 | $371.60 | GLD has fallen below its SMA20 trend line and its current PnL is approaching the strict st... |
| `2026-11-09 11:30` | 🟢 BUY | `GLD` | $7.00 | $378.35 | GLD is in a confirmed uptrend above its SMA20, market status is open, 1-hour momentum is s... |
| `2026-11-06 13:10` | 🟢 BUY | `MSFT` | $7.00 | $534.82 | MSFT is in a confirmed uptrend above its SMA20, market status is open, 1-hour RSI has reco... |
| `2026-11-05 17:40` | 🟢 BUY | `AAPL` | $6.50 | $345.35 | AAPL is in a confirmed uptrend above its SMA20, market status is open, and 1-hour momentum... |
| `2026-11-05 11:20` | 🔴 SELL (-0.15$) | `ETH-USD` | $6.85 | $2374.60 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -2.10% hit safety limit (-2.0%). Liquidated by code... |

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
