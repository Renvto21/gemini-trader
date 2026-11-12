# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-11 22:10:50`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$31.84 USD** | **$6.56 USD** | **$38.40 USD** | 🔴 **-3.99%** ($-1.60) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $348.51 | $6.56 | 📈 +0.92% | 6d 4h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "All traditional Wall Street equities and ETFs (AAPL, GLD, SPY, NVDA, MSFT, QQQ) are currently in 'CERRADO' (closed market) status with frozen prices, preventing execution. AAPL remains our sole active holding, maintaining a positive PnL (+0.92%) above its SMA20 uptrend line with an hourly RSI near 70.4. Cryptocurrencies (BTC-USD, ETH-USD, SOL-USD) are trading 24/7 but are all currently classified in a 'BAJISTA' (bearish) trend below their respective SMA20 lines with negative or neutral 1-hour momentum, failing our strict quantitative trend-following filters."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is in a confirmed uptrend above the SMA20 and currently showing a positive PnL (+0.92%). Since the market is closed, we hold the position patiently and await Wall Street reopening to target our +3.5% to +5.0% profit objective.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain the existing AAPL position during closed market hours as it preserves its UPTREND status above the SMA20. Prepare to execute a profit-taking exit once Wall Street reopens if AAPL reaches the +3.5% to +5.0% target zone or if the 1-hour RSI crosses above 72. Keep all crypto assets sidelined since none satisfy the trend filter requirement above the SMA20. Ensure cash reserves remain strictly above $4.00."
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
