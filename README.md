# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-09 17:20:45`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.14 USD** | **$20.80 USD** | **$38.93 USD** | 🔴 **-2.67%** ($-1.07) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $351.09 | $6.61 | 📈 +1.66% | 3d 23h |
| `MSFT` | 0.013089 | $534.82 | $547.41 | $7.16 | 📈 +2.35% | 3d 4h |
| `GLD` | 0.018501 | $378.35 | $379.63 | $7.02 | 📈 +0.34% | 5h 49m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Equities like MSFT (+2.35%), AAPL (+1.66%), and GLD (+0.34%) are performing steadily in confirmed uptrends above their SMA20s, with MSFT and AAPL approaching our profit target range (+3.0% to +5.0%). Cryptocurrencies and indices such as SPY, QQQ, and NVDA remain in downtrends below their SMA20 lines, enforcing strict adherence to our trend-following filter to avoid falling knives. We continue to hold our three equity positions with discipline and patience."

**Cycle Actions:**
- *No changes this cycle (HOLD)*

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain current equity holdings (AAPL, MSFT, GLD) as they respect holding patience and trend-following rules. Monitor MSFT and AAPL for profit-taking if they reach the +3.0% to +5.0% target or if 1-hour RSI pushes past 72. Keep strict -2.0% stop-losses active. Continue avoiding crypto and downtrended indices."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **89** | 🎯 **42.7%** (38W / 36L / 15BE) | 🔴 **$-1.23 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-09 11:30` | 🟢 BUY | `GLD` | $7.00 | $378.35 | GLD is in a confirmed uptrend above its SMA20, market status is open, 1-hour momentum is s... |
| `2026-11-06 13:10` | 🟢 BUY | `MSFT` | $7.00 | $534.82 | MSFT is in a confirmed uptrend above its SMA20, market status is open, 1-hour RSI has reco... |
| `2026-11-05 17:40` | 🟢 BUY | `AAPL` | $6.50 | $345.35 | AAPL is in a confirmed uptrend above its SMA20, market status is open, and 1-hour momentum... |
| `2026-11-05 11:20` | 🔴 SELL (-0.15$) | `ETH-USD` | $6.85 | $2374.60 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -2.10% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-05 01:41` | 🟢 BUY | `ETH-USD` | $7.00 | $2425.59 | ETH-USD is in a confirmed uptrend above its SMA20, market status is open 24/7, 1-hour RSI ... |

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
