# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-06 07:20:45`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.14 USD** | **$6.48 USD** | **$38.61 USD** | 🔴 **-3.46%** ($-1.39) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $344.17 | $6.48 | 📉 -0.34% | 13h 40m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Wall Street markets remain closed (CERRADO) following a broad tech and equity sell-off. Major indices and equities like NVDA, SPY, and QQQ are currently in a downtrend below their SMA20. AAPL and MSFT remain in a confirmed uptrend above the SMA20, though prices are frozen due to market hours. Cryptocurrencies are trading 24/7, but all major crypto assets (BTC-USD, ETH-USD, SOL-USD) are currently in a downtrend (below SMA20), meaning no crypto meets our strict trend-following pullback rules. Our sole open position is AAPL, which is performing stably during market closure and should be held patiently following our equity holding rules."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is in a confirmed uptrend above its SMA20 and is currently closed. Adhering to the equity holding patience rule, we will hold the position rather than rotating or selling prematurely.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain the AAPL position through the market closure, respecting equity holding patience and its status above the SMA20 trend line. Keep cash reserves secure ($32.14). Avoid all crypto assets and downtrended equities (like NVDA, SPY, QQQ) until they reclaim SMA20 and exhibit confirmed positive hourly momentum upon market re-opening. Continue to monitor MSFT and GLD for potential pullback entries once Wall Street reopens, ensuring all reversal triggers (rsi_1h >= 32 and change_1h_pct > 0.0) are met."
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
