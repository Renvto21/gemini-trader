# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-06 11:30:51`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.14 USD** | **$6.39 USD** | **$38.53 USD** | 🔴 **-3.68%** ($-1.47) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $339.58 | $6.39 | 📉 -1.67% | 17h 50m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market remains under pressure with all tracked assets currently positioned in a bearish trend below their respective SMA20 levels, reflecting ongoing macroeconomic headwinds and technology sector sell-offs. Our current holding, AAPL, is down approximately 1.67% and nearing our strict stop-loss threshold (-2.0%). However, adhering to equity holding patience and capital preservation principles, we continue to monitor the position closely without premature panic selling, awaiting either a recovery towards take-profit targets (+3.0% to +5.0%) or automatic risk mitigation via the stop-loss circuit breaker. No new positions are initiated as potential setups fail to meet strict trend-following pullback criteria."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is currently held in the portfolio with a minor drawdown (-1.67%). Following equity holding patience guidelines, we do not sell prematurely for flat movement unless the hard stop-loss of -2.0% is triggered or the take-profit target (+3.0% to +5.0%) is reached.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL position while closely monitoring the -2.0% stop-loss threshold. Do not buy any assets currently trading below SMA20. Maintain cash reserves above $4.00 USD and wait for confirmed uptrend breakouts and positive 1-hour reversal candles before deploying new capital."
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
