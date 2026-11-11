# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-11 17:00:52`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$31.84 USD** | **$6.67 USD** | **$38.52 USD** | 🔴 **-3.71%** ($-1.48) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $354.55 | $6.67 | 📈 +2.66% | 5d 23h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market continues to show a mixed trend environment. While major equity benchmarks like SPY are in a confirmed uptrend above the SMA20, other indices such as QQQ and key large-cap tech assets remain below their SMA20 trend line. AAPL remains our sole open position, maintaining a profitable status (+2.66%) in an established uptrend above the SMA20, adhering to our equity holding patience rules. Crypto assets such as BTC-USD, ETH-USD, and SOL-USD continue to trade below their SMA20 lines, violating strict trend filter rules for new long entries despite positive 24-hour bounces. We maintain strict risk management and capital preservation."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in a confirmed uptrend above its SMA20 and is currently profitable (+2.66%). Following the equity holding patience rule, we will maintain the position rather than rotating prematurely, waiting for the target range of +3.0% to +5.0% or an RSI 1h > 72 before taking profits.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Continue holding AAPL per equity holding patience rules. Monitor AAPL closely for take-profit opportunities if it reaches +3.0% to +5.0% gains or if RSI 1h exceeds 72. Maintain strict discipline on trend-following filters: do not open new long positions on any asset trading below its SMA20. For future equity deployment, look for confirmed uptrends like SPY or AAPL experiencing a healthy pullback where RSI 1h >= 32 and change_1h_pct > 0.0. Keep cash reserves secure above the $4.00 minimum threshold."
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
