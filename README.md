# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-27 11:20:46`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.75 USD** | **$13.44 USD** | **$39.19 USD** | 🔴 **-2.03%** ($-0.81) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $344.46 | $6.95 | 📉 -0.78% | 3d 21h |
| `MSFT` | 0.012263 | $530.04 | $529.47 | $6.49 | 📉 -0.11% | 23h 19m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market continues to show mixed signals, with several major indices and crypto assets remaining in downtrends below their SMA20. AAPL and MSFT are currently held as equity positions in confirmed uptrends. MSFT shows a minor negative 1h change (-0.62%) but remains safely above stop-loss and trend parameters, while AAPL continues steady. Crypto assets remain in bearish trends below the SMA20, prompting us to stay on the sidelines as per our trend filter rules."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): AAPL is in a confirmed uptrend above its SMA20 and holding steady. Sticking to equity holding patience principles, we will let the trade play out toward our +3.0% to +5.0% take-profit target while respecting the stop-loss.
- **[HOLD] MSFT** (Confidence: 100%): MSFT remains in an uptrend above its SMA20 with a minor intraday pullback. Current PnL is well within acceptable limits far above the -1.8% stop-loss threshold. Maintaining position patience.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Hold existing equity positions AAPL and MSFT. Monitor stop-loss levels strictly at -1.8% to -2.0% and take-profit targets between +3.0% and +5.0%. Avoid opening any new positions until clear pullback confirmations with green 1-hour candles appear on uptrend-confirmed assets."
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
