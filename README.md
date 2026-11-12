# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-12 11:50:49`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$31.84 USD** | **$6.73 USD** | **$38.57 USD** | 🔴 **-3.57%** ($-1.43) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $357.53 | $6.73 | 📈 +3.53% | 6d 18h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market remains largely under selling pressure with most assets trading below their SMA20 trend lines, reflecting ongoing macro uncertainty and headline-driven volatility, particularly in tech following recent executive shakeups. AAPL is the notable exception, displaying relative strength in an confirmed uptrend above its SMA20 with a high profit margin, currently exhibiting strong overbought conditions on the 1H RSI. Cryptocurrencies and other major equities remain in downtrends or fail to meet strict pullback and confirmation triggers."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL remains in a confirmed uptrend above the SMA20 with a positive PnL of +3.53%. Adhering to the equity holding patience rule, we continue holding this position to let the winner run while monitoring take-profit criteria.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain our single equity holding in AAPL in alignment with equity holding patience rules, closely monitoring its overbought 1H RSI (96.6) to lock in profits between +3.0% and +5.0% if momentum shows signs of exhaustion. No crypto or new equity buys will be executed due to the strict trend filter and lack of confirmed bullish reversal triggers across the rest of the board."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **91** | 🎯 **41.8%** (38W / 38L / 15BE) | 🔴 **$-1.52 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-11 12:20` | 🔴 SELL (-0.17$) | `MSFT` | $6.83 | $521.92 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -2.41% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-10 11:31` | 🔴 SELL (-0.12$) | `GLD` | $6.87 | $371.60 | GLD has fallen below its SMA20 trend line and its current PnL is approaching the strict st... |
| `2026-11-09 11:30` | 🟢 BUY | `GLD` | $7.00 | $378.35 | GLD is in a confirmed uptrend above its SMA20, market status is open, 1-hour momentum is s... |
| `2026-11-06 13:10` | 🟢 BUY | `MSFT` | $7.00 | $534.82 | MSFT is in a confirmed uptrend above its SMA20, market status is open, 1-hour RSI has reco... |
| `2026-11-05 17:40` | 🟢 BUY | `AAPL` | $6.50 | $345.35 | AAPL is in a confirmed uptrend above its SMA20, market status is open, and 1-hour momentum... |

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
