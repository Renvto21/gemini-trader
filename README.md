# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-10 14:30:54`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.01 USD** | **$13.55 USD** | **$38.56 USD** | 🔴 **-3.59%** ($-1.44) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $348.17 | $6.55 | 📈 +0.82% | 4d 20h |
| `MSFT` | 0.013089 | $534.82 | $534.76 | $7.00 | 📉 -0.01% | 4d 1h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market is exhibiting cautious behavior, with major equity indices like SPY, QQQ, and NVDA trading in a downtrend below their respective SMA20 lines. AAPL and MSFT remain strong outliers, holding firm in confirmed uptrends above their SMA20 lines despite minor intraday pullbacks. Cryptocurrencies are currently under severe downward pressure and remain strictly in bear trends (below SMA20 with low RSI levels), making them uninvestable under our trend-following rules. We maintain patience with our existing equity positions (AAPL and MSFT) as they respect equity holding patience principles and remain above critical technical thresholds."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL remains in a confirmed uptrend above its SMA20 line with solid resilience. Following equity holding patience rules, we maintain the position as it fluctuates within normal parameters.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain patience with AAPL and MSFT as they continue to hold above their SMA20 trend lines. Monitor positions for profit targets between +3.0% and +5.0% or adhere strictly to the hard stop-loss at -2.0%. Avoid all crypto assets and downtrended equities like NVDA, SPY, and QQQ until structural trend reversals and confirmed upward momentum triggers are met."
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
