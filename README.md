# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-12 06:20:52`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$31.84 USD** | **$6.69 USD** | **$38.54 USD** | 🔴 **-3.66%** ($-1.46) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $355.63 | $6.69 | 📈 +2.98% | 6d 12h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market condition remains cautious with major equities and commodities currently sitting below their SMA20 trend lines while Wall Street is closed (market status CERRADO). Cryptocurrencies (SOL-USD, ETH-USD, BTC-USD) are trading 24/7 but remain in a strong downtrend (below SMA20) with negative 1-hour momentum, preventing any new buy entries under strict trend filters. Our sole open position, AAPL, is in a confirmed uptrend (above SMA20) with a healthy PnL of +2.98% and a 1-hour RSI of 70.4. Equity holding patience rules apply, and we will hold AAPL until take-profit conditions (+3.5% to +5.0% or 1H RSI > 72) are met."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 95%): AAPL is in a confirmed uptrend above SMA20 with a solid PnL of +2.98%. Following equity holding patience rules, we maintain the position as it approaches take-profit territory without triggering any stop-loss criteria.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Continue holding AAPL under equity holding patience rules, targeting a take-profit execution if 1-hour RSI exceeds 72 or PnL hits +3.5% to +5.0%. Maintain strict discipline on crypto and closed-market assets: do not enter any positions until they reclaim their SMA20 and exhibit confirmed positive reversal candles. Cash reserves remain safe at $31.84."
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
