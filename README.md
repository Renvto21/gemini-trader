# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-06 13:10:45`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.14 USD** | **$13.49 USD** | **$38.63 USD** | 🔴 **-3.42%** ($-1.37) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $345.04 | $6.49 | 📉 -0.09% | 19h 30m |
| `MSFT` | 0.013089 | $534.82 | $534.82 | $7.00 | 📈 +0.00% | 0m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market remains mostly bearish with major indices like QQQ, SPY, and crypto assets trading below their respective SMA20 levels, signaling caution. However, selective equities such as AAPL and MSFT remain in a confirmed uptrend above the SMA20. AAPL is currently held in the portfolio while consolidating slightly near entry, respecting equity holding patience guidelines. MSFT is showing a bullish trend structure with a positive 1-hour percentage change of +0.41% and an increasing 1-hour RSI approaching the entry threshold, presenting a solid setup for a disciplined trend-following pullback entry."

**Cycle Actions:**
- **[BUY] MSFT** (Confidence: 85%): MSFT is in a confirmed uptrend above its SMA20, market status is open, 1-hour RSI has recovered above 29 and ticked up with a positive 1-hour candle change (+0.41%), confirming a high-quality pullback entry.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL position while monitoring for take-profit targets between +3.5% and +5.0% and strict stop-loss protection near -2.0%. MSFT is in an uptrend (above SMA20) with a positive 1-hour change (+0.41%) and RSI ticking upwards, meeting our pullback criteria for a $7.00 allocation. Maintaining cash reserves above the $4.00 minimum."
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
