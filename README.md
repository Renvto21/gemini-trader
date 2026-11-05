# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-05 06:40:46`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$31.78 USD** | **$6.96 USD** | **$38.75 USD** | 🔴 **-3.13%** ($-1.25) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.002886 | $2425.59 | $2412.94 | $6.96 | 📉 -0.52% | 4h 59m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The traditional equity and ETF markets are currently closed (CERRADO), showing frozen prices and mixed 24-hour sentiment. Among crypto assets trading 24/7, ETH-USD remains in a confirmed uptrend above its SMA20, though it is experiencing a minor consolidation with a negative 1-hour percentage change (-0.22%) and a 1-hour RSI of 54.2. BTC-USD is also in an uptrend above its SMA20, trading above $80,000. Our active position in ETH-USD is down slightly by -0.52%, well above our -1.8% stop-loss threshold. Since the 1-hour candle is not yet green (change_1h_pct is -0.22%), we must hold patience and let the position play out according to our trend-following rules."

**Cycle Actions:**
- **[HOLD] ETH-USD** (Confidence: 80%): ETH-USD is in a confirmed uptrend above its SMA20, and our current loss (-0.52%) is safely within acceptable limits far above our -1.8% stop-loss threshold. The 1-hour change is slightly negative (-0.22%), meaning we hold patiently until the bounce confirmation triggers or the target is reached.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding ETH-USD acquired at 2425.59. Current stop-loss is protected around 2380 (-1.8%) and take-profit target remains set at 2500 (+3.0%). Maintaining patience and waiting for a confirmed green 1-hour candle bounce before considering any scaling or additional entries. Cash reserve is healthy at $31.78."
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
