# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-28 13:11:01`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.75 USD** | **$13.44 USD** | **$39.19 USD** | 🔴 **-2.02%** ($-0.81) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $345.68 | $6.97 | 📉 -0.43% | 4d 23h |
| `MSFT` | 0.012263 | $530.04 | $527.76 | $6.47 | 📉 -0.43% | 2d 1h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market is exhibiting mixed signals with most assets currently trading below their SMA20 trend lines, classified as bearish short-term conditions. AAPL and SPY remain bright spots holding above their SMA20 uptrend filters. MSFT has dipped slightly below its SMA20 line, turning its trend bearish, and requires close monitoring against our strict stop-loss rules. Crypto assets (BTC-USD, ETH-USD, SOL-USD) are in a downtrend without confirmed reversal triggers, remaining on the sidelines per our strict pullback and anti-correlation constraints."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in a confirmed uptrend above its SMA20 and is performing well. Following equity holding patience guidelines, we maintain the position to let it run toward our target profit of +3.0% to +5.0%.
- **[HOLD] MSFT** (Confidence: 80%): MSFT has slipped slightly below SMA20 (-0.43% PnL), but per equity holding patience rules for stocks, we give it time to recover unless it hits our mandatory stop-loss threshold of -1.8% to -2.0%.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Hold current positions in AAPL following equity holding patience rules. Monitor MSFT closely; if its performance hits our stop-loss threshold around -1.8% to -2.0%, execute a disciplined sell immediately. For new entries, wait for assets to confirm an uptrend above SMA20 accompanied by positive 1-hour momentum and green candle confirmation. Keep cash reserves secure at or above $4.00 USD."
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
