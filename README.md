# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-07 12:00:49`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.14 USD** | **$13.39 USD** | **$38.53 USD** | 🔴 **-3.69%** ($-1.47) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $342.37 | $6.44 | 📉 -0.86% | 1d 18h |
| `MSFT` | 0.013089 | $534.82 | $530.61 | $6.94 | 📉 -0.79% | 22h 50m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market is currently closed or experiencing weekend price freezes, with all monitored equities and major market indices sitting below their respective SMA20 trend filters in a bearish posture. Cryptocurrencies are open for 24/7 trading, but none meet our strict quantitative criteria for trend alignment and reversal confirmation (all are under SMA20, lacking a validated bullish breakout above the trend threshold). Our current holdings in AAPL and MSFT are in closed status and exhibit minor temporary pullbacks that do not breach our strict -2.0% circuit breaker threshold. Capital preservation dictates patience and holding current equity positions while maintaining our cash reserve."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): Asset is currently in a closed market status and holding within acceptable risk parameters above the strict -2.0% stop-loss threshold. Adhering to equity holding patience rule.
- **[HOLD] MSFT** (Confidence: 100%): Asset is currently in a closed market status and holding within acceptable risk parameters above the strict -2.0% stop-loss threshold. Adhering to equity holding patience rule.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain current equity positions in AAPL and MSFT through the weekend freeze, monitoring their distance from the -2.0% stop-loss threshold. Keep cash reserves intact at $25.14. Avoid crypto exposure due to prevailing bearish trends below SMA20 across all major tokens. Wait for traditional markets to re-open and for confirmed UPTREND structures (above SMA20 with positive 1H momentum and RSI >= 32) before deploying additional capital into new setups."
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
