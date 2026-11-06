# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-06 01:00:53`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.14 USD** | **$6.48 USD** | **$38.61 USD** | 🔴 **-3.46%** ($-1.39) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $344.17 | $6.48 | 📉 -0.34% | 7h 20m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader markets are experiencing severe downward pressure, with major equity indices like SPY and QQQ and most major cryptocurrencies in strong bear trends below their SMA20 lines following aggressive tech and crypto sell-offs. Wall Street is currently closed (CERRADO), freezing equity prices. Crypto assets are open 24/7, but they display extremely weak momentum, low 1-hour RSI readings, and negative 1-hour change percentages, failing the reversal trigger criteria. GLD and MSFT remain above their SMA20 lines, but MSFT is closed and GLD has an overbought 1-hour RSI of 89.1 without a valid pullback entry setup. Our current holding, AAPL, is currently closed with a minor unrealized loss of -0.34%, well within acceptable parameters given equity holding patience rules."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): AAPL is currently held in an established position with a minor unrealized loss of -0.34%. Wall Street is closed (CERRADO). Per equity holding patience rules, we do not rotate or sell flat or slightly down equity positions prematurely unless the stop-loss limit (-1.8% to -2.0%) is breached.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain patience with the existing AAPL equity position while Wall Street remains closed. Strictly monitor AAPL for stop-loss triggers at -1.8% to -2.0% and take-profit targets between +3.0% and +5.0%. Avoid all crypto assets as they are in strong downtrends with 1-hour RSI levels well below 32 and negative 1-hour percentage changes. Keep cash reserves above the $4.00 minimum threshold and wait for confirmed uptrend pullbacks with green 1-hour candles before considering new entries."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **89** | 🎯 **42.7%** (38W / 36L / 15BE) | 🔴 **$-1.23 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-05 17:40` | 🟢 BUY | `AAPL` | $6.50 | $345.35 | AAPL is in a confirmed uptrend above its SMA20, market status is open, and 1-hour momentum... |
| `2026-11-05 11:20` | 🔴 SELL (-0.15$) | `ETH-USD` | $6.85 | $2374.60 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -2.10% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-05 01:41` | 🟢 BUY | `ETH-USD` | $7.00 | $2425.59 | ETH-USD is in a confirmed uptrend above its SMA20, market status is open 24/7, 1-hour RSI ... |
| `2026-11-04 22:00` | 🔴 SELL (-0.31$) | `MSFT` | $6.69 | $520.99 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -4.44% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-04 11:30` | 🟢 BUY | `MSFT` | $7.00 | $545.20 | MSFT is currently the only asset trading above its SMA20 in a confirmed uptrend with stron... |

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
