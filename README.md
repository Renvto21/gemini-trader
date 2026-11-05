# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-05 05:10:39`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$31.78 USD** | **$6.99 USD** | **$38.77 USD** | 🔴 **-3.07%** ($-1.23) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.002886 | $2425.59 | $2421.02 | $6.99 | 📉 -0.19% | 3h 29m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Wall Street equities (QQQ, SPY, MSFT, AAPL, NVDA, GLD) are currently closed, with prices frozen. Cryptocurrencies are open 24/7. Among the open assets, ETH-USD and BTC-USD are trading in confirmed uptrends above their SMA20. ETH-USD is currently held in the portfolio with a healthy RSI and positive hourly momentum, adhering to our anti-correlation rule of holding only one crypto position. Wall Street equities such as MSFT and AAPL remain closed, so we maintain our current positions or hold cash until markets reopen."

**Cycle Actions:**
- **[HOLD] ETH-USD** (Confidence: 85%): ETH-USD is in a confirmed uptrend above its SMA20, positive 1-hour change, and healthy RSI. We hold this position in accordance with the 1-crypto maximum rule and let the winner run toward our +3% to +5% target.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding ETH-USD as our single active crypto position. Target profit for ETH-USD is set between +3% and +5% (around $2500+), with a strict stop-loss at -2.0% to protect capital. Wall Street assets are closed; will evaluate AAPL and MSFT pullbacks when traditional markets reopen."
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
