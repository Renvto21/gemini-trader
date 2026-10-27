# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-27 15:40:47`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.75 USD** | **$13.48 USD** | **$39.23 USD** | 🔴 **-1.93%** ($-0.77) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $345.88 | $6.97 | 📉 -0.37% | 4d 2h |
| `MSFT` | 0.012263 | $530.04 | $530.60 | $6.51 | 📈 +0.11% | 1d 3h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market continues to present a mixed picture with major indices like SPY, QQQ, and crypto assets trading predominantly below their SMA20, indicating broader bearish trends. However, AAPL and MSFT remain strong in confirmed uptrends above their SMA20. AAPL is holding steady with a minor negative PnL (-0.37%), and MSFT is slightly positive (+0.11%). Adhering to the equity holding patience rule, we will maintain both positions as they have not hit stop-losses nor reached profit targets, and avoid opening new positions given the lack of optimal risk/reward pullbacks."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): AAPL is above its SMA20 in a confirmed uptrend. Per equity holding patience rules, we do not rotate or sell prematurely and will let the trade play out.
- **[HOLD] MSFT** (Confidence: 100%): MSFT is above its SMA20 in a confirmed uptrend with a slight positive PnL. Maintaining position to allow target gains to develop.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing positions in AAPL and MSFT. Both assets are in confirmed uptrends above the SMA20. Monitor closely for take-profit opportunities (+3.0% to +5.0%) or strict stop-loss protection (-1.8% to -2.0%). Keep cash reserves intact and avoid entering assets below their SMA20 or crypto while holding equities."
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
