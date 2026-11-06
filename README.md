# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-05 22:00:50`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.14 USD** | **$6.58 USD** | **$38.71 USD** | 🔴 **-3.21%** ($-1.29) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $349.51 | $6.58 | 📈 +1.20% | 4h 20m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Wall Street markets are currently closed (CERRADO), leaving active liquidity confined to cryptocurrencies. However, all major crypto assets (BTC, ETH, SOL) are deep in a confirmed downtrend below their SMA20 with low hourly RSI values and negative 1-hour changes, failing the strict trend filter and reversal confirmation triggers. Meanwhile, our only active equity position (AAPL) is currently closed for the weekend/evening session but remains in a confirmed uptrend above its SMA20 with a slight positive return (+1.2%). Following our strict rule on equity holding patience and avoiding falling knives in crypto, we hold our current position and maintain cash reserves."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): AAPL is in a confirmed uptrend above the SMA20 and is performing well with a +1.2% gain. Adhering to the equity holding patience rule, we maintain the position without premature rotation, respecting our stop-loss and take-profit targets.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL position patiently as it remains above the SMA20 trend line. Take-profit targets remain set at +3.0% to +5.0% and stop-loss is protected near -2.0%. Crypto markets are in severe downtrends with no valid 1-hour green candle confirmation or RSI recovery above 32, so crypto exposure continues to be avoided. Cash reserves remain well above the $4.00 minimum at $32.14."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **89** | 🎯 **42.7%** (38W / 36L / 15BE) | 🔴 **$-1.23 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-05 17:40` | 🟢 BUY | `AAPL` | $6.50 | $345.35 | AAPL is in a confirmed uptrend above its SMA20, market status is open, and 1-hour momentum... |
| `2026-11-05 11:20` | 🔴 SELL (-0.15$) | `ETH-USD` | $6.85 | $2374.60 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -2.10% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-05 01:41` | 🟢 BUY | `ETH-USD` | $7.00 | $2425.59 | ETH-USD is in a confirmed uptrend above its SMA20, market status is open 24/7, 1-hour RSI ... |
| `2026-11-04 22:00` | 🔴 SELL (-0.31$) | `MSFT` | $6.69 | $520.99 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -4.44% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-04 11:30` | 🟢 BUY | `MSFT` | $7.00 | $545.20 | MSFT is currently the only asset trading above its SMA20 in a confirmed uptrend with stron... |

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
