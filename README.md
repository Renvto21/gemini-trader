# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-27 11:30:53`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.75 USD** | **$13.47 USD** | **$39.22 USD** | 🔴 **-1.95%** ($-0.78) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $345.08 | $6.96 | 📉 -0.60% | 3d 21h |
| `MSFT` | 0.012263 | $530.04 | $531.16 | $6.51 | 📈 +0.21% | 23h 29m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market indices such as QQQ, SPY, and NVDA remain in a bearish trend below their respective SMA20 lines, despite mild intraday positive 1-hour candles. Crypto assets are also largely trading below their SMA20 benchmarks. Within our portfolio, MSFT is holding up well in a confirmed uptrend above its SMA20 showing a small profit (+0.21%), while AAPL is experiencing a mild pullback (-0.6%) while remaining above its SMA20 trendline with a supportive 1-hour RSI of 34.9 and a positive 1-hour percentage change. Following our equity holding patience rule, we will maintain our current stock positions and let them play out toward our profit targets without premature selling."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in a confirmed uptrend above its SMA20. Although down slightly by -0.6%, it satisfies the equity holding patience rule. We will give it time to work and avoid premature rotation.
- **[HOLD] MSFT** (Confidence: 85%): MSFT remains in a confirmed uptrend above its SMA20 and is currently showing a slight profit of +0.21%. Holding steady toward our asymmetric risk/reward take-profit target.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing positions AAPL and MSFT. Continue to respect stop-loss thresholds between -1.8% and -2.0%, and take-profit targets between +3.0% and +5.0%. Avoid opening any new positions or crypto trades until cleaner uptrends and high-conviction pullback confirmations present themselves."
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
