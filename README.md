# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-26 14:01:15`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.75 USD** | **$13.44 USD** | **$39.19 USD** | 🔴 **-2.02%** ($-0.81) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $343.87 | $6.93 | 📉 -0.95% | 3d 0h |
| `MSFT` | 0.012263 | $530.04 | $530.72 | $6.51 | 📈 +0.13% | 1h 59m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market shows mixed signals with most major indices and crypto assets still in a bearish trend below their respective SMA20 lines. However, select equities like MSFT and AAPL maintain their status above the SMA20 uptrend filter, supporting our current stock positions. AAPL is experiencing a mild pullback with a negative 1-hour change (-0.23%) and an RSI of 40.5, while MSFT remains stable with a positive 1-hour change and strong momentum. Crypto assets remain in downtrends and are avoided due to anti-correlation constraints and trend filters."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is in a confirmed uptrend above the SMA20. Although experiencing a minor pullback (-0.23% in the last hour), equity holding patience rules dictate we give stocks time to play out unless stop-loss limits are breached.
- **[HOLD] MSFT** (Confidence: 90%): MSFT is holding steady above its SMA20 with positive 1-hour momentum. We continue to let our winner run toward the +3.0% to +5.0% take-profit target while protecting capital with a strict stop-loss.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain current positions in AAPL and MSFT as both remain in confirmed uptrends above their SMA20 lines. Give AAPL time to recover from its minor hourly dip without panicking, and monitor MSFT for potential take-profit targets between +3.0% and +5.0%. Keep cash reserves above $4.00 USD and refrain from entering any crypto assets until trend reversals above the SMA20 are confirmed."
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
