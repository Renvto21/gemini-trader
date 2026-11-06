# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-06 12:10:44`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.14 USD** | **$6.43 USD** | **$38.57 USD** | 🔴 **-3.57%** ($-1.43) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $341.84 | $6.43 | 📉 -1.02% | 18h 30m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market is experiencing a cautious tech and equity downturn, with most assets currently trading below their SMA20 trend line, reflecting a bearish macro sentiment. However, some individual stocks like MSFT show strong relative standing with an uptrend status. AAPL is currently held in the portfolio despite a minor pullback, but since its trend has shifted below SMA20 and 1-hour change is negative, it will be monitored closely for stop-loss limits. No new crypto positions will be initiated as they remain below their SMA20 trend lines, failing our strict uptrend pullback criteria."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is currently held in the portfolio. Although it has dipped below the SMA20 trend line, equity holding patience dictates we give stocks time to play out unless the strict -1.8% to -2.0% stop-loss circuit breaker is triggered.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL position while vigilantly tracking the -1.8% to -2.0% stop-loss circuit breaker. MSFT is showing an uptrend but its 1-hour change is negative (-0.63%), failing the reversal confirmation trigger. Will wait for confirmed positive 1-hour momentum and RSI >= 32 before entering any new pullback opportunities."
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
