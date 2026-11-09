# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-09 09:30:39`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.14 USD** | **$13.39 USD** | **$38.53 USD** | 🔴 **-3.69%** ($-1.47) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $342.37 | $6.44 | 📉 -0.86% | 3d 15h |
| `MSFT` | 0.013089 | $534.82 | $530.61 | $6.94 | 📉 -0.79% | 2d 20h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Wall Street equities (AAPL, MSFT, SPY, QQQ, NVDA) are currently closed (CERRADO) for the weekend, and all of them are displaying short-term bearish trends below their respective SMA20 lines. Our open positions in AAPL and MSFT remain stable with minor unrealized losses well above our strict -1.8% to -2.0% circuit breaker. In crypto markets, which remain open 24/7, assets like ETH-USD, BTC-USD, and SOL-USD show positive 1-hour momentum and RSI levels recovering above 32, but they are all still categorized in macro downtrends (below SMA20). Following our strict quantitative rules against catching falling knives or opening multiple crypto positions while holding equity risk, no new trades are permitted this cycle."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): Asset is closed for the weekend and we adhere to equity holding patience. The current unrealized loss of -0.86% is well within our risk parameters away from the -2.0% stop-loss.
- **[HOLD] MSFT** (Confidence: 100%): Asset is closed for the weekend. The position is stable with an unrealized loss of -0.79%, comfortably away from the circuit breaker threshold.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL and MSFT through the weekend. Both positions remain safely away from the circuit breaker. We are respecting the strict trend filter rule: no crypto or equity positions will be opened until assets officially reclaim their SMA20 uptrend with confirmed positive 1-hour momentum. Maintain cash reserves above $4.00 USD."
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
