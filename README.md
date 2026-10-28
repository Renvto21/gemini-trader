# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-28 13:01:27`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.75 USD** | **$13.43 USD** | **$39.18 USD** | 🔴 **-2.05%** ($-0.82) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $345.26 | $6.96 | 📉 -0.55% | 4d 23h |
| `MSFT` | 0.012263 | $530.04 | $527.55 | $6.47 | 📉 -0.47% | 2d 1h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The market shows mixed conditions with major indices like SPY holding above the SMA20 uptrend filter, while tech giants and crypto remain largely range-bound or in minor downtrends. AAPL remains our solid equity holding above SMA20 with stable technicals. MSFT has dipped slightly below its SMA20 trend line with a negative 1-hour change, requiring close observation to protect against our hard -1.8% to -2.0% stop-loss threshold. Cash reserves remain robust at $25.75 USD, adhering to capital preservation rules."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 80%): AAPL is in a confirmed uptrend above its SMA20 and is exhibiting stable holding behavior. Sticking to equity holding patience guidelines while monitoring for further upside.
- **[HOLD] MSFT** (Confidence: 70%): MSFT current PnL is at -0.47%, well above our hard stop-loss threshold of -2.0%. Holding position patiently per equity holding rules while keeping risk controlled.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain AAPL as our core equity position. Monitor MSFT closely; if its performance nears the -1.8% to -2.0% stop-loss threshold, execute a disciplined sell. For new entries, patiently wait for assets to confirm an uptrend above SMA20 accompanied by a positive 1-hour RSI and green candle confirmation. Keep cash reserves secure."
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
