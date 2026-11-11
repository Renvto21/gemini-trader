# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-11 11:31:06`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.01 USD** | **$13.57 USD** | **$38.59 USD** | 🔴 **-3.53%** ($-1.41) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $350.41 | $6.60 | 📈 +1.47% | 5d 17h |
| `MSFT` | 0.013089 | $534.82 | $533.26 | $6.98 | 📉 -0.29% | 4d 22h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader equity market is showing mixed recovery signals with tech futures and indices like QQQ and SPY ticking upward on the day, but many major tickers remain below their crucial SMA20 trend lines, categorizing them as downtrending for strict rule adherence. Our active holdings, AAPL and MSFT, are both currently open, in confirmed uptrends above their SMA20, and displaying resilience. AAPL is holding a positive PnL (+1.47%), while MSFT is flat/slightly negative (-0.29%) but well within acceptable holding patience parameters. Cryptocurrencies and other assets like GLD, NVDA, and QQQ are either below SMA20 or failing to meet the rigorous buy trigger criteria (positive 1h change and RSI >= 32 simultaneously with confirmed uptrends). We continue to prioritize capital preservation and equity patience."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in a confirmed uptrend above its SMA20 with a positive PnL (+1.47%). Adhering to the equity holding patience rule, we will let the winner run rather than prematurely exiting, targeting a +3.0% to +5.0% gain.
- **[HOLD] MSFT** (Confidence: 85%): MSFT remains in a confirmed uptrend above its SMA20. Despite minor fluctuations (-0.29%), equity patience dictates holding unless stop-loss limits (-1.8% to -2.0%) are breached or take-profit targets are reached.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintained AAPL and MSFT positions, respecting equity holding patience for slower-moving equities. AAPL is approaching profitable territory (+1.47%), and we will monitor for take-profit opportunities if RSI rises above 72 with gains reaching the +3.0% to +5.0% threshold. MSFT is holding steady near support. Keep cash reserves intact above $4.00 USD and avoid crypto or downtrending assets until strict trend filters and reversal confirmation triggers align."
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
