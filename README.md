# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-09 12:30:46`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.14 USD** | **$20.67 USD** | **$38.81 USD** | 🔴 **-2.98%** ($-1.19) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $350.51 | $6.60 | 📈 +1.49% | 3d 18h |
| `MSFT` | 0.013089 | $534.82 | $541.79 | $7.09 | 📈 +1.30% | 2d 23h |
| `GLD` | 0.018501 | $378.35 | $377.37 | $6.98 | 📉 -0.26% | 59m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The portfolio is currently holding three strong equity and commodity positions (AAPL, MSFT, GLD) that remain in confirmed uptrends above their SMA20. Overall market conditions show a divergence between healthy large-cap tech/gold names and struggling crypto assets or tech names facing specific news headwinds (like NVDA). Cryptocurrencies (BTC, ETH, SOL) and indices like SPY and QQQ continue to trade below their SMA20, signaling that we must stay out of them due to our strict trend-following and anti-falling-knife rules. Cash reserves stand comfortably at $18.14 above our minimum threshold."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): AAPL is maintaining a solid uptrend above its SMA20 with positive multi-day momentum. Following equity holding patience rules, we let winners run and keep the position open.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain positions in AAPL, MSFT, and GLD as they respect their uptrend channels. Take-profit targets are locked between +3.5% and +5.0%, and stop-losses are firmly observed at -1.8% to -2.0%. Continue to exercise patience and hold off on new crypto or equity entries until clear pullback confirmation triggers materialize."
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
