# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-05 04:20:41`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$31.78 USD** | **$7.00 USD** | **$38.78 USD** | 🔴 **-3.05%** ($-1.22) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.002886 | $2425.59 | $2424.51 | $7.00 | 📉 -0.04% | 2h 39m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Wall Street traditional markets remain closed, keeping equities and ETFs untradeable. Active 24/7 crypto markets show ETH-USD consolidating just below entry levels with a small unrealized loss (-0.04%). ETH-USD remains in a confirmed daily uptrend above its SMA20 with neutral-to-bullish momentum (daily RSI 54.2), though the 1-hour candle is slightly negative (-0.13%). BTC-USD is also above its SMA20 but does not currently present an active green reversal trigger combined with a pullback. Per anti-correlation rules and capital preservation discipline, we maintain our single crypto position (ETH-USD) and hold cash."

**Cycle Actions:**
- **[HOLD] ETH-USD** (Confidence: 80%): ETH-USD remains in a confirmed uptrend above its SMA20 with healthy fundamentals. It has not triggered either our stop-loss (-2.0%) or take-profit (+3.0% to +5.0%) targets. Maintaining position per equity holding patience and trend-following rules.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding ETH-USD. Maintain strict stop-loss protection between -1.8% and -2.0% ($2377-2380) and target take-profit levels at +3.0% to +5.0% ($2500-2540). Keep cash reserve above $4.00 USD ($31.78 current cash) and wait for Wall Street markets to reopen before evaluating quality equity pulldowns."
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
