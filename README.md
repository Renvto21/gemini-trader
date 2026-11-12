# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-12 08:40:39`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$31.84 USD** | **$6.69 USD** | **$38.54 USD** | 🔴 **-3.66%** ($-1.46) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $355.63 | $6.69 | 📈 +2.98% | 6d 14h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Wall Street equities and commodities (AAPL, QQQ, SPY, NVDA, MSFT, GLD) are currently closed for the weekend/off-hours, showing frozen prices and mixed conditions. AAPL remains our sole open equity holding, comfortably above its SMA20 trend line with a solid 2.98% PnL and nearing take-profit territory. Cryptocurrencies (BTC-USD, ETH-USD, SOL-USD) are open 24/7, but all remain trapped in strict bearish trends below their respective SMA20 lines, accompanied by negative 1-hour changes and low RSI readings. Per strict quantitative rules, we must avoid catching falling knives in crypto and wait for confirmed uptrends and green 1-hour candle reversals. Therefore, no new crypto trades are warranted, and closed equities must remain undisturbed."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is in a confirmed uptrend above its SMA20 with solid positive performance (+2.98% PnL). Following the equity holding patience rule and asymmetric risk/reward guidelines, we will hold the position rather than rotating prematurely, keeping an eye on the +3.5% to +5.0% take-profit target.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Continue holding AAPL patiently above the SMA20 trend line, monitoring for potential take-profit triggers if the 1-hour RSI exceeds 72 or price reaches the +3.5% to +5.0% target. Keep all crypto assets sidelined as they remain in bear trends below SMA20 without green 1-hour candle confirmation. Ensure cash reserves remain well above the $4.00 USD minimum threshold."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **91** | 🎯 **41.8%** (38W / 38L / 15BE) | 🔴 **$-1.52 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-11 12:20` | 🔴 SELL (-0.17$) | `MSFT` | $6.83 | $521.92 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -2.41% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-10 11:31` | 🔴 SELL (-0.12$) | `GLD` | $6.87 | $371.60 | GLD has fallen below its SMA20 trend line and its current PnL is approaching the strict st... |
| `2026-11-09 11:30` | 🟢 BUY | `GLD` | $7.00 | $378.35 | GLD is in a confirmed uptrend above its SMA20, market status is open, 1-hour momentum is s... |
| `2026-11-06 13:10` | 🟢 BUY | `MSFT` | $7.00 | $534.82 | MSFT is in a confirmed uptrend above its SMA20, market status is open, 1-hour RSI has reco... |
| `2026-11-05 17:40` | 🟢 BUY | `AAPL` | $6.50 | $345.35 | AAPL is in a confirmed uptrend above its SMA20, market status is open, and 1-hour momentum... |

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
