# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-11 13:50:44`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$31.84 USD** | **$6.66 USD** | **$38.51 USD** | 🔴 **-3.74%** ($-1.49) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $353.99 | $6.66 | 📈 +2.50% | 5d 20h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market remains in a corrective phase with most assets currently trading below their SMA20 trend lines (BAJISTA). Notable exceptions like AAPL continue to show strong resilience, staying above SMA20 with positive weekly performance (+6.66%) and maintaining a profitable position (+2.5%). Cryptocurrencies and major index ETFs are experiencing mixed short-term recovery attempts, but strict quantitative rules forbid catching falling knives or entering assets below SMA20 without confirmed trend reversals. Cash is preserved above the minimum threshold."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is currently in an uptrend (above SMA20) with a profit of +2.5%, near our take-profit target range (+3.0% to +5.0%). Per equity holding patience rules, we maintain the position and do not prematurely liquidate stable winning assets.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL in line with equity holding patience rules. AAPL is showing positive momentum and sits securely above its SMA20. We will continue monitoring AAPL for take-profit targets (+3.0% to +5.0%) or stop-loss limits (-2.0%). We remain disciplined, avoiding all downtrend assets and waiting for confirmed uptrends before deploying additional capital."
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
