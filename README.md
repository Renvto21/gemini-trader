# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-26 11:51:13`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.25 USD** | **$6.99 USD** | **$39.23 USD** | 🔴 **-1.91%** ($-0.77) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $346.49 | $6.99 | 📉 -0.20% | 2d 22h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market presents a mixed environment with several key equities and all major cryptocurrencies trading below their respective SMA20 trend filters, signaling caution. However, AAPL remains in a confirmed uptrend above its SMA20 with stable price action, currently holding a minor negative PnL of -0.2%. MSFT is also in an uptrend (above SMA20) with positive short-term momentum, though no open position is currently held in it. Cryptocurrencies are trading in a downtrend, preventing any crypto entries under our strict trend rules. Wall Street assets are open, allowing active management of our equity holding."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 80%): AAPL is currently in a confirmed uptrend (above SMA20) and our equity holding patience rule dictates that we give stocks time to play out rather than rotating prematurely on minor fluctuations (-0.2% PnL). It has not hit our stop-loss limit nor reached the take-profit target.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain our current AAPL position respecting equity holding patience, as flat or slightly negative short-term moves in equities do not invalidate the uptrend. Monitor AAPL for a continuation toward take-profit targets (+3% to +5% or RSI 1h > 72 with profit >= +2.5%) while respecting the hard stop-loss threshold at -1.8%. Watch MSFT for a potential pullback entry if it confirms a bounce with 1h RSI >= 32 and positive 1-hour change while staying above SMA20. Keep cash reserves well above the $4.00 minimum."
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
