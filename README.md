# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-09 01:20:38`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.14 USD** | **$13.39 USD** | **$38.53 USD** | 🔴 **-3.69%** ($-1.47) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $342.37 | $6.44 | 📉 -0.86% | 3d 7h |
| `MSFT` | 0.013089 | $534.82 | $530.61 | $6.94 | 📉 -0.79% | 2d 12h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market is currently in a defensive posture with all major equities and crypto assets trading below their SMA20 trend lines, signaling a broader bearish correction. Wall Street equities (AAPL, MSFT, SPY, QQQ, NVDA) are closed for the weekend, meaning prices are frozen and no actions can be taken on them per our market status rules. In the crypto sector, BTC-USD shows a slight positive 1-hour momentum (+0.17%) and an RSI of 37.5, but its overarching trend remains firmly bearish under the SMA20, violating our strict trend-following pullback rules. Therefore, no crypto buys are authorized. Our current equity positions in AAPL and MSFT must be held patiently through the weekend in accordance with equity holding patience guidelines, as neither has breached the hard stop-loss threshold of -1.8% to -2.0%."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): Asset is currently closed for the weekend. Position is within normal holding fluctuation (-0.86% PnL) and well above the strict stop-loss threshold. Maintaining patience as per equity holding rules.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintained AAPL and MSFT equity positions through the weekend shutdown without panic, adhering to holding patience rules. Avoided entering any crypto assets (BTC-USD, ETH-USD, SOL-USD) because all are trading below their SMA20 despite brief hourly bounces. For upcoming cycles, wait for a confirmed daily uptrend (price crossing back above SMA20) combined with positive 1-hour momentum before entering any new positions. Monitor current stop-losses closely on AAPL and MSFT when Wall Street reopens."
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
