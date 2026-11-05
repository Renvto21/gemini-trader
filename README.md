# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-05 03:40:44`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$31.78 USD** | **$6.99 USD** | **$38.78 USD** | 🔴 **-3.05%** ($-1.22) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.002886 | $2425.59 | $2423.61 | $6.99 | 📉 -0.08% | 1h 59m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Wall Street equities and precious metals are currently closed for the weekend/night sessions, meaning liquidity is restricted to 24/7 crypto markets. Within crypto, ETH-USD maintains an uptrend above its SMA20 with positive 1-hour momentum, fulfilling our quantitative criteria for a continued hold. Our current position in ETH-USD is performing stably with minimal drawdown (-0.08%), safely away from our -2.0% circuit breaker stop-loss. Other assets like BTC-USD are also above SMA20, but due to anti-correlation constraints restricting us to a single crypto position, we will continue holding ETH-USD and let the trade develop toward our +3.5% to +5.0% target."

**Cycle Actions:**
- **[HOLD] ETH-USD** (Confidence: 85%): ETH-USD remains in a confirmed uptrend above its SMA20 with positive 1-hour momentum (+0.29%). The position is healthy, well within risk parameters, and awaiting further upside toward our +3.5% target.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Currently holding ETH-USD opened at $2425.59. Maintain stop-loss at -1.8% to -2.0% ($2377-2380) and target a profit take between +3.0% and +5.0% ($2500-2540). Wall Street assets (AAPL, MSFT, GLD, QQQ, SPY, NVDA) are closed; wait for market open before evaluating equities. Adhere strictly to the single crypto position rule."
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
