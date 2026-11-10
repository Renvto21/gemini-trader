# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-10 16:20:44`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.01 USD** | **$13.55 USD** | **$38.56 USD** | 🔴 **-3.59%** ($-1.44) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $348.39 | $6.56 | 📈 +0.88% | 4d 22h |
| `MSFT` | 0.013089 | $534.82 | $534.33 | $6.99 | 📉 -0.09% | 4d 3h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market reflects mixed conditions with major equity indices like QQQ, SPY, and NVDA trading in confirmed downtrends below their SMA20 lines. Crypto assets (BTC-USD, ETH-USD, SOL-USD) remain under heavy selling pressure and are trading in bear trends with negative 24-hour momentum, failing to trigger our reversal requirements. Conversely, our current equity holdings AAPL and MSFT remain resilient, maintaining their positions above their SMA20 uptrend lines. We continue to prioritize capital preservation by holding existing winning and stable equity positions while waiting for clear, confirmed reversal triggers before deploying new capital."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is trading above its SMA20 in an established uptrend with positive 7-day performance. Adhering to equity holding patience.
- **[HOLD] MSFT** (Confidence: 90%): MSFT maintains its position above the SMA20 uptrend line. No stop-loss or profit target reached, continuing to hold.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintained AAPL and MSFT in accordance with the equity holding patience rule as both continue to trade in healthy uptrends above their SMA20. Monitored crypto and other watchlist assets, but none met the strict quantitative criteria (must be above SMA20, rsi_1h >= 32, and positive 1-hour change). Cash remains secure at $25.01. Will wait for optimal pullback entries in confirmed uptrend assets before taking further actions."
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
