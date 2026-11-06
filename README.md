# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-06 18:00:59`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.14 USD** | **$13.40 USD** | **$38.53 USD** | 🔴 **-3.66%** ($-1.47) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $342.51 | $6.45 | 📉 -0.82% | 1d 0h |
| `MSFT` | 0.013089 | $534.82 | $531.10 | $6.95 | 📉 -0.70% | 4h 50m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market continues to experience a broad macro correction with all tracked assets currently positioned below their SMA20 trend lines in a bearish state. Wall Street equities (AAPL, MSFT, SPY, QQQ, NVDA, GLD) are currently closed for the weekend, meaning no equity transactions can or should take place. Cryptocurrencies are trading live 24/7, but they also remain under structural pressure. Our current equity holdings (AAPL and MSFT) are exhibiting minor unrealized drawdowns but must be held patiently in accordance with the equity holding patience rule, provided they do not breach the hard stop-loss threshold (-1.8% to -2.0%). No new crypto or stock buys meet our strict trend filter criteria since none are currently in an established uptrend above SMA20 with confirmed positive momentum triggers."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): Holding current AAPL position patiently per equity holding rules. Price is slightly below entry but well above the stop-loss threshold, and equity markets are closed.
- **[HOLD] MSFT** (Confidence: 100%): Holding current MSFT position patiently per equity holding rules. Drawdown is minor and well within risk parameters while equity markets remain closed.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL and MSFT patiently according to equity holding rules. Both positions are currently showing slight negative returns but are well within acceptable volatility bands above our strict stop-loss limit of -2.0%. Wall Street is closed, and crypto markets lack confirmed uptrend structures above SMA20, so cash reserves of $25.14 USD remain safely untouched. Maintain discipline and wait for assets to reclaim their SMA20 lines before entering new pullback setups."
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
