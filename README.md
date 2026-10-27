# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-27 01:50:43`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.75 USD** | **$13.47 USD** | **$39.21 USD** | 🔴 **-1.96%** ($-0.79) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $343.91 | $6.93 | 📉 -0.94% | 3d 12h |
| `MSFT` | 0.012263 | $530.04 | $532.60 | $6.53 | 📈 +0.48% | 13h 49m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Wall Street equities (AAPL, MSFT, QQQ, SPY, NVDA, GLD) are currently in CERRADO (closed) market hours with frozen prices. Per operational rules, no equity transactions can occur while markets are closed. In the cryptocurrency sector (ABIERTO 24/7), major assets such as ETH-USD, SOL-USD, and BTC-USD remain under bearish trends below their respective SMA20 lines, accompanied by negative 7-day performance and weak 1-hour momentum, failing to meet our strict trend and reversal confirmation criteria."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): Asset market is closed (CERRADO) and position is adhering to equity patience rules while staying above SMA20.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing equity positions (AAPL and MSFT) during closed market hours. MSFT shows a strong 1h RSI of 80.0 and positive profit, nearing our +3.0% to +5.0% take-profit target window upon market reopening. AAPL is holding steady above its SMA20 despite a temporary dip. Keep crypto sidelined due to active downtrends below SMA20 and lack of confirmed 1h positive momentum triggers. Protect all active positions with strict stop-loss discipline."
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
