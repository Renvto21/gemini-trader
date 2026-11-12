# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-12 07:20:50`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$31.84 USD** | **$6.69 USD** | **$38.54 USD** | 🔴 **-3.66%** ($-1.46) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $355.63 | $6.69 | 📈 +2.98% | 6d 13h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "All traditional Wall Street equities and ETFs (AAPL, NVDA, GLD, SPY, MSFT, QQQ) are currently closed with frozen prices ('CERRADO'). Per quantitative rules, no buys or sells can be executed on closed assets. Cryptocurrencies (ETH-USD, SOL-USD, BTC-USD) are open 24/7, but all of them remain in a strict bear trend below their respective SMA20 lines with low 1-hour RSI values and no confirmed robust bounce signals, rendering them uninvestable under our trend-following rules. Our single open position, AAPL, is showing healthy performance with a +2.98% PnL, approaching our take-profit threshold (+3.5% to +5.0%) while maintaining adherence to equity holding patience."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is currently showing a solid +2.98% PnL and is approaching our take-profit target range (+3.5% to +5.0%). Because markets are closed ('CERRADO'), equity holding patience applies, and we retain the position until Wall Street reopens.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain the AAPL holding as markets are closed and the position is approaching our +3.5% to +5.0% take-profit target zone (current 1h RSI is 70.4). Monitor AAPL closely when Wall Street reopens for potential take-profit execution if momentum peaks or RSI crosses 72. Keep all crypto assets sidelined since they remain in downtrends below SMA20. Continue respecting stop-loss guidelines (-2.0% circuit breaker) and maintain cash reserves."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **91** | 🎯 **41.8%** (38W / 38L / 15BE) | 🔴 **$-1.52 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-11 12:20` | 🔴 SELL (-0.17$) | `MSFT` | $6.83 | $521.92 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -2.41% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-10 11:31` | 🔴 SELL (-0.12$) | `GLD` | $6.87 | $371.60 | GLD has fallen below its SMA20 trend line and its current PnL is approaching the strict st... |
| `2026-11-09 11:30` | 🟢 BUY | `GLD` | $7.00 | $378.35 | GLD is in a confirmed uptrend above its SMA20, market status is open, 1-hour momentum is s... |
| `2026-11-06 13:10` | 🟢 BUY | `MSFT` | $7.00 | $534.82 | MSFT is in a confirmed uptrend above its SMA20, market status is open, 1-hour RSI has reco... |
| `2026-11-05 17:40` | 🟢 BUY | `AAPL` | $6.50 | $345.35 | AAPL is in a confirmed uptrend above its SMA20, market status is open, and 1-hour momentum... |

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
