# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-10 16:40:51`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.01 USD** | **$13.56 USD** | **$38.57 USD** | 🔴 **-3.57%** ($-1.43) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $348.52 | $6.56 | 📈 +0.92% | 4d 23h |
| `MSFT` | 0.013089 | $534.82 | $535.03 | $7.00 | 📈 +0.04% | 4d 3h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market remains cautious with major indices and crypto assets under pressure, trading mostly below their SMA20 lines. AAPL and MSFT continue to show resilience, holding confirmed uptrends above their SMA20 despite minor intraday consolidation. Cryptocurrencies and high-beta names like NVDA are deep in a downtrend (below SMA20) with weak hourly momentum, reinforcing the rule to avoid falling knives. Current open positions in AAPL and MSFT remain compliant with our trend-following strategy and are exhibiting patience as equity holding time rules dictate."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL remains in a confirmed uptrend above the SMA20 with positive weekly performance. Holding per equity patience rules and targeting asymmetric upside.
- **[HOLD] MSFT** (Confidence: 90%): MSFT is trading above its SMA20 in a solid uptrend. No structural reason to sell; adhering to holding patience for equities.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintained existing AAPL and MSFT positions as both stay above their SMA20 lines in healthy uptrends. Avoided all crypto and downtrending equities due to failure of trend and reversal triggers (negative 1-hour momentum or below SMA20). Will continue to hold current positions targeting +3.0% to +5.0% gains and monitoring strictly against the -2.0% stop-loss threshold."
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
