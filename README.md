# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-09 11:30:52`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.14 USD** | **$20.63 USD** | **$38.76 USD** | 🔴 **-3.09%** ($-1.24) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $345.18 | $6.50 | 📉 -0.05% | 3d 17h |
| `MSFT` | 0.013089 | $534.82 | $544.84 | $7.13 | 📈 +1.87% | 2d 22h |
| `GLD` | 0.018501 | $378.35 | $378.35 | $7.00 | 📈 +0.00% | 0m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Equities show a mixed recovery context with strong large-cap tech leadership holding above their SMA20 (e.g., MSFT and AAPL), while broad indices like SPY and QQQ remain under pressure below their respective SMA20 lines. GLD continues to perform well as a defensive safe-haven asset in a confirmed uptrend. Crypto markets (BTC, ETH, SOL) are showing weak downside momentum and remain trapped in bear trends below the SMA20, prompting zero exposure per our strict quantitative trend filters."

**Cycle Actions:**
- **[BUY] GLD** (Confidence: 85%): GLD is in a confirmed uptrend above its SMA20, market status is open, 1-hour momentum is strongly positive (+1.56%), and 1-hour RSI is at 58.0, satisfying all pullback and reversal entry criteria.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Current holdings AAPL and MSFT remain stable above SMA20 with MSFT showing a solid +1.87% gain. Maintaining equity holding patience and letting winners run toward the +3.5% to +5.0% take-profit targets. GLD is displaying a strong confirmed uptrend above the SMA20 with a favorable 1h RSI of 58.0 and positive hourly momentum (+1.56%), making it an attractive candidate for capital deployment if cash permits. Keeping crypto exposure completely flat due to ongoing downside trends."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **89** | 🎯 **42.7%** (38W / 36L / 15BE) | 🔴 **$-1.23 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-09 11:30` | 🟢 BUY | `GLD` | $7.00 | $378.35 | GLD is in a confirmed uptrend above its SMA20, market status is open, 1-hour momentum is s... |
| `2026-11-06 13:10` | 🟢 BUY | `MSFT` | $7.00 | $534.82 | MSFT is in a confirmed uptrend above its SMA20, market status is open, 1-hour RSI has reco... |
| `2026-11-05 17:40` | 🟢 BUY | `AAPL` | $6.50 | $345.35 | AAPL is in a confirmed uptrend above its SMA20, market status is open, and 1-hour momentum... |
| `2026-11-05 11:20` | 🔴 SELL (-0.15$) | `ETH-USD` | $6.85 | $2374.60 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -2.10% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-05 01:41` | 🟢 BUY | `ETH-USD` | $7.00 | $2425.59 | ETH-USD is in a confirmed uptrend above its SMA20, market status is open 24/7, 1-hour RSI ... |

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
