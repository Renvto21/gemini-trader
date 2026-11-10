# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-10 20:50:37`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.01 USD** | **$13.54 USD** | **$38.55 USD** | 🔴 **-3.63%** ($-1.45) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $348.51 | $6.56 | 📈 +0.92% | 5d 3h |
| `MSFT` | 0.013089 | $534.82 | $533.16 | $6.98 | 📉 -0.31% | 4d 7h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Wall Street markets are currently closed (CERRADO), preventing any active stock or ETF trading during this cycle. Equity holdings AAPL and MSFT remain stable; AAPL is showing positive momentum (+0.92% PnL) while holding above its SMA20 uptrend. MSFT is slightly negative (-0.31%) but comfortably above its stop-loss boundary and remains in a confirmed uptrend. Cryptocurrency markets (BTC-USD, ETH-USD, SOL-USD) are open 24/7 but remain firmly in a BAJISTA (below SMA20) macro bear trend. Despite minor hourly recovery attempts, strict quantitative filters forbid catching falling knives or entering crypto assets under bearish conditions. Cash reserves are maintained safely above the $4.00 minimum at $25.01."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): Asset is in a confirmed uptrend above SMA20 with positive PnL (+0.92%). Market is closed, and equity holding patience rule applies to avoid premature rotation.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing positions in AAPL and MSFT as equity holding patience dictates giving stocks time to work despite flat near-term action. Monitor stop-losses strictly around -1.8% to -2.0% and profit targets at +3.0% to +5.0%. Keep crypto assets sidelined until daily and hourly structures reclaim their SMA20 trend lines and confirm bullish reversals."
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
