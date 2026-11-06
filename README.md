# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-06 14:40:37`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.14 USD** | **$13.46 USD** | **$38.59 USD** | 🔴 **-3.51%** ($-1.41) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $343.88 | $6.47 | 📉 -0.43% | 20h 59m |
| `MSFT` | 0.013089 | $534.82 | $533.73 | $6.99 | 📉 -0.20% | 1h 29m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Major equity indices like SPY, QQQ, and NVDA remain under heavy pressure, trading below their SMA20 with 1-hour momentum declining. Crypto assets (BTC-USD, ETH-USD, SOL-USD) are also seeing downward 1-hour price action. Our current holdings AAPL and MSFT are both in confirmed uptrends above their SMA20 but are experiencing minor short-term pullbacks (-0.43% and -0.20% PnL respectively) with negative 1-hour changes. Following our equity holding patience and trend-following pullback rules, we maintain our positions as neither has hit stop-loss limits (-1.8% to -2.0%) or profit targets (+3.0% to +5.0%). No new buys are triggered as 1-hour candles are currently red across the board."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): Asset remains in an uptrend above SMA20. Short-term dip is within normal noise; holding patiently per equity patience rules while monitoring stop-loss limits.
- **[HOLD] MSFT** (Confidence: 85%): Asset is in a confirmed uptrend above SMA20 with minimal drawdown. Maintaining position to let the trade play out.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain patience with AAPL and MSFT holdings. Monitor for stop-loss at -1.8% and take-profit targets at +3.0% to +5.0%. Wait for positive 1-hour momentum confirmation (change_1h_pct > 0.0 and rsi_1h >= 32) before considering any new allocations. Keep cash reserves intact."
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
