# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-10 11:31:03`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.01 USD** | **$13.74 USD** | **$38.75 USD** | 🔴 **-3.12%** ($-1.25) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $352.51 | $6.63 | 📈 +2.07% | 4d 17h |
| `MSFT` | 0.013089 | $534.82 | $542.95 | $7.11 | 📈 +1.52% | 3d 22h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Wall Street is open and experiencing mixed conditions with several major indices and assets sliding below their SMA20. However, AAPL and MSFT remain resilient in confirmed uptrends above their SMA20. GLD has slipped below its SMA20 trend line, registering a loss of -1.78% which approaches our stop-loss threshold. Cryptocurrencies remain under heavy bearish pressure below their SMA20 with weak momentum, meaning no crypto positions will be initiated."

**Cycle Actions:**
- **[SELL] GLD** (Confidence: 90%): GLD has fallen below its SMA20 trend line and its current PnL is approaching the strict stop-loss limit of -1.8%, triggering our capital preservation rule to cut losses fast.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL and MSFT as they continue to respect their uptrends. GLD is nearing our stop-loss parameter (-1.78% PnL); will monitor closely and cut if it breaches -1.8% to preserve capital. No new entries today as most candidates are below SMA20 or lack the required 1-hour green candle confirmation."
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
