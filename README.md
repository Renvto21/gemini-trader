# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-27 15:10:41`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.75 USD** | **$13.48 USD** | **$39.23 USD** | 🔴 **-1.92%** ($-0.77) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $345.63 | $6.97 | 📉 -0.44% | 4d 1h |
| `MSFT` | 0.012263 | $530.04 | $531.34 | $6.52 | 📈 +0.25% | 1d 3h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market presents a cautious picture with most assets trading below their SMA20, signaling bearish or consolidation trends across key indices and commodities. However, AAPL and MSFT remain resiliently above their SMA20 in confirmed uptrends. AAPL is currently down slightly by -0.44% while MSFT shows a modest gain of +0.25%. Per our equity holding patience rule, we will maintain these existing stock positions and allow them time to develop, avoiding premature exits while keeping stop-losses strictly monitored."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL remains in a confirmed uptrend above its SMA20. Holding per equity patience guidelines as the position is experiencing minor normal fluctuations.
- **[HOLD] MSFT** (Confidence: 85%): MSFT remains above its SMA20 in an uptrend with a positive PnL. Maintaining position to let the winner run toward the +3.0% to +5.0% profit target.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain current holdings in AAPL and MSFT as both remain in confirmed uptrends above the SMA20. Monitor MSFT and AAPL for take-profit targets between +3.0% and +5.0% or if the 1-hour RSI exceeds 72. Enforce stop-losses strictly at -1.8% to -2.0%. Avoid opening new crypto or equity positions until clear pullback bounce confirmations are satisfied."
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
