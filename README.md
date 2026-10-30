# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-30 13:30:50`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.23 USD** | **$7.00 USD** | **$39.23 USD** | 🔴 **-1.93%** ($-0.77) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $347.27 | $7.00 | 📈 +0.03% | 6d 23h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market is currently experiencing significant downward pressure, with nearly all major equities, indices, and crypto assets trading below their 20-period simple moving averages (SMA20) and registering bearish daily trends. AAPL remains our sole holding positioned above its SMA20 in a confirmed uptrend, displaying resilience despite a slight negative hourly tick (-0.07%). Market-wide indicators reflect oversold daily conditions across SPY, QQQ, NVDA, and GLD, but our strict quantitative rules forbid catching falling knives or buying assets below the SMA20. Cryptocurrencies like ETH-USD and SOL-USD show minor hourly green candles, but neither exhibits a sufficiently strong setup or meets all stringent reversal criteria while maintaining our anti-correlation constraint and cash preservation mandates."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is maintaining its position above the SMA20 in a confirmed uptrend. In accordance with the equity holding patience rule, we give the stock time to play out without rotating or selling prematurely, keeping our stop-loss and take-profit targets active.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "We continue to hold AAPL patiently under the equity holding patience rule, maintaining our stop-loss at -1.8% to -2.0% ($340.00) and take-profit targets between +3.0% and +5.0% ($357.00 - $364.00). Cash reserves remain healthy at $32.23 USD. Given that almost the entire market is currently trading in a bearish trend below the SMA20, we will maintain a defensive posture, avoid new long entries until market breadth and confirmed uptrends return, and monitor AAPL closely for potential profit-taking or trend continuation."
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
