# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-05 23:20:45`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.14 USD** | **$6.58 USD** | **$38.71 USD** | 🔴 **-3.21%** ($-1.29) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $349.51 | $6.58 | 📈 +1.20% | 5h 40m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader equity and crypto markets experienced severe downward pressure recently, with Wall Street suffering notable losses and crypto assets testing local lows. Most traditional equities and crypto assets are currently categorized as 'CERRADO' or showing bearish trends below their respective SMA20 levels, failing our strict trend-following filters. However, our sole active position in AAPL remains above the SMA20 in a confirmed uptrend and is currently held patiently with a minor positive PnL (+1.2%), despite the market being closed. Cryptocurrencies remain below their SMA20 levels with weak 1-hour candles, meaning no crypto buys are justified under our anti-falling-knife and reversal confirmation rules. Cash reserves remain healthy above the required minimum."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is currently in a confirmed uptrend above the SMA20 with positive PnL. Adhering to the equity holding patience rule, we continue holding through flat or minor fluctuations while waiting for the take-profit target (+3.0% to +5.0%) or stop-loss protection.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain the current AAPL position patiently as it stays above the SMA20. Monitor for take-profit opportunities between +3.0% and +5.0% or execute stop-loss if price drops below -1.8%. Avoid all crypto assets and closed stocks during this cycle as they fail our strict trend and market-status filters. Keep cash reserves secure above $4.00."
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
