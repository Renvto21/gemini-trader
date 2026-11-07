# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-07 06:20:39`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.14 USD** | **$13.39 USD** | **$38.53 USD** | 🔴 **-3.69%** ($-1.47) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $342.37 | $6.44 | 📉 -0.86% | 1d 12h |
| `MSFT` | 0.013089 | $534.82 | $530.61 | $6.94 | 📉 -0.79% | 17h 9m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Wall Street equities (AAPL, MSFT, SPY, QQQ, GLD, NVDA) are currently in weekend closure ('CERRADO'), with prices frozen and trading restricted. Across the board, traditional equities are currently trading below their SMA20 with bearish daily trends, meaning no equity action can be taken per quantitative rules. In the crypto markets ('ABIERTO (24/7)'), BTC-USD, ETH-USD, and SOL-USD all show negative 1-hour changes and do not meet the strict 1-hour reversal bounce criteria ('change_1h_pct' > 0.0), alongside being under their respective SMA20 trends. Given the current portfolio holds AAPL and MSFT safely within acceptable drawdown thresholds (and given rule enforcement for equity holding patience), no trades should be executed this cycle."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): Market is closed ('CERRADO') for AAPL and the position is within normal holding patience parameters (-0.86% PnL). No action required.
- **[HOLD] MSFT** (Confidence: 100%): Market is closed ('CERRADO') for MSFT and the position is within normal holding patience parameters (-0.79% PnL). No action required.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain current AAPL and MSFT equity positions during market closure. Monitor positions closely for stop-loss limits (-1.8% to -2.0%) when Wall Street reopens. Avoid crypto exposure due to negative 1-hour momentum and failing trend filters. Continue holding cash reserves above $4.00 USD."
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
