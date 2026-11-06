# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-06 15:20:42`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.14 USD** | **$13.44 USD** | **$38.58 USD** | 🔴 **-3.55%** ($-1.42) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $343.73 | $6.47 | 📉 -0.47% | 21h 39m |
| `MSFT` | 0.013089 | $534.82 | $532.88 | $6.97 | 📉 -0.36% | 2h 9m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market remains fragile with major indices like QQQ, SPY, and NVDA trading in bear trends below their SMA20 amidst ongoing volatility in the tech and AI sectors. Our current holdings, AAPL and MSFT, are experiencing minor pullbacks but remain structurally sound in confirmed uptrends above the SMA20. Per our equity patience and trend-following rules, we hold our positions while keeping a close eye on stop-loss thresholds (-2%). No crypto assets meet our strict criteria today since all major tokens are under their SMA20 or lack the required 1-hour green momentum."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in a confirmed uptrend above the SMA20. Despite a minor 1-hour dip, equity holding patience dictates we allow the stock time to play out without panic-selling, as it hasn't hit our stop-loss or take-profit targets.
- **[HOLD] MSFT** (Confidence: 85%): MSFT remains above its SMA20 in an overall uptrend. The minor downward movement is within normal pullback parameters, and patience is maintained in accordance with our equity rules.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL and MSFT patiently. Both are showing minor hourly dips but remain above the SMA20 trend filter. Stop-loss hard limit is set at -2.0% for both positions, and take-profit targets are placed at +3% to +5%. Will continue to monitor for a reversal confirmation trigger if any equity or crypto asset sets up properly in subsequent cycles."
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
