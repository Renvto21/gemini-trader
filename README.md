# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-27 11:10:56`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.75 USD** | **$13.43 USD** | **$39.18 USD** | 🔴 **-2.05%** ($-0.82) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $344.27 | $6.94 | 📉 -0.84% | 3d 21h |
| `MSFT` | 0.012263 | $530.04 | $529.20 | $6.49 | 📉 -0.16% | 23h 9m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market reflects mixed sentiment with several key indices and assets trading below their SMA20, signaling caution. However, our current equity holdings AAPL and MSFT remain in confirmed uptrends above the SMA20. MSFT experienced a slight negative 1-hour change, but its holding time is still short, and equity patience rules dictate holding unless stop-loss thresholds are reached. No new crypto assets meet our strict trend filter criteria as most remain in bearish trends below the SMA20."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 80%): AAPL remains in a confirmed uptrend above the SMA20. PnL is within acceptable limits (-0.84%), and equity holding patience applies.
- **[HOLD] MSFT** (Confidence: 80%): MSFT remains in a confirmed uptrend above the SMA20. PnL is minimal (-0.16%), well above the hard stop-loss threshold of -2.0%.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain current equity positions AAPL and MSFT while respecting stop-loss levels at -1.8% and aiming for take-profit targets between +3.0% and +5.0%. Avoid opening crypto positions due to persistent bearish trends below the SMA20. Continue monitoring for pullback setups with green 1-hour candle confirmations."
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
