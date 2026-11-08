# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-08 09:30:45`

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
| `MSFT` | 0.013089 | $534.82 | $530.61 | $6.94 | 📉 -0.79% | 1d 20h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "All equity markets and traditional assets are currently closed for the weekend with prices frozen, and all monitored assets across both crypto and equities are trading below their respective SMA20 trend filters, signaling a broader market downtrend. Cryptocurrencies like BTC, ETH, and SOL are open 24/7 but lack positive 1-hour momentum confirmation (change_1h_pct is flat or negative), meaning no high-quality pullback or reversal trigger is present. In accordance with strict quantitative trend-following and capital preservation rules, no buying is permitted into downtrends or closed markets. Existing equity positions in AAPL and MSFT must be held patiently through the weekend without panic selling, maintaining strict adherence to the equity holding patience rule."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): Asset is currently in a closed market status and holding period rules dictate patience for equities unless stop-loss is hit. PnL is within acceptable minor drawdown bounds (-0.86%).
- **[HOLD] MSFT** (Confidence: 100%): Market is closed for the weekend and equity holding patience rule applies. Current drawdown is minimal (-0.79%) and well clear of the hard circuit breaker.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Hold existing AAPL and MSFT equity positions through the weekend, monitoring distance to the -2.0% stop-loss threshold. Do not execute any trades in crypto or equities given that all assets remain below the SMA20 trend filter and lack green 1-hour reversal triggers. Wait for Wall Street to reopen next week and watch for confirmed trend breakouts and positive 1-hour momentum before deploying any cash reserves."
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
