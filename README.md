# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-09 16:30:46`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.14 USD** | **$20.71 USD** | **$38.85 USD** | 🔴 **-2.88%** ($-1.15) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $351.16 | $6.61 | 📈 +1.68% | 3d 22h |
| `MSFT` | 0.013089 | $534.82 | $544.95 | $7.13 | 📈 +1.89% | 3d 3h |
| `GLD` | 0.018501 | $378.35 | $376.70 | $6.97 | 📉 -0.44% | 4h 59m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Equities are exhibiting broad recovery with major indices like SPY and QQQ advancing over the past 24 hours, though several remain slightly below their 20-period moving averages (SMA20). Among our active holdings, AAPL and MSFT remain solid performers in confirmed uptrends above their SMA20, hovering near +1.7% to +1.9% gains. GLD is consolidating slightly below entry with a minor loss of -0.44% but remains in a confirmed uptrend above its SMA20. Crypto assets continue to trade in a general downtrend below their SMA20, requiring us to stay strictly on the sidelines regarding digital assets per our trend filter and anti-correlation constraints. Market conditions favor holding current equity positions and letting winners run toward our +3.0% to +5.0% target window."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is maintaining a strong uptrend above its SMA20 with a +1.68% gain. We will let the winner run toward our +3.0% to +5.0% profit target instead of selling prematurely.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing positions in AAPL, MSFT, and GLD. Monitor AAPL and MSFT closely for take-profit opportunities if 1-hour RSI crosses above 72 and gains approach the +3.0% to +5.0% target zone. Keep strict stop-loss levels at -2.0% for all holdings. Continue to avoid all crypto assets and below-SMA20 securities until proper trend reversal confirmation occurs."
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
