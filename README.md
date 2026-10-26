# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-26 15:10:39`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.75 USD** | **$13.44 USD** | **$39.19 USD** | 🔴 **-2.02%** ($-0.81) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $343.52 | $6.93 | 📉 -1.05% | 3d 1h |
| `MSFT` | 0.012263 | $530.04 | $531.37 | $6.52 | 📈 +0.25% | 3h 9m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The market is mixed with major indices showing slight variations. Equity positions remain open with MSFT exhibiting strong momentum with a 1-hour RSI at 74.5 and up 0.25% in PnL, nearing our take-profit threshold. AAPL is down -1.05% but remains in an uptrend above its SMA20, requiring adherence to equity holding patience and our strict stop-loss parameters (-1.8% to -2.0%). Cryptocurrencies and other major indices are largely below their SMA20 trends, keeping us sidelined on new crypto entries to avoid high downside correlation."

**Cycle Actions:**
- **[HOLD] MSFT** (Confidence: 80%): MSFT is in a confirmed uptrend above SMA20 and showing positive momentum with a current gain of 0.25%. Sticking to equity holding patience while monitoring for the +3.0% to +5.0% take-profit target.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain AAPL and MSFT positions. Monitor MSFT closely for profit-taking if hourly RSI remains over 72 and gains reach the +3.0% to +5.0% target zone, or cut if momentum completely reverses. Hold AAPL with patience as it is above SMA20, respecting the hard stop-loss near -1.8% to -2.0%. Keep cash reserves above $4.00 and continue avoiding downtrending assets and crypto."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **85** | 🎯 **44.7%** (38W / 32L / 15BE) | 🔴 **$-0.62 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-26 12:01` | 🟢 BUY | `MSFT` | $6.50 | $530.04 | MSFT is in a confirmed uptrend above its SMA20, and the 1-hour RSI (62.8) and 1-hour perce... |
| `2026-10-23 13:40` | 🟢 BUY | `AAPL` | $7.00 | $347.17 | AAPL is in a confirmed uptrend above its SMA20, satisfying our strict trend filter. The 1-... |
| `2026-10-22 16:00` | 🔴 SELL (-0.12$) | `MSFT` | $6.88 | $521.40 | MSFT has dropped to a PnL of -1.71%, closely approaching our mandatory stop-loss threshold... |
| `2026-10-22 14:40` | 🔴 SELL (+0.17$) | `AAPL` | $10.17 | $346.52 | AAPL rsi_1h has surpassed 72 (currently 73.4) with a positive return of +1.73%, satisfying... |
| `2026-10-21 12:01` | 🟢 BUY | `MSFT` | $7.00 | $530.45 | MSFT is in a confirmed uptrend above its SMA20. The 1-hour RSI is at 36.7 (above the 32 th... |

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
