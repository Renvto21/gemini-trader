# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-12 07:50:48`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$31.84 USD** | **$6.69 USD** | **$38.54 USD** | 🔴 **-3.66%** ($-1.46) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $355.63 | $6.69 | 📈 +2.98% | 6d 14h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market shows major indices and equities under downward pressure with most tracked assets trading below their SMA20, signaling a prevailing bearish trend. Wall Street is currently closed (market status CERRADO), freezing equity prices. AAPL remains our sole active position, currently showing a solid unrealized profit of +2.98% while maintaining an uptrend above its SMA20 and an elevated 1H RSI near 70.4. Cryptocurrencies are open 24/7 but continue to trade in bearish trends below their SMA20 lines with weak momentum, failing to meet our strict pullback entry criteria (rsi_1h >= 32 and change_1h_pct > 0.0), keeping us sidelined on crypto assets to avoid falling knives."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is maintaining a strong uptrend above its SMA20 with a +2.98% unrealized gain. Sticking to equity holding patience principles, we will not sell prematurely and will hold until the take-profit target (+3.5% to +5.0% or RSI > 72) is achieved.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Continue holding AAPL patiently according to equity holding rules, targeting a take-profit gain between +3.5% and +5.0% or an exit if rsi_1h exceeds 72. Keep crypto assets completely sidelined as they are in downtrends below SMA20 with negative 1-hour momentum. Maintain strict stop-loss rules for all open and future positions and preserve our cash reserve above the $4.00 minimum."
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
