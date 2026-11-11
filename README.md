# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-11 00:50:49`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.01 USD** | **$13.54 USD** | **$38.55 USD** | 🔴 **-3.63%** ($-1.45) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $348.51 | $6.56 | 📈 +0.92% | 5d 7h |
| `MSFT` | 0.013089 | $534.82 | $533.16 | $6.98 | 📉 -0.31% | 4d 11h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market is currently closed for equities, showing frozen prices with major indices and stocks under varying conditions. Cryptocurrencies remain open (24/7), but all primary crypto assets (SOL-USD, BTC-USD, ETH-USD) are in clear downtrends below their SMA20 with negative 24h performance, violating our strict trend filter. Our equity holdings AAPL and MSFT remain in closed status; AAPL is in a confirmed uptrend (above SMA20) with a positive PnL of +0.92%, while MSFT is also in a confirmed uptrend with a minor PnL of -0.31%, well within normal equity fluctuation bounds and far above the strict -2.0% stop-loss circuit breaker."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): AAPL is in a confirmed uptrend above SMA20 and is currently profitable (+0.92%). Equity holding patience dictates maintaining the position during closed market hours until take-profit or stop-loss parameters are reached.
- **[HOLD] MSFT** (Confidence: 100%): MSFT is in a confirmed uptrend above SMA20 with a minor drawdown (-0.31%), well above the -2.0% stop-loss threshold. Equity holding patience applies during closed market hours.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing positions in AAPL and MSFT during closed market hours, adhering to equity holding patience. Do not buy any crypto assets as they fail the trend filter (all below SMA20). Wait for Wall Street reopening to monitor AAPL and MSFT for take-profit targets (+3.5% to +5.0%) or strict stop-losses if the -2.0% threshold is breached."
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
