# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-06 06:30:47`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.14 USD** | **$6.48 USD** | **$38.61 USD** | 🔴 **-3.46%** ($-1.39) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $344.17 | $6.48 | 📉 -0.34% | 12h 50m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader macroeconomic sentiment is currently cautious and risk-off following sharp declines across major stock indices like QQQ, NVDA, and SPY. Most equity markets and traditional assets are currently closed (CERRADO), leaving prices frozen. Among open crypto assets, Bitcoin, Ethereum, and Solana remain under their respective SMA20 trends, confirming a broader crypto downtrend and discouraging aggressive buying per strict quantitative rules. Within the portfolio, AAPL is held as an active equity position above its SMA20; although it experienced slight downward drift, rules dictate equity patience over 24-48 hour holding windows unless stop-losses are triggered. GLD and MSFT show bullish trends on the daily/SMA20 check, but their market status is closed. We maintain capital preservation by preserving a healthy cash reserve."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is currently in a confirmed uptrend above its SMA20, and per equity holding patience rules, stocks should not be rotated or sold prematurely for flat performance over short horizons. The position is stable and within risk limits.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain current AAPL equity position as it remains above its SMA20 trend and well within the acceptable stop-loss boundary (-0.34% current PnL). Do not panic sell equities during flat or minor negative hourly movements. Keep all crypto assets sidelined until confirmed uptrends above SMA20 and positive hourly momentum triggers appear together. Maintain cash above the $4.00 USD minimum threshold and wait for market reopening to evaluate MSFT and GLD pullbacks."
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
