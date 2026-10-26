# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-25 21:30:49`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.25 USD** | **$7.01 USD** | **$39.26 USD** | 🔴 **-1.85%** ($-0.74) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $347.73 | $7.01 | 📈 +0.16% | 2d 7h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Equity markets remain closed (CERRADO) with prices frozen, leaving AAPL as our sole active holding. AAPL is showing solid resilience with a positive PnL (+0.16%), sitting in a confirmed uptrend above the SMA20 with a 1h RSI at 66.0 and daily RSI at 72.3, approaching our take-profit threshold (+3.0% to +5.0% or 1h RSI > 72). Other major equities are currently in downtrends below their SMA20. Crypto assets are open (24/7), but ETH-USD, SOL-USD, and BTC-USD remain in bearish trends below their SMA20 with negative 24h momentum, failing our strict trend filter and reversal confirmation rules. Therefore, no crypto trades will be executed."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is remaining in a healthy confirmed uptrend above the SMA20 with positive PnL (+0.16%). Equity markets are currently closed (CERRADO), and the asset has not yet reached our take-profit target or breached our stop-loss. Complying with equity holding patience.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Continue holding AAPL in its established uptrend above SMA20. Monitor AAPL closely when equity markets reopen for our take-profit target (+3.0% to +5.0% or 1h RSI > 72) while strictly maintaining our stop-loss at -1.8%. Keep crypto assets sidelined due to persistent bearish macro conditions and trends below SMA20."
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
