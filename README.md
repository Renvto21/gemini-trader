# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-06 15:50:40`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.14 USD** | **$13.47 USD** | **$38.61 USD** | 🔴 **-3.48%** ($-1.39) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $344.43 | $6.48 | 📉 -0.27% | 22h 9m |
| `MSFT` | 0.013089 | $534.82 | $534.09 | $6.99 | 📉 -0.14% | 2h 39m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market continues to exhibit cautious recovery following recent tech and crypto sell-offs. Major equity indexes like SPY and QQQ remain in a downtrend below their SMA20 lines, indicating that broad market risk is still elevated. However, specific quality holdings such as AAPL and MSFT remain in confirmed uptrends above their SMA20 lines and are holding steady despite short-term consolidation. In the crypto sector, assets remain mostly in bearish daily structures under their respective SMA20 thresholds, requiring strict adherence to our anti-correlation and trend-following rules. GLD shows strength as a defensive asset in an uptrend, presenting potential pullback opportunities if confirmation criteria are met."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in a confirmed uptrend above its SMA20 and has been held for less than 24 hours. Per our equity holding patience rule, stocks are given time to play out unless stop-loss limits are breached. Current PnL is minimal (-0.27%), so we hold.
- **[HOLD] MSFT** (Confidence: 85%): MSFT remains above its SMA20 in a confirmed uptrend with a very minor pullback (-0.14%). Sticking to equity holding patience to let the position develop toward our +3.0% to +5.0% take-profit target.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "We are maintaining our current equity positions in AAPL and MSFT patiently according to our holding rules, as both remain above the SMA20 trend filter. Cash reserves are at $25.14 USD, comfortably above our $4.00 minimum reserve rule. For upcoming cycles, we will watch GLD for a potential pullback entry if it maintains its uptrend and meets our RSI >= 32 and positive 1-hour momentum confirmation triggers. Stop-loss triggers remain strictly set at -2.0% for open positions, and take-profit targets are locked between +3.0% and +5.0%."
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
