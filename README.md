# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-29 13:21:06`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.23 USD** | **$7.04 USD** | **$39.27 USD** | 🔴 **-1.83%** ($-0.73) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $349.37 | $7.04 | 📈 +0.63% | 5d 23h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market continues to experience a broad corrective phase, with major indices and most equities (QQQ, NVDA, SPY, MSFT, GLD) trading below their SMA20 lines in a bearish trend. Cryptocurrencies are also largely suppressed below their SMA20 lines with high 1-hour RSI levels showing overbought bounces rather than genuine trend continuations. AAPL remains the sole standout in our watchlist holding a confirmed bullish trend above its SMA20 with positive short-term momentum, currently up +0.63% in our portfolio."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is maintaining its uptrend above the SMA20 with positive momentum (+0.13% on the 1-hour candle and +1.61% on the 24-hour). Adhering to our equity holding patience and asymmetric risk/reward rules, we hold the position to let profits run toward our +3% to +5% target without premature rotation.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain the AAPL position patiently in accordance with equity holding rules since it remains firmly in an uptrend above the SMA20. The current profit is +0.63%; we will continue to let winners run toward our target range of +3.0% to +5.0% ($357.50 to $364.50) while keeping our stop-loss at -1.8% ($340.90). No new buys will be executed right now because all other assets on the watchlist violate our strict trend filter (trading below SMA20). Cash reserves remain secure at $32.23."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **86** | 🎯 **44.2%** (38W / 33L / 15BE) | 🔴 **$-0.64 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-28 13:21` | 🔴 SELL (-0.02$) | `MSFT` | $6.48 | $528.16 | MSFT has shifted to a bearish trend below its SMA20 and current performance is near our st... |
| `2026-10-26 12:01` | 🟢 BUY | `MSFT` | $6.50 | $530.04 | MSFT is in a confirmed uptrend above its SMA20, and the 1-hour RSI (62.8) and 1-hour perce... |
| `2026-10-23 13:40` | 🟢 BUY | `AAPL` | $7.00 | $347.17 | AAPL is in a confirmed uptrend above its SMA20, satisfying our strict trend filter. The 1-... |
| `2026-10-22 16:00` | 🔴 SELL (-0.12$) | `MSFT` | $6.88 | $521.40 | MSFT has dropped to a PnL of -1.71%, closely approaching our mandatory stop-loss threshold... |
| `2026-10-22 14:40` | 🔴 SELL (+0.17$) | `AAPL` | $10.17 | $346.52 | AAPL rsi_1h has surpassed 72 (currently 73.4) with a positive return of +1.73%, satisfying... |

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
