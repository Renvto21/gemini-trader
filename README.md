# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-23 15:10:39`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.25 USD** | **$6.99 USD** | **$39.23 USD** | 🔴 **-1.91%** ($-0.77) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $346.49 | $6.99 | 📉 -0.20% | 1h 29m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market remains largely under selling pressure with most major equities and crypto assets trading below their respective SMA20 trend lines, reflecting a bearish macro context. However, AAPL continues to hold a confirmed bullish trend above its SMA20, currently trading at $346.49 with a minor unrealized drawdown of -0.2%. Other assets like SPY, QQQ, NVDA, and GLD are oversold on short-term RSI metrics but remain in strict downtrends, barring any new entry due to our strict trend-following rule. We maintain patience with our single equity holding AAPL, adhering to equity holding patience rules."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL remains in a confirmed uptrend above its SMA20. Per equity holding patience rules, we do not rotate out of flat or minorly negative positions without hitting our take-profit or stop-loss thresholds. Current PnL is -0.2%, well within normal intraday noise.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL with an unrealized PnL of -0.2%. Strict take-profit target remains at +3.0% to +5.0% or an exit if the 1-hour RSI surpasses 72. Stop-loss remains firmly at -1.8% to protect capital. We continue to monitor crypto assets for any emerging uptrends but currently keep cash reserves secure with $32.25 available."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **85** | 🎯 **44.7%** (38W / 32L / 15BE) | 🔴 **$-0.62 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-23 13:40` | 🟢 BUY | `AAPL` | $7.00 | $347.17 | AAPL is in a confirmed uptrend above its SMA20, satisfying our strict trend filter. The 1-... |
| `2026-10-22 16:00` | 🔴 SELL (-0.12$) | `MSFT` | $6.88 | $521.40 | MSFT has dropped to a PnL of -1.71%, closely approaching our mandatory stop-loss threshold... |
| `2026-10-22 14:40` | 🔴 SELL (+0.17$) | `AAPL` | $10.17 | $346.52 | AAPL rsi_1h has surpassed 72 (currently 73.4) with a positive return of +1.73%, satisfying... |
| `2026-10-21 12:01` | 🟢 BUY | `MSFT` | $7.00 | $530.45 | MSFT is in a confirmed uptrend above its SMA20. The 1-hour RSI is at 36.7 (above the 32 th... |
| `2026-10-21 10:10` | 🔴 SELL (+0.12$) | `ETH-USD` | $10.07 | $2481.87 | ETH-USD rsi_1h has surpassed 72 (currently 73.7) with a positive return of +1.21%, satisfy... |

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
