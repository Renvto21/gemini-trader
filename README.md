# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-05 03:20:40`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$31.78 USD** | **$7.00 USD** | **$38.78 USD** | 🔴 **-3.05%** ($-1.22) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.002886 | $2425.59 | $2424.66 | $7.00 | 📉 -0.04% | 1h 39m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The portfolio currently holds an ETH-USD position opened during a confirmed uptrend with positive 1-hour momentum. Traditional equity markets remain closed (CERRADO), meaning active liquidity must remain focused on 24/7 crypto assets. BTC-USD and ETH-USD are both above their SMA20 with positive 1-hour percentage changes, satisfying trend and reversal filters. However, due to the anti-correlation constraint allowing only one active crypto position, we maintain our current ETH-USD holding and wait for it to reach its take-profit target (+3.0% to +5.0%) or hit the hard stop-loss circuit breaker."

**Cycle Actions:**
- **[HOLD] ETH-USD** (Confidence: 85%): ETH-USD remains in a confirmed uptrend above its SMA20 with positive hourly momentum. The position is well within risk parameters; we adhere to equity holding patience and asymmetric reward targets.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding ETH-USD. Monitor for take-profit between +3.0% and +5.0% or RSI > 72. Respect the strict -2.0% stop-loss circuit breaker. Maintain cash reserves and wait for traditional markets to open before evaluating equity assets such as AAPL or MSFT."
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
