# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-06 21:20:45`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.14 USD** | **$13.39 USD** | **$38.53 USD** | 🔴 **-3.69%** ($-1.47) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $342.37 | $6.44 | 📉 -0.86% | 1d 3h |
| `MSFT` | 0.013089 | $534.82 | $530.61 | $6.94 | 📉 -0.79% | 8h 10m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market is currently experiencing a broad consolidation/downtrend with all tracked assets resting below their respective SMA20 lines, indicating a bearish macro environment. Wall Street assets (AAPL, MSFT, SPY, QQQ, NVDA, GLD) are currently closed ('CERRADO'), so their prices are frozen and no actions can be taken on them. Crypto assets are open (24/7), and while SOL-USD and ETH-USD show positive 1-hour changes and RSIs above 32, they are still trading under the strict downtrend filter (below SMA20), violating our rule of never catching falling knives. Therefore, no new crypto trades will be opened."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): Asset market status is closed and the holding is within acceptable drawdown limits (-0.86%). Equity holding patience rule applies; do not panic sell.
- **[HOLD] MSFT** (Confidence: 90%): Asset market status is closed and the holding is within acceptable drawdown limits (-0.79%). Equity holding patience rule applies; do not panic sell.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain patience with current equity positions (AAPL and MSFT) through the weekend market closure. Strictly monitor their -2.0% stop-loss circuit breakers upon market reopening. Avoid entering any crypto positions as all assets remain below the SMA20 trend filter, even though SOL-USD and ETH-USD show mild 1-hour recoveries. Wait for confirmed uptrends and positive 1-hour momentum candles before deploying additional capital."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **89** | 🎯 **42.7%** (38W / 36L / 15BE) | 🔴 **$-1.23 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-06 13:10` | 🟢 BUY | `MSFT` | $7.00 | $534.82 | MSFT is in a confirmed uptrend above its SMA20, market status is open, 1-hour RSI has reco... |
| `2026-11-05 17:40` | 🟢 BUY | `AAPL` | $6.50 | $345.35 | AAPL is in a confirmed uptrend above its SMA20, market status is open, and 1-hour momentum... |
| `2026-11-05 11:20` | 🔴 SELL (-0.15$) | `ETH-USD` | $6.85 | $2374.60 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -2.10% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-05 01:41` | 🟢 BUY | `ETH-USD` | $7.00 | $2425.59 | ETH-USD is in a confirmed uptrend above its SMA20, market status is open 24/7, 1-hour RSI ... |
| `2026-11-04 22:00` | 🔴 SELL (-0.31$) | `MSFT` | $6.69 | $520.99 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -4.44% hit safety limit (-2.0%). Liquidated by code... |

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
