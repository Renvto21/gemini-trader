# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-08 23:40:41`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.14 USD** | **$13.39 USD** | **$38.53 USD** | 🔴 **-3.69%** ($-1.47) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $342.37 | $6.44 | 📉 -0.86% | 3d 5h |
| `MSFT` | 0.013089 | $534.82 | $530.61 | $6.94 | 📉 -0.79% | 2d 10h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Wall Street markets are currently closed (CERRADO) for the weekend, and all tracked equities (AAPL, MSFT, SPY, QQQ, NVDA, GLD) are showing downward trends below their respective SMA20 lines. Per strict quantitative rules, equities cannot be traded while closed, and holding equity positions through flat or corrective weekend periods is appropriate as long as stop-losses are respected. In the crypto sector (ABIERTO 24/7), assets such as BTC-USD, ETH-USD, and SOL-USD remain in macro downtrends (below SMA20) with mixed short-term recovery indicators. Although BTC and SOL show minor 1-hour positive momentum, their overall trend structure fails the rule of gold (never catch falling knives), and our anti-correlation constraint restricts opening new crypto positions while we focus on capital preservation."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): Traditional markets are closed (CERRADO) and equity holding patience rule applies. The position is experiencing a modest unrealized drawdown (-0.86%), well within the acceptable stop-loss threshold (-1.8% to -2.0%). No action required until market resumption.
- **[HOLD] MSFT** (Confidence: 100%): Traditional markets are closed (CERRADO). The MSFT position is holding steady with an unrealized loss of -0.79%, well above our circuit-breaker stop-loss limits. Maintaining equity holding patience over the weekend.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain patience on existing equity positions AAPL and MSFT over the weekend. Monitor positions closely for any gap-downs upon Monday's market open, keeping stop-loss thresholds strictly between -1.8% and -2.0%. In crypto, refrain from initiating any trades due to prevailing downtrends below SMA20. Wait for confirmed trend reversals above SMA20 across assets before executing new long entries."
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
