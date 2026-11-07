# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-07 04:00:41`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.14 USD** | **$13.39 USD** | **$38.53 USD** | 🔴 **-3.69%** ($-1.47) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $342.37 | $6.44 | 📉 -0.86% | 1d 10h |
| `MSFT` | 0.013089 | $534.82 | $530.61 | $6.94 | 📉 -0.79% | 14h 49m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market is currently in a defensive posture with all major assets—both stocks and cryptocurrencies—trading below their SMA20 trend lines (BAJISTA). Wall Street equities (AAPL, MSFT, QQQ, SPY, NVDA, GLD) are closed for the weekend, preventing any trade execution on equities per rule constraints. Existing positions in AAPL and MSFT are currently experiencing minor unrealized drawdowns (-0.86% and -0.79% respectively), well above our hard circuit breaker stop-loss threshold of -2.0%. Cryptocurrencies are open 24/7, but none currently meet our strict trend filter criteria as they are all below their SMA20 and lack clear reversal triggers with sufficient momentum."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): Asset market status is closed for the weekend. The position is well within acceptable drawdown parameters (-0.86%) and above the strict stop-loss limit. Upholding equity holding patience rule.
- **[HOLD] MSFT** (Confidence: 100%): Asset market status is closed for the weekend. The position is holding steady with a minor drawdown of -0.79%, safely above the stop-loss circuit breaker threshold.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing AAPL and MSFT equity positions through the weekend, keeping close watch on stop-loss levels (-1.8% to -2.0%). Do not open any new crypto or equity positions as market conditions show all tracked assets in a downtrend (below SMA20). Wait for Wall Street to reopen and for confirmed bullish trend breakouts or valid pullback reversal confirmations before deploying cash reserves."
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
