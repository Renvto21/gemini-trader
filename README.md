# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-11 23:30:45`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$31.84 USD** | **$6.56 USD** | **$38.40 USD** | 🔴 **-3.99%** ($-1.60) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $348.51 | $6.56 | 📈 +0.92% | 6d 5h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "All traditional equities and ETF markets are currently closed (CERRADO) for the weekend, preventing any trading actions on stocks like AAPL, which is currently holding steady with a modest +0.92% PnL. In the crypto markets, which remain open 24/7, assets like BTC-USD, SOL-USD, and ETH-USD are showing minor 1-hour recovery bounces with positive 1-hour percentage changes. However, all crypto assets remain strictly in a downtrend (below their SMA20), violating our Trend Filter rule (Rule of Gold). Therefore, we must maintain a disciplined stance, holding our current AAPL position and keeping crypto sidelined until confirmed uptrends materialize upon market reopening."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): AAPL is currently held in an uptrend above its SMA20 with a positive PnL (+0.92%). Market status is closed, and equity holding patience dictates maintaining positions through the weekend unless stop-loss limits are approached.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain the current AAPL position as equity holding patience dictates letting quality stocks play out while markets are closed. Monitor AAPL closely upon market open for potential profit-taking targets between +3.0% and +5.0% or if 1-hour RSI exceeds 72. Keep all crypto assets sidelined since they remain in bear trends below the SMA20, despite short-term 1-hour green candles. Ensure cash reserves remain above the $4.00 minimum."
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
