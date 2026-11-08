# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-08 08:50:43`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.14 USD** | **$13.39 USD** | **$38.53 USD** | 🔴 **-3.69%** ($-1.47) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $342.37 | $6.44 | 📉 -0.86% | 2d 15h |
| `MSFT` | 0.013089 | $534.82 | $530.61 | $6.94 | 📉 -0.79% | 1d 19h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Traditional equity markets are currently closed (CERRADO) for the weekend, and all major assets (AAPL, MSFT, SPY, QQQ, NVDA) are currently trading below their respective SMA20 trend lines, reflecting a broader macro correction. In the crypto markets (ABIERTO 24/7), assets such as SOL-USD, ETH-USD, and BTC-USD show positive 1-hour momentum, but all remain classified under a bearish trend filter (below SMA20). Adhering strictly to our trend-following and risk-management principles, we must avoid catching falling knives or initiating new long crypto positions below the SMA20. Existing equity holdings (AAPL and MSFT) are currently experiencing minor unrealized drawdowns (-0.86% and -0.79% respectively), well above our hard stop-loss circuit breaker of -2.0%. Given the equity holding patience rule, we will maintain these positions through the weekend."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): Holding current position in accordance with equity holding patience. The drawdown (-0.86%) is well within safe thresholds and far above the -2.0% stop-loss circuit breaker. Market is closed.
- **[HOLD] MSFT** (Confidence: 90%): Holding current position in accordance with equity holding patience. The drawdown (-0.79%) is well within safe thresholds and far above the -2.0% stop-loss circuit breaker. Market is closed.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain current equity positions in AAPL and MSFT while respecting the strict -2.0% stop-loss boundary. Wall Street is closed, so no stock actions can be taken. Although crypto assets show positive hourly momentum, all remain below the SMA20 trend filter; therefore, no crypto positions will be opened to avoid counter-trend risks. Wait for markets to reopen and for assets to reclaim the SMA20 with confirmed breakout momentum before deploying additional capital."
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
