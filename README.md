# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-22 13:22:15`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.20 USD** | **$17.11 USD** | **$39.30 USD** | 🔴 **-1.75%** ($-0.70) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $346.05 | $10.16 | 📈 +1.59% | 2d 1h |
| `MSFT` | 0.013196 | $530.45 | $526.43 | $6.95 | 📉 -0.76% | 1d 1h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The market demonstrates overall corrective pressure across multiple asset classes with most equities and crypto assets trading below their SMA20. AAPL remains a standout showing resilience in a confirmed uptrend (above SMA20) with an hourly RSI of 68.1 and a positive return of +1.59%, approaching our take-profit window. MSFT has dipped below the SMA20 trend filter, currently showing a mild loss of -0.76%, but per our equity holding patience rule, it should be given time unless the hard stop-loss is triggered. Crypto assets (BTC-USD, ETH-USD, SOL-USD) are currently under downward pressure, and with no confirmed 1-hour positive reversal triggers meeting our strict criteria (hourly changes are negative or lack bounce confirmation), no new crypto trades are warranted."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in a confirmed uptrend above SMA20 with a positive PnL of +1.59% and approaching the take-profit threshold. Upholding equity holding patience.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Continue to hold AAPL and monitor for take-profit targets (+3.0% to +5.0% gain or rsi_1h > 72 with profit >= +2.5%). Hold MSFT patiently despite short-term weakness, keeping a strict stop-loss at -1.8% to -2.0%. Maintain cash reserves around $22.20 USD while awaiting validated pullback entry triggers in confirmed uptrend assets."
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
