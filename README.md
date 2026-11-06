# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-06 17:30:48`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.14 USD** | **$13.43 USD** | **$38.57 USD** | 🔴 **-3.57%** ($-1.43) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $343.76 | $6.47 | 📉 -0.46% | 23h 50m |
| `MSFT` | 0.013089 | $534.82 | $532.13 | $6.96 | 📉 -0.50% | 4h 20m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market remains cautious with key indices like QQQ, SPY, and NVDA trading below their SMA20 daily trends, reflecting ongoing macro headwinds and recent tech volatility. However, our core equity holdings AAPL and MSFT remain in confirmed daily uptrends above their SMA20. Despite minor intraday pullbacks, both positions are within acceptable risk parameters and well clear of our strict -2.0% stop-loss threshold. Cryptocurrencies are currently exhibiting choppy sideways to slightly negative 1-hour momentum with 1-hour changes lingering around zero or slightly negative, failing to meet our strict reversal confirmation trigger (rsi_1h >= 32 and change_1h_pct > 0.0 simultaneously on a confirmed uptrend asset). Given our anti-correlation rules, equity holding patience, and minimum cash reserve requirements, the optimal course of action is to hold current equity positions and preserve capital until high-probability trend-following pullbacks present themselves."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in a confirmed daily uptrend above its SMA20 and is well within normal holding parameters. Adhering to equity holding patience rules, we maintain the position as it has not hit the stop-loss or profit-taking targets.
- **[HOLD] MSFT** (Confidence: 85%): MSFT remains in a confirmed daily uptrend above its SMA20. Following equity holding patience guidelines, we hold the position steady and allow it time to play out without reacting to minor flat intraday fluctuations.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL and MSFT patiently according to equity holding patience rules. Both stocks remain above their SMA20 daily trend lines. Cash reserves are robust at $25.14 USD. For upcoming cycles, continue to monitor crypto assets for confirmed uptrend recoveries above SMA20 paired with positive 1-hour momentum, and watch equity positions closely for any approach toward the -1.8% to -2.0% stop-loss threshold while targeting +3.0% to +5.0% for profit-taking."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **89** | 🎯 **42.7%** (38W / 36L / 15BE) | 🔴 **$-1.23 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-06 13:10` | 🟢 BUY | `MSFT` | $7.00 | $534.82 | MSFT is in a confirmed uptrend above its SMA20, market status is open, 1-hour RSI has reco... |
| `2026-11-05 17:40` | 🟢 BUY | `AAPL` | $6.50 | $345.35 | AAPL is in a confirmed uptrend above its SMA20, market status is open, and 1-hour momentum... |
| `2026-11-05 11:20` | 🔴 SELL (-0.15$) | `ETH-USD` | $6.85 | $2374.60 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -2.10% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-05 01:41` | 🟢 BUY | `ETH-USD` | $7.00 | $2425.59 | ETH-USD is in a confirmed uptrend above its SMA20, market status is open 24/7, 1-hour RSI ... |
| `2026-11-04 22:00` | 🔴 SELL (-0.31$) | `MSFT` | $6.69 | $520.99 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -4.44% hit safety limit (-2.0%). Liquidated by code... |

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
