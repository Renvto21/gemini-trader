# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-11 12:10:43`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.01 USD** | **$13.53 USD** | **$38.54 USD** | 🔴 **-3.64%** ($-1.46) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $353.20 | $6.65 | 📈 +2.27% | 5d 18h |
| `MSFT` | 0.013089 | $534.82 | $525.88 | $6.88 | 📉 -1.67% | 4d 22h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Major equity indices like SPY and QQQ show partial recoveries following positive tech earnings (CoreWeave), but most underlying assets remain below their SMA20 trend lines, classified as bearish or consolidating. AAPL maintains a solid uptrend above its SMA20 with positive 1-hour and 7-day momentum (+6.42%). MSFT has slipped below its SMA20 with a 1-hour RSI dropping to 30.2, bringing its PnL close to the stop-loss limit (-1.67%). Cryptocurrencies remain under pressure, generally situated below their daily SMA20 lines without meeting the strict pullback reversal criteria."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 80%): AAPL is in a confirmed uptrend above its SMA20 with positive momentum and a 2.27% profit. Sticking to the equity holding patience rule to let winners run.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "AAPL is performing well and holding steady above its SMA20; I will let winners run toward the +3% to +5% take-profit target. MSFT is currently hovering near the -1.67% mark; if it dips further toward -1.8% or lower, the stop-loss circuit breaker will execute. Cash reserves are healthy at $25.01 USD. No new buys executed as no assets currently meet all strict quantitative trend and reversal triggers simultaneously."
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
