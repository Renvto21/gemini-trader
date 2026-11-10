# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-10 12:50:49`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.01 USD** | **$13.64 USD** | **$38.65 USD** | 🔴 **-3.38%** ($-1.35) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $347.68 | $6.54 | 📈 +0.67% | 4d 19h |
| `MSFT` | 0.013089 | $534.82 | $541.99 | $7.09 | 📈 +1.34% | 3d 23h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market is under pressure following hotter-than-expected CPI inflation data, pushing major indices and crypto assets into short-term corrections. Crypto assets like BTC, ETH, and SOL are in deep downtrends (below SMA20) with oversold conditions, meaning no immediate buys. Equities like SPY, QQQ, and NVDA are also under SMA20. However, our existing holdings AAPL and MSFT remain resilient, maintaining confirmed uptrends above their SMA20 lines with solid weekly gains, validating our equity holding patience rule."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL remains in a confirmed uptrend above the SMA20 with positive PnL and stable momentum. Adhering to the equity holding patience rule, we continue to let the winner run.
- **[HOLD] MSFT** (Confidence: 90%): MSFT continues to trade above the SMA20 in a solid uptrend with positive performance. Holding the position to reach our take-profit target.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL and MSFT in confirmed uptrends above the SMA20. Both positions are showing positive PnL (+0.67% and +1.34% respectively), and we will let winners run toward our +3.0% to +5.0% target while respecting the hard stop-loss at -2.0%. Avoid all crypto assets and downtrending equities due to bearish macro sentiment. Keep cash reserves intact above $4.00 USD and wait for a clear 1-hour green momentum reversal before deploying capital into new positions."
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
