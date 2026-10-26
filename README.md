# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-26 14:21:07`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.75 USD** | **$13.44 USD** | **$39.19 USD** | 🔴 **-2.02%** ($-0.81) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $343.97 | $6.94 | 📉 -0.92% | 3d 0h |
| `MSFT` | 0.012263 | $530.04 | $530.59 | $6.51 | 📈 +0.10% | 2h 19m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Major equity indices like QQQ, SPY, and NVDA are currently trading below their SMA20, indicating broader market weakness or corrective phases despite minor intraday green candles. Among our holdings, AAPL and MSFT remain the only two assets confirmed in an uptrend above their SMA20. AAPL is experiencing a mild pullback (-0.92% PnL) with a 1-hour change currently negative (-0.21%), so we continue to hold patiently according to equity holding patience rules. MSFT is holding steady above its entry price with a positive 1-hour change (+0.03%) and strong 1-hour RSI (69.2). Crypto assets remain in downtrends below their SMA20, prompting us to maintain a zero-crypto posture to adhere to strict trend filters and anti-correlation constraints."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in a confirmed uptrend above the SMA20. Although down slightly (-0.92%), equity holding patience rules dictate we do not panic-sell flat or slightly negative positions that have not breached the stop-loss threshold (-1.8% to -2.0%).
- **[HOLD] MSFT** (Confidence: 90%): MSFT remains above its SMA20 in a confirmed uptrend with positive momentum. We hold to let winners run toward our +3.0% to +5.0% take-profit target.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain current equity positions in AAPL and MSFT as they are the sole assets above the SMA20. Monitor MSFT for potential take-profit targets approaching +3.0% to +5.0% and AAPL for a rebound confirmation as its 1-hour change turns positive. Keep cash reserves secure above $4.00 USD and avoid crypto markets until a clear bullish reversal above the SMA20 occurs."
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
