# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-25 14:40:40`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.25 USD** | **$7.01 USD** | **$39.26 USD** | 🔴 **-1.85%** ($-0.74) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $347.73 | $7.01 | 📈 +0.16% | 2d 0h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The majority of traditional equity and crypto markets remain in a cautious state, with major indices like SPY, QQQ, and most crypto assets under their SMA20 trend filters. AAPL is currently holding steady above its SMA20 in an uptrend with a daily RSI at 72.3 and 1h RSI at 66.0, currently showing a mild positive PnL. However, because AAPL and all other tracked US equities have their market status as closed ('CERRADO'), no buy or sell transactions can be executed on equities during this cycle. Crypto assets are open (24/7), but none currently meet our strict trend filter criteria as they are all trading below their SMA20 with negative or weak momentum, violating our rule against catching falling knives."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is in an established uptrend above its SMA20 and is currently exhibiting stable price action with a positive return. Since the market status is closed ('CERRADO'), no execution is possible; we adhere to equity holding patience and await market reopening.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Continue holding AAPL as it remains above its SMA20 in an established uptrend, patiently respecting equity holding guidelines. Monitor AAPL closely upon the reopening of Wall Street for a take-profit trigger if its 1-hour RSI surpasses 72 or if total profit reaches the +3.0% to +5.0% target band, while maintaining a strict stop-loss at -1.8%. Keep crypto assets sidelined due to bearish trends below the SMA20."
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
