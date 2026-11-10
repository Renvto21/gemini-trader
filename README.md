# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-10 11:50:41`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.01 USD** | **$13.68 USD** | **$38.69 USD** | 🔴 **-3.28%** ($-1.31) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $350.04 | $6.59 | 📈 +1.36% | 4d 18h |
| `MSFT` | 0.013089 | $534.82 | $541.58 | $7.09 | 📈 +1.26% | 3d 22h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader equity market and crypto assets are experiencing mild to moderate downward pressure following hotter consumer inflation data. Most major indices (SPY, QQQ) and crypto assets (BTC-USD, ETH-USD, SOL-USD) remain below their SMA20 trend filters in bearish configurations. However, AAPL and MSFT remain strong exceptions, holding above their respective SMA20 lines in confirmed uptrends. Our current positions in AAPL and MSFT are profitable (+1.36% and +1.26% respectively) and continue to display healthy technical conditions despite slight intraday pullbacks."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL remains in a confirmed uptrend (above SMA20) with positive unrealized gains (+1.36%). Adhering to the equity holding patience rule, we continue to let the winner run toward our +3% to +5% target.
- **[HOLD] MSFT** (Confidence: 90%): MSFT is in a confirmed uptrend above its SMA20 with stable unrealized gains (+1.26%). Holding position patiently to let momentum play out.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL and MSFT as they remain in confirmed uptrends above their SMA20. Will monitor AAPL and MSFT for take-profit targets between +3.0% and +5.0% or if RSI 1h climbs above 72. All crypto assets and other equities remain in downtrends or fail to meet the strict pullback confirmation rules (change_1h_pct > 0.0), so no new trades are initiated. Cash reserves remain healthy at $25.01."
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
