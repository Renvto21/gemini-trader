# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-26 10:30:49`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.25 USD** | **$6.94 USD** | **$39.19 USD** | 🔴 **-2.02%** ($-0.81) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $344.33 | $6.94 | 📉 -0.82% | 2d 20h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market continues to exhibit mixed conditions with major indices like SPY, QQQ, and crypto assets remaining mostly in downtrends below their SMA20. However, AAPL and MSFT maintain confirmed uptrends above their SMA20. AAPL is currently experiencing a minor pullback with a 1-hour change of -0.92%, but it remains well above our stop-loss threshold of -1.8% to -2.0% (current PnL is -0.82%). Following our quantitative rules for equity holding patience and trend-following, we will hold AAPL rather than panicking over short-term noise."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in a confirmed uptrend above its SMA20. Current PnL is -0.82%, well within our risk limits and far from the -1.8% stop-loss threshold. Sticking to equity holding patience rules.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain the current long position in AAPL patiently as it remains in an uptrend above the SMA20. Monitor AAPL for take-profit opportunities (+3.0% to +5.0% gains or 1-hour RSI > 72 with profit >= +2.5%) and strictly enforce the stop-loss at -1.8% to -2.0%. Keep holding cash reserves ($32.25 USD) and avoid opening new positions until clear reversal confirmations or better pullback entries emerge."
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
