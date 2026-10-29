# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-29 14:41:08`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.23 USD** | **$7.05 USD** | **$39.28 USD** | 🔴 **-1.81%** ($-0.72) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $349.70 | $7.05 | 📈 +0.73% | 6d 1h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market is currently exhibiting a bearish tone, with major indices like SPY, QQQ, and most individual equities (MSFT, NVDA, GLD) trading below their respective SMA20 trend filters. AAPL remains a notable exception, maintaining its position in a confirmed uptrend above the SMA20 with positive 24-hour and 7-day performance. Cryptocurrencies are also under pressure, trading below their SMA20 levels. With strict trend-following rules in place, we avoid catching falling knives in bearish assets and remain patient with our only winning equity position."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is maintaining its confirmed uptrend above the SMA20. In accordance with equity holding patience and strict trend rules, we will hold the position steady and let it play out toward our profit targets without premature rotation.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "We continue to hold our AAPL position patiently as it remains in a confirmed uptrend above the SMA20, currently showing a +0.73% unrealized gain. We will maintain this holding until our take-profit target of +3.0% to +5.0% is achieved, or if RSI 1H exceeds 72 with sufficient profit, or if the stop-loss limit of -1.8% is triggered. Cash reserves are robust at $32.23. We are monitoring all assets for valid pullbacks in confirmed uptrend conditions before deploying additional capital."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **86** | 🎯 **44.2%** (38W / 33L / 15BE) | 🔴 **$-0.64 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-28 13:21` | 🔴 SELL (-0.02$) | `MSFT` | $6.48 | $528.16 | MSFT has shifted to a bearish trend below its SMA20 and current performance is near our st... |
| `2026-10-26 12:01` | 🟢 BUY | `MSFT` | $6.50 | $530.04 | MSFT is in a confirmed uptrend above its SMA20, and the 1-hour RSI (62.8) and 1-hour perce... |
| `2026-10-23 13:40` | 🟢 BUY | `AAPL` | $7.00 | $347.17 | AAPL is in a confirmed uptrend above its SMA20, satisfying our strict trend filter. The 1-... |
| `2026-10-22 16:00` | 🔴 SELL (-0.12$) | `MSFT` | $6.88 | $521.40 | MSFT has dropped to a PnL of -1.71%, closely approaching our mandatory stop-loss threshold... |
| `2026-10-22 14:40` | 🔴 SELL (+0.17$) | `AAPL` | $10.17 | $346.52 | AAPL rsi_1h has surpassed 72 (currently 73.4) with a positive return of +1.73%, satisfying... |

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
