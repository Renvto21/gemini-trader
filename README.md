# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-11 19:40:42`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$31.84 USD** | **$6.69 USD** | **$38.54 USD** | 🔴 **-3.66%** ($-1.46) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $355.63 | $6.69 | 📈 +2.98% | 6d 1h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Wall Street markets are currently closed (CERRADO) for the weekend/night cycle, meaning all equity and ETF assets like AAPL, SPY, QQQ, and MSFT have frozen prices. Cryptocurrencies remain active 24/7, but all major crypto assets (SOL-USD, ETH-USD, BTC-USD) are currently in a bearish trend below their SMA20, violating our strict trend filter rule. Our sole open position is AAPL, which is in a confirmed uptrend above its SMA20 with a positive PnL of +2.98% and an hourly RSI of 70.4. Since Wall Street is closed and AAPL is approaching our profit target range (+3.0% to +5.0% or hourly RSI > 72), we must patiently hold the position according to equity holding patience rules rather than forcing premature exits or invalid crypto trades."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 95%): AAPL is in a confirmed uptrend above the SMA20, showing a strong +2.98% profit. With Wall Street markets currently closed, equity holding patience rules dictate we maintain the position until it reaches our +3.0% to +5.0% profit target or RSI 1h exceeds 72.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Continue holding AAPL as it remains above its SMA20 and is nearing the profit-taking threshold (+3.0% to +5.0% or RSI 1h > 72). Monitor AAPL closely when Wall Street reopens for potential profit realization. Keep cash reserves protected at $31.84. Do not open any crypto positions since none meet the strict trend filter requirements (all are below SMA20)."
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
