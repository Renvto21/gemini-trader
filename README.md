# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-23 16:00:50`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.25 USD** | **$6.99 USD** | **$39.24 USD** | 🔴 **-1.89%** ($-0.76) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $346.88 | $6.99 | 📉 -0.08% | 2h 20m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market remains largely under pressure, with major indices and equities trading below their SMA20 trendlines (such as SPY, QQQ, GLD, MSFT, and NVDA) showing weakness and depressed short-term RSI values. Crypto assets (ETH-USD, BTC-USD, SOL-USD) are also consolidating below their SMA20 filters with slightly negative 1-hour percentage changes, failing to meet our rigorous breakout and reversal triggers. AAPL is the single asset maintaining a confirmed uptrend above its SMA20 with a positive 1-hour return (+0.17%) and an RSI of 62.7, aligning with our trend-following philosophy."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): AAPL is currently in a confirmed uptrend above the SMA20 with a positive 1-hour change of +0.17%. Following equity holding patience, we maintain the position as it has only been held for 2 hours and 20 minutes, awaiting our target gain of +3.0% to +5.0% or an RSI > 72.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL position currently at a negligible PnL of -0.08%. Equity holding patience remains in full effect as AAPL is the only asset respecting our uptrend filter and rules. Take-profit target remains set between +3.0% and +5.0% or when the 1-hour RSI exceeds 72. Stop-loss is firmly monitored at -1.8%. No new trades or rotations will be executed until other assets regain their uptrend or AAPL triggers its profit target."
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
