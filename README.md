# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-12 12:21:03`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$31.84 USD** | **$6.71 USD** | **$38.56 USD** | 🔴 **-3.61%** ($-1.44) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $356.63 | $6.71 | 📈 +3.27% | 6d 18h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market is currently experiencing significant downward pressure with major indices and stocks trading below their SMA20 trend lines, heavily impacted by negative macro sentiment and leadership shocks in the technology sector (such as Nvidia's Jensen Huang resigning). Almost all major equities and crypto assets show bearish trends. Only AAPL remains in a confirmed uptrend (above SMA20) with positive relative performance and solid holding gains (+3.27%). Most other assets are facing strong corrective moves with extremely oversold short-term conditions, but lack reversal confirmation triggers (positive 1-hour changes and RSI >= 32)."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is currently the only asset meeting our uptrend requirements (above SMA20). It is showing stable performance with a +3.27% profit. Sticking to the equity holding patience rule, we continue to hold this position while letting winners run towards our profit target.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding our single winning equity position in AAPL in line with equity patience guidelines. All other monitored assets are currently in a bearish trend below their SMA20 lines or lacking proper reversal triggers. We maintain our cash buffer of $31.84 and wait for clear trend recoveries and positive 1-hour momentum before entering new pullback setups. Target profit for AAPL is set around +4% to +5%, with stop-loss protection ready."
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
