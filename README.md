# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-27 13:31:06`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.75 USD** | **$13.53 USD** | **$39.28 USD** | 🔴 **-1.81%** ($-0.72) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $346.55 | $6.99 | 📉 -0.18% | 3d 23h |
| `MSFT` | 0.012263 | $530.04 | $533.28 | $6.54 | 📈 +0.61% | 1d 1h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market continues to exhibit a mixed technical picture. Major indices like SPY, QQQ, NVDA, and GLD are currently trading in bearish trends below their respective SMA20 lines, despite some intraday bounces. In contrast, AAPL and MSFT remain in confirmed uptrends above their SMA20 lines. Crypto assets (SOL-USD, BTC-USD, ETH-USD) show short-term positive 1-hour changes but remain in broader weekly downtrends below the SMA20, prompting us to stay sidelined in crypto per our strict trend filter."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is in a confirmed uptrend above the SMA20 with solid daily RSI. Adhering to equity patience rules, we hold the position as it consolidates.
- **[HOLD] MSFT** (Confidence: 90%): MSFT remains above its SMA20 in a confirmed uptrend with a positive PnL (+0.61%). We continue to hold while monitoring for the +3.0% to +5.0% profit target window.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain current equity holdings in AAPL and MSFT as they remain in confirmed uptrends above the SMA20. MSFT shows a 1h RSI above 72 with a modest profit; monitor closely for profit-taking in the +3.0% to +5.0% target zone or exit if momentum stalls. AAPL is consolidating nicely and should be given time to develop per equity holding patience rules. Strictly respect stop-loss levels (-1.8% to -2.0%) and avoid all assets in downtrends."
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
