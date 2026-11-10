# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-10 16:50:45`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.01 USD** | **$13.58 USD** | **$38.59 USD** | 🔴 **-3.52%** ($-1.41) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $348.76 | $6.56 | 📈 +0.99% | 4d 23h |
| `MSFT` | 0.013089 | $534.82 | $536.00 | $7.02 | 📈 +0.22% | 4d 3h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market remains cautious with several indices and equities trading below their SMA20 lines due to macro concerns and inflationary pressures. However, AAPL and MSFT remain solid exceptions, holding firmly above their SMA20 trend lines in constructive uptrends. Cryptocurrencies and other major indices continue to show weakness or are in bearish trends, failing the strict trend-following filters."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is trading above its SMA20 in a confirmed uptrend and exhibits positive hourly momentum. Following the equity holding patience rule, we continue to hold and let the winner run toward the +3.0% to +5.0% target.
- **[HOLD] MSFT** (Confidence: 85%): MSFT maintains its position above the SMA20 trend line with stable performance. Adhering to equity holding patience, we will hold this position rather than prematurely rotating out.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintained existing AAPL and MSFT positions following the equity holding patience rule since both continue to trade above their SMA20 lines with positive hourly momentum. Avoided entering new crypto positions as BTC-USD, ETH-USD, and SOL-USD remain in clear downtrends below their SMA20 lines. Continuing to monitor positions for the +3.0% to +5.0% take-profit target while respecting the strict -2.0% stop-loss threshold."
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
