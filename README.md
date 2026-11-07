# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-07 06:40:49`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.14 USD** | **$13.39 USD** | **$38.53 USD** | 🔴 **-3.69%** ($-1.47) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $342.37 | $6.44 | 📉 -0.86% | 1d 13h |
| `MSFT` | 0.013089 | $534.82 | $530.61 | $6.94 | 📉 -0.79% | 17h 30m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "All tracked equities (AAPL, MSFT, SPY, QQQ, NVDA, GLD) are currently in CERRADO (closed market) status with prices frozen and trending below their respective SMA20 lines. Cryptocurrencies are open (24/7) but are all exhibiting bearish trends below their SMA20 indicators with negative 1-hour percentage changes, failing the strict trend filter and reversal confirmation triggers. Existing equity holdings AAPL and MSFT remain stable despite minor unrealized losses (-0.86% and -0.79%), well clear of the -1.8% to -2.0% stop-loss threshold. We maintain patience with equity holdings and cash reserves."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): Asset is currently in a closed market status and holding time is within normal equity patience limits. Unrealized loss is -0.86%, remaining well above the -1.8% stop-loss threshold.
- **[HOLD] MSFT** (Confidence: 90%): Asset is currently in a closed market status and holding time is within normal equity patience limits. Unrealized loss is -0.79%, remaining well above the -1.8% stop-loss threshold.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Continue holding AAPL and MSFT during market closure. Monitor positions for potential stop-loss exits near -1.8% to -2.0% or take-profit targets at +3.0% to +5.0% when Wall Street reopens. Do not open new crypto positions as all available options remain below their SMA20 with negative hourly momentum. Keep cash reserves safely above $4.00 USD."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **89** | 🎯 **42.7%** (38W / 36L / 15BE) | 🔴 **$-1.23 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-06 13:10` | 🟢 BUY | `MSFT` | $7.00 | $534.82 | MSFT is in a confirmed uptrend above its SMA20, market status is open, 1-hour RSI has reco... |
| `2026-11-05 17:40` | 🟢 BUY | `AAPL` | $6.50 | $345.35 | AAPL is in a confirmed uptrend above its SMA20, market status is open, and 1-hour momentum... |
| `2026-11-05 11:20` | 🔴 SELL (-0.15$) | `ETH-USD` | $6.85 | $2374.60 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -2.10% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-05 01:41` | 🟢 BUY | `ETH-USD` | $7.00 | $2425.59 | ETH-USD is in a confirmed uptrend above its SMA20, market status is open 24/7, 1-hour RSI ... |
| `2026-11-04 22:00` | 🔴 SELL (-0.31$) | `MSFT` | $6.69 | $520.99 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -4.44% hit safety limit (-2.0%). Liquidated by code... |

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
