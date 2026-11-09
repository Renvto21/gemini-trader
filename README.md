# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-09 11:40:44`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.14 USD** | **$20.67 USD** | **$38.81 USD** | 🔴 **-2.99%** ($-1.19) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $349.60 | $6.58 | 📈 +1.23% | 3d 18h |
| `MSFT` | 0.013089 | $534.82 | $542.96 | $7.11 | 📈 +1.52% | 2d 22h |
| `GLD` | 0.018501 | $378.35 | $377.38 | $6.98 | 📉 -0.26% | 9m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader equity market is showing recovery signs today with major indices and holdings like MSFT (+2.33%), AAPL (+2.12%), and GLD (+1.3%) moving higher and maintaining their confirmed uptrends above the SMA20. Conversely, assets like NVDA, QQQ, and SPY remain below their SMA20 despite intraday bounces, keeping them off the buy list per the trend filter rule. Crypto assets (BTC-USD, ETH-USD, SOL-USD) are currently in downtrends below the SMA20, so crypto exposure remains strictly flat. Current positions in AAPL, MSFT, and GLD are performing well or holding steady; equity holding patience is applied to let winners run toward our take-profit targets."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): AAPL remains in a confirmed uptrend above its SMA20 with positive momentum. Applying equity holding patience to let winners run toward take-profit targets.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Existing positions AAPL, MSFT, and GLD continue to hold steady above their respective SMA20 thresholds. We will maintain these equity holdings with patience, letting them run toward take-profit targets of +3.5% to +5.0% while respecting stop-loss levels at -1.8% to -2.0%. Cash reserve is at $18.14 USD, ensuring adequate liquidity above the $4.00 minimum. No new entries are warranted today as crypto assets are in downtrends and we maintain a one-crypto limit, while equity opportunities that fit strict pullback criteria are currently fully allocated."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **89** | 🎯 **42.7%** (38W / 36L / 15BE) | 🔴 **$-1.23 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-09 11:30` | 🟢 BUY | `GLD` | $7.00 | $378.35 | GLD is in a confirmed uptrend above its SMA20, market status is open, 1-hour momentum is s... |
| `2026-11-06 13:10` | 🟢 BUY | `MSFT` | $7.00 | $534.82 | MSFT is in a confirmed uptrend above its SMA20, market status is open, 1-hour RSI has reco... |
| `2026-11-05 17:40` | 🟢 BUY | `AAPL` | $6.50 | $345.35 | AAPL is in a confirmed uptrend above its SMA20, market status is open, and 1-hour momentum... |
| `2026-11-05 11:20` | 🔴 SELL (-0.15$) | `ETH-USD` | $6.85 | $2374.60 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -2.10% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-05 01:41` | 🟢 BUY | `ETH-USD` | $7.00 | $2425.59 | ETH-USD is in a confirmed uptrend above its SMA20, market status is open 24/7, 1-hour RSI ... |

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
