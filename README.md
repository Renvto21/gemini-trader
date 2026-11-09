# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-09 04:20:39`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.14 USD** | **$13.39 USD** | **$38.53 USD** | 🔴 **-3.69%** ($-1.47) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $342.37 | $6.44 | 📉 -0.86% | 3d 10h |
| `MSFT` | 0.013089 | $534.82 | $530.61 | $6.94 | 📉 -0.79% | 2d 15h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "All equity markets and gold are currently closed for the weekend, showing frozen prices with negative short-term momentum and most tickers sitting below their respective SMA20 trends. Cryptocurrencies are open 24/7, but they also exhibit bearish trends below their SMA20 levels with negative 1-hour momentum, failing to trigger our strict reversal criteria (rsi_1h >= 32 and change_1h_pct > 0). Our current equity holdings in AAPL and MSFT are experiencing minor unrealized drawdowns (-0.86% and -0.79% respectively) but remain well within our safety threshold above the -2.0% stop-loss limit. Following the equity holding patience rule, we will maintain our positions and wait for the market open to re-evaluate."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): Holding AAPL in accordance with equity holding patience rules. The asset is closed for the weekend and current drawdown (-0.86%) is well above the strict -2.0% stop-loss threshold.
- **[HOLD] MSFT** (Confidence: 100%): Holding MSFT in accordance with equity holding patience rules. The market is closed and current drawdown (-0.79%) is well above the strict -2.0% stop-loss threshold.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Hold current positions in AAPL and MSFT over the weekend. Monitor equity open closely on Monday morning to ensure stop-loss limits (-2.0%) are respected. Avoid entering any new crypto positions due to prevailing downtrends and lack of reversal confirmation. Keep cash reserves secure at $25.14 USD."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **89** | 🎯 **42.7%** (38W / 36L / 15BE) | 🔴 **$-1.23 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-06 13:10` | 🟢 BUY | `MSFT` | $7.00 | $534.82 | MSFT is in a confirmed uptrend above its SMA20, market status is open, 1-hour RSI has reco... |
| `2026-11-05 17:40` | 🟢 BUY | `AAPL` | $6.50 | $345.35 | AAPL is in a confirmed uptrend above its SMA20, market status is open, and 1-hour momentum... |
| `2026-11-05 11:20` | 🔴 SELL (-0.15$) | `ETH-USD` | $6.85 | $2374.60 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -2.10% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-05 01:41` | 🟢 BUY | `ETH-USD` | $7.00 | $2425.59 | ETH-USD is in a confirmed uptrend above its SMA20, market status is open 24/7, 1-hour RSI ... |
| `2026-11-04 22:00` | 🔴 SELL (-0.31$) | `MSFT` | $6.69 | $520.99 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -4.44% hit safety limit (-2.0%). Liquidated by code... |

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
