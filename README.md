# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-02 06:00:51`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.23 USD** | **$6.95 USD** | **$39.17 USD** | 🔴 **-2.06%** ($-0.83) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $344.63 | $6.95 | 📉 -0.73% | 9d 16h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader equity market remains closed with most key indices and stocks (SPY, QQQ, NVDA, MSFT, AAPL, GLD) showing 'CERRADO' status. Among equities, only AAPL remains in a confirmed uptrend (above SMA20), while all other evaluated assets are currently trading in bearish trends below their respective SMA20 lines. In the 24/7 crypto markets, SOL-USD, ETH-USD, and BTC-USD show positive 1-hour changes and RSIs above 32, but they are all in bearish daily trends below their SMA20 levels. Following our strict quantitative trend-following filters, catching falling knives or buying crypto in macro downtrends is prohibited. Therefore, we hold our current AAPL equity position patiently and refrain from opening new crypto positions."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is currently in a confirmed uptrend above its SMA20. Per our equity holding patience and capital preservation rules, we maintain our position while equity markets are closed, monitoring our stop-loss and profit targets.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain the AAPL position patiently as it remains the sole asset in a confirmed uptrend above the SMA20. Monitor stop-loss levels near -1.8% to -2.0% ($340.20) and take-profit targets between +3.0% and +5.0% ($357.50+). Keep crypto exposure at zero due to persistent macro downtrends below the SMA20 across ETH, BTC, and SOL. Wait for equity markets to reopen and present confirmed pullback opportunities above the SMA20 before deploying additional capital from our $32.23 cash reserves."
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
