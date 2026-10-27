# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-26 22:40:46`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.75 USD** | **$13.47 USD** | **$39.21 USD** | 🔴 **-1.96%** ($-0.79) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $343.91 | $6.93 | 📉 -0.94% | 3d 9h |
| `MSFT` | 0.012263 | $530.04 | $532.60 | $6.53 | 📈 +0.48% | 10h 39m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The portfolio currently holds AAPL and MSFT, both of which are currently in confirmed uptrends (above SMA20). Wall Street and traditional equities are closed (market status CERRADO), meaning prices are frozen and no equity orders can be placed. Cryptocurrencies are open (ABIERTO 24/7), but all major crypto assets (BTC-USD, ETH-USD, SOL-USD) remain in bearish trends below their SMA20 and fail our strict trend filter, keeping us sidelined in crypto per capital preservation rules. AAPL is experiencing a mild pullback with an unrealized PnL of -0.94%, while MSFT shows a slight positive PnL of +0.48%. Both equity positions should be held patiently according to equity holding rules, waiting for market re-opening and profit targets (+3.0% to +5.0%) or stop-loss thresholds (-1.8%)."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): AAPL is in a confirmed uptrend above SMA20. Equity holding patience applies as markets are closed and the position is within normal fluctuation limits.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain current equity positions in AAPL and MSFT. Keep crypto exposure at zero since crypto assets are trading below SMA20 in a downtrend. Monitor MSFT and AAPL closely for upcoming market sessions, ready to take profits if targets (+3.0% to +5.0%) are reached or cut losses strictly if stop-loss (-1.8% to -2.0%) is hit upon market opening."
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
