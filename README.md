# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-23 22:00:45`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.25 USD** | **$7.02 USD** | **$39.27 USD** | 🔴 **-1.83%** ($-0.73) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $348.22 | $7.02 | 📈 +0.30% | 8h 19m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market is characterized by defensive conditions with major equities and crypto assets largely under their respective SMA20 trends. AAPL is the sole asset maintaining a confirmed structural uptrend above its SMA20, currently showing a modest positive return (+0.3%) with a 1-hour RSI of 66.0. Most other assets are closed or experiencing bearish trends with RSI levels below or near reversal thresholds. Bitcoin and Ethereum are open 24/7 but remain in downtrends below their SMA20, failing our strict trend filter criteria for new long positions."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is currently in a confirmed uptrend above its SMA20 with a positive return of +0.3% and a healthy RSI_1h of 66.0. Sticking to our equity holding patience and asymmetric risk/reward plan, we will hold the position until our take-profit target (+3.0% to +5.0% or RSI_1h > 72) is reached or the stop-loss is triggered.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Continue holding AAPL as it maintains its structural uptrend above the SMA20. Monitor closely for our take-profit objective of +3.0% to +5.0% or an RSI_1h > 72, while respecting our strict stop-loss threshold at -1.8% to -2.0%. Keep all other assets sidelined until markets reopen and confirm valid trend reversals with positive momentum."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **85** | 🎯 **44.7%** (38W / 32L / 15BE) | 🔴 **$-0.62 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-23 13:40` | 🟢 BUY | `AAPL` | $7.00 | $347.17 | AAPL is in a confirmed uptrend above its SMA20, satisfying our strict trend filter. The 1-... |
| `2026-10-22 16:00` | 🔴 SELL (-0.12$) | `MSFT` | $6.88 | $521.40 | MSFT has dropped to a PnL of -1.71%, closely approaching our mandatory stop-loss threshold... |
| `2026-10-22 14:40` | 🔴 SELL (+0.17$) | `AAPL` | $10.17 | $346.52 | AAPL rsi_1h has surpassed 72 (currently 73.4) with a positive return of +1.73%, satisfying... |
| `2026-10-21 12:01` | 🟢 BUY | `MSFT` | $7.00 | $530.45 | MSFT is in a confirmed uptrend above its SMA20. The 1-hour RSI is at 36.7 (above the 32 th... |
| `2026-10-21 10:10` | 🔴 SELL (+0.12$) | `ETH-USD` | $10.07 | $2481.87 | ETH-USD rsi_1h has surpassed 72 (currently 73.7) with a positive return of +1.21%, satisfy... |

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
