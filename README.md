# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-11 09:10:44`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.01 USD** | **$13.54 USD** | **$38.55 USD** | 🔴 **-3.63%** ($-1.45) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $348.51 | $6.56 | 📈 +0.92% | 5d 15h |
| `MSFT` | 0.013089 | $534.82 | $533.16 | $6.98 | 📉 -0.31% | 4d 19h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Wall Street equities (AAPL, MSFT, SPY, QQQ, NVDA, GLD) are currently closed for the weekend/pre-market, meaning their prices are frozen and no actions can be taken on them per our operational rules. In the crypto markets, assets like BTC-USD, ETH-USD, and SOL-USD are active (24/7), but all major crypto assets are currently categorized in a bearish trend below their respective SMA20 lines and lack positive 1-hour momentum confirmation triggers (change_1h_pct is negative or flat). Therefore, strict risk management dictates zero crypto exposure. Our current equity positions in AAPL and MSFT remain healthy, holding above their SMA20 trend lines with positive or minimal drawdown well within our strict stop-loss limits. We continue to exercise equity holding patience while maintaining a strong cash buffer."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): AAPL is in a confirmed uptrend above its SMA20 and is performing well with a positive PnL. Adhering to the equity holding patience rule, we will not disturb this profitable position.
- **[HOLD] MSFT** (Confidence: 100%): MSFT remains above its SMA20 trend line with minor drawdown well within our -1.8% to -2.0% stop-loss threshold. We hold patiently awaiting upside target convergence.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing long positions in AAPL and MSFT as they remain safely above their SMA20 trend lines, respecting equity holding patience. Do not touch closed equity markets. For crypto markets, continue to sit on hands and wait for a confirmed daily uptrend and a positive 1-hour reversal trigger (RSI >= 32 and change_1h_pct > 0.0) before deploying any of our $25.01 cash reserve. Keep cash reserve strictly above $4.00."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **90** | 🎯 **42.2%** (38W / 37L / 15BE) | 🔴 **$-1.35 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-10 11:31` | 🔴 SELL (-0.12$) | `GLD` | $6.87 | $371.60 | GLD has fallen below its SMA20 trend line and its current PnL is approaching the strict st... |
| `2026-11-09 11:30` | 🟢 BUY | `GLD` | $7.00 | $378.35 | GLD is in a confirmed uptrend above its SMA20, market status is open, 1-hour momentum is s... |
| `2026-11-06 13:10` | 🟢 BUY | `MSFT` | $7.00 | $534.82 | MSFT is in a confirmed uptrend above its SMA20, market status is open, 1-hour RSI has reco... |
| `2026-11-05 17:40` | 🟢 BUY | `AAPL` | $6.50 | $345.35 | AAPL is in a confirmed uptrend above its SMA20, market status is open, and 1-hour momentum... |
| `2026-11-05 11:20` | 🔴 SELL (-0.15$) | `ETH-USD` | $6.85 | $2374.60 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -2.10% hit safety limit (-2.0%). Liquidated by code... |

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
