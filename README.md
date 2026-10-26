# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-26 06:00:49`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.25 USD** | **$7.01 USD** | **$39.26 USD** | 🔴 **-1.85%** ($-0.74) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $347.73 | $7.01 | 📈 +0.16% | 2d 16h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The equity markets remain closed (market_status CERRADO), meaning existing equity positions like AAPL must be held with patience while awaiting market reopening. AAPL maintains an uptrend above SMA20 with a current PnL of +0.16% and an RSI_1h of 66.0, not yet hitting our take-profit threshold (+3.0% to +5.0% gain or RSI_1h > 72 with profit >= +2.5%) or stop-loss limit. In the crypto sector (ABIERTO 24/7), assets such as SOL-USD, ETH-USD, and BTC-USD remain in a BAJISTA (below SMA20) trend, violating our strict trend-filter rule against catching falling knives. Therefore, no crypto trades are executed, and we maintain cash reserves."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is currently in an established uptrend above SMA20 with a positive PnL. Equity markets are closed, and the position has not met take-profit or stop-loss criteria, adhering to equity holding patience rules.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain the current AAPL equity position as Wall Street is closed. Continue monitoring AAPL for take-profit targets (+3.0% to +5.0% or RSI_1h > 72 with profit >= +2.5%) or strict stop-loss protection (-1.8% to -2.0%). Keep crypto sidelined as all available options remain below their SMA20 trend lines. Re-evaluate crypto and equity setups once the market reopens."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **85** | 🎯 **44.7%** (38W / 32L / 15BE) | 🔴 **$-0.62 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-23 13:40` | 🟢 BUY | `AAPL` | $7.00 | $347.17 | AAPL is in a confirmed uptrend above its SMA20, satisfying our strict trend filter. The 1-... |
| `2026-10-22 16:00` | 🔴 SELL (-0.12$) | `MSFT` | $6.88 | $521.40 | MSFT has dropped to a PnL of -1.71%, closely approaching our mandatory stop-loss threshold... |
| `2026-10-22 14:40` | 🔴 SELL (+0.17$) | `AAPL` | $10.17 | $346.52 | AAPL rsi_1h has surpassed 72 (currently 73.4) with a positive return of +1.73%, satisfying... |
| `2026-10-21 12:01` | 🟢 BUY | `MSFT` | $7.00 | $530.45 | MSFT is in a confirmed uptrend above its SMA20. The 1-hour RSI is at 36.7 (above the 32 th... |
| `2026-10-21 10:10` | 🔴 SELL (+0.12$) | `ETH-USD` | $10.07 | $2481.87 | ETH-USD rsi_1h has surpassed 72 (currently 73.7) with a positive return of +1.21%, satisfy... |

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
