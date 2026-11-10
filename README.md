# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-10 15:10:40`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.01 USD** | **$13.50 USD** | **$38.52 USD** | 🔴 **-3.71%** ($-1.48) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $347.89 | $6.55 | 📈 +0.74% | 4d 21h |
| `MSFT` | 0.013089 | $534.82 | $531.53 | $6.96 | 📉 -0.62% | 4d 1h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market remains cautious with several indices and assets trading below their SMA20 trend lines, including QQQ, SPY, and GLD, pressured by macroeconomic inflation concerns. However, core equity holdings AAPL and MSFT remain in confirmed uptrends above the SMA20. Cryptocurrencies like BTC-USD, ETH-USD, and SOL-USD are in strong bear trends (below SMA20) with oversold conditions, requiring strict avoidance of catching falling knives per our quantitative rules."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): AAPL remains in a confirmed uptrend above the SMA20 with positive PnL. Adhering to equity holding patience to let the winner run.
- **[HOLD] MSFT** (Confidence: 100%): MSFT remains above its SMA20 in a confirmed uptrend. Current drawdown (-0.62%) is well within normal fluctuation range and above the strict stop-loss threshold.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain current holdings in AAPL and MSFT as they remain in a confirmed uptrend above the SMA20. MSFT's current PnL is down slightly at -0.62%, well above the strict -1.8% to -2.0% stop-loss floor; give equities patience to play out. AAPL is showing positive performance (+0.74%). Do not initiate any new crypto or equity positions until strict trend-following pullback criteria and reversal confirmation triggers (1-hour candle green with RSI >= 32) are fully met."
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
