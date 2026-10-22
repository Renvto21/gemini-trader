# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-22 13:40:58`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.20 USD** | **$17.08 USD** | **$39.28 USD** | 🔴 **-1.81%** ($-0.72) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $345.70 | $10.15 | 📈 +1.49% | 2d 1h |
| `MSFT` | 0.013196 | $530.45 | $525.24 | $6.93 | 📉 -0.98% | 1d 1h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broad market is currently experiencing a pullback, with most monitored assets trading below their SMA20 lines in bearish short-term structures. AAPL remains the sole asset in a confirmed uptrend (above SMA20) with a strong daily RSI of 69.4 and a 1-hour RSI of 65.1, showing resilience despite minor hourly fluctuations. MSFT has dipped into a short-term downtrend below its SMA20 with a PnL of -0.98%, but per the equity holding patience rule and strict risk parameters, it should be held unless the hard stop-loss of -1.8% to -2.0% is breached. Crypto and alternative assets are showing weak hourly changes (negative 1-hour percentage changes) and do not satisfy the reversal confirmation trigger (change_1h_pct > 0.0), keeping us safely on the sidelines."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is maintaining a strong uptrend above its SMA20 and is approaching our profit-taking window. Sticking to equity holding patience to let winners run.
- **[HOLD] MSFT** (Confidence: 80%): MSFT is currently experiencing a mild pullback at -0.98% PnL, well within our acceptable risk threshold before hitting the hard stop-loss at -1.8% to -2.0%. Equities require time to develop.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Continue to hold AAPL and monitor for profit-taking targets (+3.0% to +5.0% gain, or rsi_1h > 72 with profit >= +2.5%). Hold MSFT patiently as equities require time to play out, strictly respecting the hard stop-loss at -1.8% to -2.0%. Maintain cash reserves above $4.00 USD and wait for validated pullback entry triggers (rsi_1h >= 32 and change_1h_pct > 0.0) in assets confirmed above their SMA20 trend."
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
