# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-10 12:30:50`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.01 USD** | **$13.64 USD** | **$38.65 USD** | 🔴 **-3.38%** ($-1.35) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $347.05 | $6.53 | 📈 +0.49% | 4d 18h |
| `MSFT` | 0.013089 | $534.82 | $542.77 | $7.10 | 📈 +1.49% | 3d 23h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market remains mixed with macroeconomic pressures following hotter inflation data and continued downward pressure on crypto and select tech names. Key crypto assets like BTC, ETH, and SOL are firmly in a bear trend below their SMA20 with weak momentum, rendering them uninvestable under strict trend-following filters. Meanwhile, our equity holdings AAPL and MSFT remain resilient, maintaining their position above the SMA20 trend line with stable 1H RSI readings. We continue to practice equity holding patience, allowing our winning positions room to run towards our profit targets while maintaining a healthy cash reserve."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 80%): AAPL remains in a confirmed uptrend above the SMA20 with positive momentum and PnL. In accordance with equity holding patience, we will let this winning position run.
- **[HOLD] MSFT** (Confidence: 80%): MSFT is holding strong above its SMA20 with solid gains. No reason to exit prematurely; maintaining position to let profits accumulate.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL and MSFT as they remain in a confirmed uptrend above the SMA20 with positive PnL. Avoid all crypto and downtrend assets due to strict trend rules. Maintain cash reserve above $4.00 USD and look for confirmed pullbacks in uptrending equities for future deployment."
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
