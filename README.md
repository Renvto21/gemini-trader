# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-06 11:50:38`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.14 USD** | **$6.42 USD** | **$38.56 USD** | 🔴 **-3.60%** ($-1.44) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $341.29 | $6.42 | 📉 -1.18% | 18h 9m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Macro sentiment remains cautious following a severe tech rout and broader market weakness, with all tracked assets currently classified in a bearish trend below their respective SMA20 levels. Equity indices and individual stocks like AAPL show short-term retracements, while crypto assets are range-bound with low immediate breakout conviction. Strict adherence to capital preservation and the trend-filter rule dictates avoiding new long entries in falling knife conditions, while patient holding of existing positions applies unless stop-losses are triggered."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 80%): AAPL is currently experiencing a minor pullback down -1.18%, holding above our strict -2.0% stop-loss threshold. Per equity holding patience rules, we maintain the position rather than panic-selling on flat or slightly negative short-term noise, keeping a close eye on risk parameters.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL position while carefully watching the -1.8% to -2.0% stop-loss threshold. All scanned assets are currently in a downtrend (below SMA20), violating our core trend filter for new entries. We will remain strictly on the sidelines for new purchases until assets reclaim their SMA20 and exhibit confirmed 1-hour positive momentum. Cash reserves are maintained comfortably above the $4.00 USD minimum."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **89** | 🎯 **42.7%** (38W / 36L / 15BE) | 🔴 **$-1.23 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-05 17:40` | 🟢 BUY | `AAPL` | $6.50 | $345.35 | AAPL is in a confirmed uptrend above its SMA20, market status is open, and 1-hour momentum... |
| `2026-11-05 11:20` | 🔴 SELL (-0.15$) | `ETH-USD` | $6.85 | $2374.60 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -2.10% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-05 01:41` | 🟢 BUY | `ETH-USD` | $7.00 | $2425.59 | ETH-USD is in a confirmed uptrend above its SMA20, market status is open 24/7, 1-hour RSI ... |
| `2026-11-04 22:00` | 🔴 SELL (-0.31$) | `MSFT` | $6.69 | $520.99 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -4.44% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-04 11:30` | 🟢 BUY | `MSFT` | $7.00 | $545.20 | MSFT is currently the only asset trading above its SMA20 in a confirmed uptrend with stron... |

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
