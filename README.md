# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-10 13:51:24`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.01 USD** | **$13.66 USD** | **$38.67 USD** | 🔴 **-3.33%** ($-1.33) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $347.76 | $6.55 | 📈 +0.70% | 4d 20h |
| `MSFT` | 0.013089 | $534.82 | $543.41 | $7.11 | 📈 +1.61% | 4d 0h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market exhibits mixed conditions with several key indices and assets trading below their SMA20 lines, indicating short-term bearish pressure. Cryptocurrencies remain under heavy selling pressure with all major assets (BTC, ETH, SOL) deep in downtrends and failing the reversal confirmation criteria. Meanwhile, our core equity positions, AAPL and MSFT, remain securely above their SMA20 lines in confirmed uptrends, showing resilience and positive small gains (+0.7% and +1.61% respectively). Adhering to the equity holding patience rule and strict trend filters, no action is required to close these positions prematurely, and no new purchases are warranted at this moment."

**Cycle Actions:**
- *No changes this cycle (HOLD)*

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL and MSFT comfortably above their SMA20 lines. Continue to monitor positions for the +3.0% to +5.0% profit target while respecting the hard stop-loss at -2.0%. Cash reserves stand at $25.01 USD. Avoid all downtrending assets and crypto until structural reversals and positive 1-hour momentum confirmations materialize."
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
