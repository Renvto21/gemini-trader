# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-22 12:20:48`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.20 USD** | **$17.06 USD** | **$39.25 USD** | 🔴 **-1.86%** ($-0.75) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $344.77 | $10.12 | 📈 +1.21% | 2d 0h |
| `MSFT` | 0.013196 | $530.45 | $525.72 | $6.94 | 📉 -0.89% | 1d 0h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The market is exhibiting broad defensive conditions with most assets trading below their SMA20, signaling a short-term bearish trend across equities and crypto. AAPL remains an exception, holding an uptrend above its SMA20 with positive momentum. Our current open positions include AAPL (+1.21%) and MSFT (-0.89%), which is experiencing slight downward pressure but remains well above our -2.0% stop-loss threshold. Patience is maintained for equities in line with the equity holding patience rule."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 80%): AAPL is in a confirmed uptrend above SMA20 with positive returns (+1.21%). Adhering to the equity holding patience rule to let winners run toward our +3.0% to +5.0% profit target.
- **[HOLD] MSFT** (Confidence: 70%): MSFT is currently down -0.89%, comfortably above our strict stop-loss limit of -2.0%. Giving the position time to play out per equity holding patience guidelines.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL and MSFT positions. AAPL is progressing well toward take-profit targets (+3.0% to +5.0%), while MSFT is monitored for stop-loss compliance (-1.8% to -2.0%). No new crypto or equity entries are triggered as market-wide trends are predominantly bearish and fail pullback criteria."
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
