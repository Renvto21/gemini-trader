# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-12 00:30:48`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$31.84 USD** | **$6.69 USD** | **$38.54 USD** | 🔴 **-3.66%** ($-1.46) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $355.63 | $6.69 | 📈 +2.98% | 6d 6h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The traditional stock market is currently closed (market status CERRADO), meaning assets like AAPL are frozen in price. AAPL remains our sole active equity position, showing solid performance with a +2.98% PnL, trading in an uptrend above its SMA20 with a 1-hour RSI near 70.4. In the crypto markets, which are open 24/7, assets such as BTC-USD and SOL-USD continue to show bearish trends below their respective SMA20 lines, failing to meet our strict quantitative filters for a pullback entry. Therefore, we preserve capital and hold our current equity position."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in a confirmed uptrend above SMA20 with a healthy profit of +2.98%. Per equity holding patience rules, stocks should not be rotated or sold prematurely unless stop-loss is hit or take-profit targets (+3% to +5%) are achieved. Wall Street is currently closed.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Hold AAPL position as markets are closed and the asset remains in a confirmed uptrend above SMA20. Monitor AAPL upon market reopening to secure profits once the +3.0% to +5.0% target zone is reached or if rsi_1h surpasses 72. Keep all crypto assets sidelined due to persistent downtrends below SMA20. Maintain cash reserve discipline above $4.00."
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
