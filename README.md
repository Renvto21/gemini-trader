# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-10 17:30:46`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.01 USD** | **$13.54 USD** | **$38.55 USD** | 🔴 **-3.62%** ($-1.45) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $348.70 | $6.56 | 📈 +0.97% | 4d 23h |
| `MSFT` | 0.013089 | $534.82 | $533.22 | $6.98 | 📉 -0.30% | 4d 4h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market continues to exhibit broad weakness, with major equity indices like SPY, QQQ, and NVDA trading in a bearish trend below their respective SMA20 levels. Crypto assets (BTC-USD, ETH-USD, SOL-USD) are also primarily in downtrends, though some show early bounce attempts. Our existing equity holdings, AAPL and MSFT, remain in confirmed uptrends above the SMA20, demonstrating resilience. AAPL is showing positive momentum with a +0.97% PnL, while MSFT is holding steady near breakeven (-0.3%). Adhering strictly to equity holding patience and our rule of never catching falling knives, we will maintain our current positions and hold cash."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in a confirmed uptrend above the SMA20 and showing a positive PnL (+0.97%). Adhering to equity holding patience rules, we maintain the position.
- **[HOLD] MSFT** (Confidence: 85%): MSFT remains above its SMA20 trend line despite minor intraday fluctuations. Patiently holding to let the trade play out within risk parameters.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintained AAPL and MSFT positions following equity holding patience guidelines. Both equities remain above the SMA20 trend line. Will continue to monitor stop-loss levels (-2.0%) and take-profit targets (+3.5% to +5.0%). No new crypto or stock entries made this cycle due to strict trend filters and anti-correlation constraints."
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
