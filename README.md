# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-30 12:30:50`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.23 USD** | **$7.01 USD** | **$39.24 USD** | 🔴 **-1.91%** ($-0.76) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $347.71 | $7.01 | 📈 +0.16% | 6d 22h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market is currently experiencing a strong bearish sweep with almost all tracked equities and cryptocurrencies trading below their SMA20 lines. Assets like MSFT, SPY, QQQ, NVDA, and GLD are deep in daily downtrends with severely depressed 1H RSI readings, marking classic falling knife conditions. AAPL is the sole exception holding firm in an uptrend above its SMA20 (current price $347.71 with a positive 1H change and healthy RSI of 57.1). Cryptocurrencies like BTC-USD and SOL-USD show slight hourly bounces but remain below their respective SMA20 trends, violating our strict trend-following rule."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): AAPL remains in a confirmed uptrend above its SMA20, adhering to our trend filter and equity holding patience guidelines. PnL is currently slightly positive (+0.16%), and we are letting the trade develop towards our +3.0% to +5.0% take-profit target while protecting against the -2.0% circuit breaker.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "We are maintaining our patient equity holding stance on AAPL, which continues to show resilience above its SMA20 with stable performance. Take-profit target remains set between +3.0% and +5.0%, and stop-loss is protected around -1.8% to -2.0%. All other market assets remain in bearish trends below SMA20 or fail confirmation triggers; we will refrain from opening new positions until high-quality uptrend pullback opportunities arise."
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
