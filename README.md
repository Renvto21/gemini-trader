# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-05 01:41:00`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$31.78 USD** | **$7.00 USD** | **$38.78 USD** | 🔴 **-3.04%** ($-1.22) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.002886 | $2425.59 | $2425.59 | $7.00 | 📈 +0.00% | 0m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Wall Street equities (AAPL, MSFT, NVDA, QQQ, SPY, GLD) are currently closed (CERRADO), leaving active liquidity strictly confined to the 24/7 cryptocurrency markets. Among crypto assets, ETH-USD and BTC-USD are trading in confirmed uptrends above their SMA20. ETH-USD satisfies all quantitative filters: it is in an uptrend, market status is open, 1-hour RSI is 66.3 (above the 32 threshold), and change_1h_pct is positive at +0.14%, confirming a steady bounce. BTC-USD also exhibits positive momentum (+0.08%, RSI 70.6). Given the anti-correlation rule restricting holdings to a single crypto position, ETH-USD represents a high-quality asymmetric opportunity."

**Cycle Actions:**
- **[BUY] ETH-USD** (Confidence: 85%): ETH-USD is in a confirmed uptrend above its SMA20, market status is open 24/7, 1-hour RSI is healthy at 66.3 (>= 32), and the 1-hour candle has turned green with change_1h_pct at +0.14%. This fulfills all quantitative entry rules for a pullback/bounce entry.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Successfully executing a $7.00 buy order on ETH-USD following confirmation of positive 1-hour momentum while above the SMA20. Will monitor for asymmetric upside targeting a +3.5% to +5.0% gain while strictly enforcing a hard stop-loss circuit breaker at -2.0% to protect capital."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **88** | 🎯 **43.2%** (38W / 35L / 15BE) | 🔴 **$-1.08 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-05 01:41` | 🟢 BUY | `ETH-USD` | $7.00 | $2425.59 | ETH-USD is in a confirmed uptrend above its SMA20, market status is open 24/7, 1-hour RSI ... |
| `2026-11-04 22:00` | 🔴 SELL (-0.31$) | `MSFT` | $6.69 | $520.99 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -4.44% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-04 11:30` | 🟢 BUY | `MSFT` | $7.00 | $545.20 | MSFT is currently the only asset trading above its SMA20 in a confirmed uptrend with stron... |
| `2026-11-02 11:40` | 🔴 SELL (-0.13$) | `AAPL` | $6.87 | $340.69 | AAPL has slipped further into a bearish trend below its SMA20 with a 1-hour RSI of 24.8 an... |
| `2026-10-28 13:21` | 🔴 SELL (-0.02$) | `MSFT` | $6.48 | $528.16 | MSFT has shifted to a bearish trend below its SMA20 and current performance is near our st... |

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
