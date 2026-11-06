# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-06 13:40:40`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.14 USD** | **$13.51 USD** | **$38.65 USD** | 🔴 **-3.39%** ($-1.35) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $344.76 | $6.49 | 📉 -0.17% | 19h 59m |
| `MSFT` | 0.013089 | $534.82 | $536.34 | $7.02 | 📈 +0.28% | 29m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market remains largely under pressure, with most assets trading below their SMA20 daily trend lines, indicating a persistent defensive backdrop. However, key mega-cap equities such as AAPL and MSFT remain resilient in confirmed uptrends above their SMA20. Cryptocurrencies like BTC-USD and ETH-USD are currently consolidating below their SMAs with negative or flat short-term momentum, meaning no high-quality crypto pullback criteria are met. Following the equity holding patience rule, our current open equity positions (AAPL and MSFT) are maintained as they are comfortably within normal noise ranges, well above stop-loss levels."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is in a confirmed uptrend above its SMA20. Following the equity holding patience rule, we hold the position steady and let it play out without premature rotation.
- **[HOLD] MSFT** (Confidence: 90%): MSFT remains in a confirmed uptrend above its SMA20 with positive performance. Holding patiently per the equity holding patience rule.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL and MSFT patiently according to equity holding patience. Stop-loss triggers remain active near -2.0% for both positions, and take-profit targets are set at +3.5% to +5.0%. No new entries will be made until a high-quality asset meets the strict trend and reversal confirmation triggers (rsi_1h >= 32 and change_1h_pct > 0.0 in a confirmed uptrend)."
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
