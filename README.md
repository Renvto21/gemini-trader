# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-26 10:51:11`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.25 USD** | **$6.89 USD** | **$39.14 USD** | 🔴 **-2.16%** ($-0.86) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $341.60 | $6.89 | 📉 -1.60% | 2d 21h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market continues to exhibit broad caution, with most major assets trading below their respective SMA20 trend filters, signaling a persistent macro correction or consolidation phase. AAPL, our sole open equity position, is currently experiencing a mild pullback with a 1-hour PnL at -1.6%, approaching our stop-loss threshold of -1.8% to -2.0%. However, per our equity holding patience and strict stop-loss rules, we will hold the position unless the stop-loss is explicitly breached, or until a recovery takes place toward our take-profit targets (+3.0% to +5.0%). Cryptocurrencies and other major equities remain in downtrends or lack the required 1-hour positive reversal confirmation, keeping us on the sidelines for new capital deployment."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 80%): AAPL is currently holding at a PnL of -1.6%, approaching our mandatory stop-loss boundary (-1.8% to -2.0%). In accordance with our equity holding patience and risk rules, we maintain the position without panic, letting it play out unless the circuit breaker stop-loss level is crossed.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Monitor AAPL closely for a potential stop-loss activation if it drops past -1.8% to -2.0%, or wait patiently for a 1-hour candle recovery and RSI expansion to target a +3.0% to +5.0% gain. Keep cash reserves intact and do not enter new positions until strict trend and reversal criteria are satisfied."
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
