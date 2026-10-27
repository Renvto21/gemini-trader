# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-27 12:50:52`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.75 USD** | **$13.56 USD** | **$39.30 USD** | 🔴 **-1.74%** ($-0.70) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $347.29 | $7.00 | 📈 +0.03% | 3d 23h |
| `MSFT` | 0.012263 | $530.04 | $534.36 | $6.55 | 📈 +0.82% | 1d 0h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The market shows mixed conditions with several major indices and assets remaining below their SMA20 trend lines, categorized as bearish trends. However, AAPL and MSFT remain securely in confirmed uptrends above their SMA20 lines. Both of our open positions (AAPL and MSFT) are performing well within expectations, respecting equity holding patience rules. MSFT is currently up +0.82% with a 1h RSI of 75.8, approaching our potential profit-taking threshold if momentum persists, while AAPL remains stable. No new trades are initiated currently as we maintain our equity positions and wait for optimal asymmetric setups."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is in a confirmed uptrend above its SMA20 and is currently showing stable positive performance. Holding as per equity holding patience and letting the trend run toward the target.
- **[HOLD] MSFT** (Confidence: 90%): MSFT remains in a confirmed uptrend above its SMA20 with a +0.82% gain. Monitoring 1h RSI (75.8) for potential take-profit conditions if profits reach >= +2.5%.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain current equity positions in AAPL and MSFT. Exercise equity holding patience, letting winners run towards the +3.0% to +5.0% profit target or monitoring MSFT for a potential exit if 1h RSI remains above 72 with profits >= +2.5%. Keep enforcing the strict stop-loss circuit breaker at -1.8% to -2.0% for risk management. Continue avoiding assets below their SMA20 trend line and uphold the single crypto position constraint."
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
