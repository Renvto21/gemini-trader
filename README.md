# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-22 11:20:46`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.20 USD** | **$17.03 USD** | **$39.22 USD** | 🔴 **-1.94%** ($-0.78) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $344.59 | $10.12 | 📈 +1.16% | 1d 23h |
| `MSFT` | 0.013196 | $530.45 | $523.75 | $6.91 | 📉 -1.26% | 23h 19m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market is experiencing a downward correction, with major indices and equities like QQQ, SPY, NVDA, and MSFT trading below their respective SMA20 lines. MSFT has dipped into negative territory (-1.26%), approaching our strict stop-loss threshold near -2.0%. AAPL remains resilient in a confirmed uptrend (above SMA20) with a positive PnL of +1.16% and a 1h RSI of 59.1, nearing our target profit window. Crypto assets are mostly in bearish trends or lack confirmed 1h green reversal candles."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in a confirmed uptrend above SMA20 with a positive return (+1.16%). Following equity holding patience rules, we hold position to allow it to reach the target profit window.
- **[HOLD] MSFT** (Confidence: 80%): MSFT is currently experiencing a pullback (-1.26%) but has not breached the hard stop-loss threshold (-1.8% to -2.0%). Adhering to equity holding patience rules, we give the stock time to play out unless stop-loss is hit.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL in an active uptrend toward the profit target of +3.0% to +5.0% or until 1h RSI exceeds 72. Monitoring MSFT closely as it trades down (-1.26%); if it hits the strict stop-loss threshold of -1.8% to -2.0% ($519.84), it will be cut immediately. Maintaining cash reserves ($22.20 USD) and refraining from new equity purchases until assets regain their SMA20 uptrend status and satisfy reversal trigger rules."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **83** | 🎯 **44.6%** (37W / 31L / 15BE) | 🔴 **$-0.67 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-21 12:01` | 🟢 BUY | `MSFT` | $7.00 | $530.45 | MSFT is in a confirmed uptrend above its SMA20. The 1-hour RSI is at 36.7 (above the 32 th... |
| `2026-10-21 10:10` | 🔴 SELL (+0.12$) | `ETH-USD` | $10.07 | $2481.87 | ETH-USD rsi_1h has surpassed 72 (currently 73.7) with a positive return of +1.21%, satisfy... |
| `2026-10-20 13:51` | 🟢 BUY | `ETH-USD` | $9.95 | $2452.17 | ETH-USD muestra un excelente impulso de corto plazo con change_1h_pct positivo (+0.55%) y ... |
| `2026-10-20 13:51` | 🔴 SELL (-0.05$) | `GLD` | $9.95 | $377.90 | GLD se encuentra estancado con un rendimiento ligeramente negativo (-0.47%) y un rsi_1h de... |
| `2026-10-20 12:01` | 🟢 BUY | `GLD` | $10.00 | $379.70 | GLD presenta un RSI de 1 hora en 31.4, acercándose a la zona ideal de sobreventa para acti... |

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
