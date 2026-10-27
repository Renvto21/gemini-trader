# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-27 12:10:52`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.75 USD** | **$13.54 USD** | **$39.29 USD** | 🔴 **-1.78%** ($-0.71) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $347.35 | $7.00 | 📈 +0.05% | 3d 22h |
| `MSFT` | 0.012263 | $530.04 | $532.99 | $6.54 | 📈 +0.56% | 1d 0h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market continues to show a mixed trend with major indices like SPY, QQQ, and NVDA remaining in bearish territory below their SMA20 lines. However, individual tech equities AAPL and MSFT remain strong in confirmed uptrends above their SMA20 with positive 1-hour performance. Cryptocurrencies are consolidating under downward pressure and remain below their SMA20 trend filters, making them ineligible for entry under strict quantitative rules. Capital preservation and equity holding patience remain top priorities."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL remains in a confirmed uptrend above its SMA20 with positive momentum. Complying with equity holding patience rules, we hold the position to let winners run toward our +3.0% to +5.0% profit target.
- **[HOLD] MSFT** (Confidence: 90%): MSFT is holding steady above its SMA20 with positive 1H and 24H changes. Following the equity holding patience guidelines, we maintain the position as stop-losses have not been breached and profits are building.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing positions in AAPL and MSFT following equity holding patience rules. Wait for take-profit targets between +3.0% and +5.0% or 1-hour RSI levels exceeding 72 before locking in gains. Enforce strict stop-losses at -1.8% to -2.0% to protect capital. Continue to avoid all crypto assets due to bearish trend conditions below the SMA20."
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
