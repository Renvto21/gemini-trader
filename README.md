# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-10 12:40:49`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.01 USD** | **$13.66 USD** | **$38.67 USD** | 🔴 **-3.33%** ($-1.33) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $348.30 | $6.56 | 📈 +0.85% | 4d 19h |
| `MSFT` | 0.013089 | $534.82 | $542.65 | $7.10 | 📈 +1.46% | 3d 23h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader equity and crypto markets exhibit weakness following hotter-than-expected CPI inflation data, leading to a general pullback. Major index ETFs like SPY and QQQ, alongside crypto assets (BTC, ETH, SOL) and tech leaders like NVDA, are trading in a downtrend below their SMA20 with low 1-hour RSI readings, signaling extreme caution. However, our current positions in AAPL and MSFT remain resilient, maintaining an uptrend above their SMA20 lines with positive performance (+0.85% and +1.46% respectively). In accordance with our equity holding patience and strict trend rules, we will hold these positions and maintain our healthy cash reserves."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL remains in a confirmed uptrend above the SMA20 with positive PnL. Adhering to the equity holding patience rule, we continue to let the winner run.
- **[HOLD] MSFT** (Confidence: 90%): MSFT is holding above its SMA20 in a stable uptrend with positive performance. No rotation or sale is warranted.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL and MSFT in confirmed uptrends above the SMA20. Avoid all crypto assets and downtrending equities due to bearish macro momentum following the hot CPI print. Keep cash reserves intact above $4.00 USD and wait for a clear trend reversal or confirmed pullback with 1-hour green momentum before deploying capital into new assets."
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
