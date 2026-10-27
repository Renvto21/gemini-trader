# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-27 00:10:39`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.75 USD** | **$13.47 USD** | **$39.21 USD** | 🔴 **-1.96%** ($-0.79) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $343.91 | $6.93 | 📉 -0.94% | 3d 10h |
| `MSFT` | 0.012263 | $530.04 | $532.60 | $6.53 | 📈 +0.48% | 12h 9m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market is currently experiencing closed conditions for Wall Street equities (AAPL, MSFT, QQQ, SPY, NVDA, GLD), which means positions cannot be traded at this moment. Cryptocurrencies are open (24/7), but all major crypto assets (SOL-USD, BTC-USD, ETH-USD) remain in a bearish trend below their SMA20 with negative or neutral momentum, failing our strict trend and reversal filters. In our equity portfolio, AAPL is holding steady at -0.94% PnL, and MSFT shows a positive PnL of +0.48% while above its SMA20. Following equity holding patience, we will maintain both positions until market reopens or stop-loss/take-profit thresholds are met."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): Asset is in an uptrend above SMA20, but the market status is closed. Adhering to equity holding patience to let the position develop.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing equity positions in AAPL and MSFT. Wall Street is currently closed; do not attempt any equity trades. Crypto markets are open but all tracked coins are below SMA20 and lack valid 1-hour green candle confirmation, so stay in cash for crypto. Monitor MSFT for potential take-profit targets (+3.0% to +5.0%) and AAPL/MSFT for stop-loss triggers (-1.8%)."
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
