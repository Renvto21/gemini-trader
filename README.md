# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-06 11:40:42`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.14 USD** | **$6.38 USD** | **$38.52 USD** | 🔴 **-3.70%** ($-1.48) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $339.23 | $6.38 | 📉 -1.77% | 17h 59m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market remains largely under pressure with most major indices and stocks trading below their SMA20 trend lines following recent macroeconomic volatility and jobs data. However, MSFT maintains a confirmed bullish trend above its SMA20 while showing a temporary 1-hour pullback. Our current equity holding AAPL is slightly down (-1.77%), remaining well within our strict stop-loss threshold (-2.0%). Adhering strictly to equity holding patience rules, we maintain our position in AAPL and hold our cash reserves."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is currently holding steady with a minor unrealized loss of -1.77%, safely above our hard circuit breaker stop-loss threshold of -2.0%. Per equity holding patience guidelines, we do not rotate or sell an equity position simply for being flat or slightly down over a short timeframe.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL position while closely monitoring the -2.0% stop-loss threshold. MSFT is showing a confirmed uptrend above its SMA20, but we wait for its 1-hour momentum to turn positive (change_1h_pct > 0.0 and rsi_1h >= 32) before considering an entry. Maintain cash reserves above $4.00 USD and enforce strict capital preservation."
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
