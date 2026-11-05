# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-05 10:50:46`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$31.78 USD** | **$6.90 USD** | **$38.68 USD** | 🔴 **-3.30%** ($-1.32) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.002886 | $2425.59 | $2389.57 | $6.90 | 📉 -1.48% | 9h 9m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Wall Street traditional markets remain closed (CERRADO), leaving crypto as the only active liquidity vehicle (ABIERTO 24/7). ETH-USD is currently holding an open position in a confirmed uptrend (above SMA20), though its 1-hour RSI has dipped slightly to 31.4 with a minor negative 1-hour change (-0.07%). BTC-USD and SOL-USD remain in bearish trends below their SMA20, violating our strict trend-filter rule. MSFT and AAPL show bullish trends above SMA20 but cannot be traded due to market closures. We maintain our current ETH-USD position as it has not triggered our stop-loss nor reached our take-profit target, and we adhere to equity holding patience and anti-correlation constraints."

**Cycle Actions:**
- **[HOLD] ETH-USD** (Confidence: 85%): ETH-USD remains in a confirmed uptrend above its SMA20. The current drawdown (-1.48%) is well within acceptable limits and above our hard stop-loss threshold (-2.0%). Maintaining position to let the trade play out toward our take-profit target.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding ETH-USD with stop-loss at -2.0% ($2377.00) and take-profit target at +3.5% ($2510.00). Will monitor 1-hour momentum to ensure RSI stabilizes above 32 and price action turns green. No new crypto positions will be opened due to the single crypto asset anti-correlation constraint. Wall Street assets will be re-evaluated upon market open."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **88** | 🎯 **43.2%** (38W / 35L / 15BE) | 🔴 **$-1.08 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-05 01:41` | 🟢 BUY | `ETH-USD` | $7.00 | $2425.59 | ETH-USD is in a confirmed uptrend above its SMA20, market status is open 24/7, 1-hour RSI ... |
| `2026-11-04 22:00` | 🔴 SELL (-0.31$) | `MSFT` | $6.69 | $520.99 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -4.44% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-04 11:30` | 🟢 BUY | `MSFT` | $7.00 | $545.20 | MSFT is currently the only asset trading above its SMA20 in a confirmed uptrend with stron... |
| `2026-11-02 11:40` | 🔴 SELL (-0.13$) | `AAPL` | $6.87 | $340.69 | AAPL has slipped further into a bearish trend below its SMA20 with a 1-hour RSI of 24.8 an... |
| `2026-10-28 13:21` | 🔴 SELL (-0.02$) | `MSFT` | $6.48 | $528.16 | MSFT has shifted to a bearish trend below its SMA20 and current performance is near our st... |

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
