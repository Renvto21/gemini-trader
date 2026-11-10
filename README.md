# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-10 14:10:57`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.01 USD** | **$13.67 USD** | **$38.68 USD** | 🔴 **-3.31%** ($-1.32) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $348.36 | $6.56 | 📈 +0.87% | 4d 20h |
| `MSFT` | 0.013089 | $534.82 | $543.11 | $7.11 | 📈 +1.55% | 4d 1h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market reflects continued weakness as major indices like QQQ, SPY, NVDA, and GLD trend below their SMA20 lines following hot inflation data and tech selloffs. However, our equity holdings AAPL and MSFT remain strong, trading above their SMA20 trend lines in confirmed uptrends. Crypto assets remain suppressed in clear downtrends below SMA20, prompting us to stay entirely sidelined in crypto per our strict trend and anti-correlation constraints."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is in a confirmed uptrend above its SMA20 with positive momentum (+0.28% 1h change). Following equity holding patience rules, we maintain the position as it builds toward the +3.0% to +5.0% profit target without hitting any stop-loss triggers.
- **[HOLD] MSFT** (Confidence: 90%): MSFT remains above its SMA20 line in a solid uptrend with positive 1-hour momentum. Current PnL is +1.55%, holding steady toward the target profit band while respecting risk parameters.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL and MSFT comfortably in confirmed uptrends above their SMA20. Monitor closely for profit targets between +3.0% and +5.0% or maintain patience while respecting the hard stop-loss at -2.0%. Avoid all downtrended assets and crypto until structural trend reversals and positive momentum confirmations are achieved."
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
