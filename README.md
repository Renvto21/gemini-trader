# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-06 17:20:46`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.14 USD** | **$13.43 USD** | **$38.57 USD** | 🔴 **-3.58%** ($-1.43) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $343.72 | $6.47 | 📉 -0.47% | 23h 40m |
| `MSFT` | 0.013089 | $534.82 | $531.98 | $6.96 | 📉 -0.53% | 4h 10m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market continues to exhibit cautious consolidation with major equity indices like SPY, QQQ, and NVDA trading below their respective SMA20 trend filters, signaling a broader corrective phase. Crypto assets are similarly under pressure with bearish daily trends. Our current holdings, AAPL and MSFT, are in confirmed uptrends above their SMA20, although experiencing minor short-term pullbacks. Per quantitative rules regarding equity holding patience and strict trend filters, we must hold our existing equity positions and refrain from catching falling knives in crypto or downtrending assets until clear reversal triggers appear."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is in a confirmed uptrend above its SMA20. Current drawdown is minimal (-0.47%), well within acceptable noise limits. Upholding equity holding patience rule to let positions play out.
- **[HOLD] MSFT** (Confidence: 90%): MSFT remains in a confirmed uptrend above its SMA20 with a minor drawdown of -0.53%. Adhering to the holding patience rule to avoid premature rotation.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL and MSFT patiently as per equity holding patience rules. Neither asset has breached the strict -1.8% to -2.0% stop-loss limit, and both remain in confirmed daily uptrends above SMA20. Cash reserve stands at $25.14 USD, well above the $4.00 minimum. Will maintain current positions and monitor for 1-hour green candles and RSI recovery before deploying additional capital."
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
