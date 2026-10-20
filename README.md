# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-20 20:51:08`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.90 USD** | **$39.02 USD** | 🔴 **-2.45%** ($-0.98) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $339.50 | $9.97 | 📉 -0.33% | 8h 49m |
| `ETH-USD` | 0.004058 | $2452.17 | $2447.08 | $9.93 | 📉 -0.21% | 7h 0m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The portfolio holds AAPL and ETH-USD. Wall Street assets such as AAPL are currently closed ('CERRADO'), and per rule requirements, closed assets cannot be traded. Crypto assets are open (24/7), but ETH-USD shows a negative 1-hour change (-0.27%) and is currently below the SMA20 trend filter. Following strict trend-following pullback and risk management rules, we hold our current positions, as they have not hit stop-loss levels (-1.8% to -2.0%) nor profit targets (+3.0% to +5.0%), and equities must be given patience."

**Cycle Actions:**
- **[HOLD] ETH-USD** (Confidence: 80%): ETH-USD is currently down slightly (-0.21%) but has not reached the strict stop-loss threshold (-1.8% to -2.0%) nor the profit target (+3.0%). Holding per capital preservation and patience guidelines.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing positions AAPL and ETH-USD. Monitor ETH-USD for upward recovery or stop-loss limits near -1.8%. Hold AAPL patiently as equity markets are closed and the asset remains in an uptrend above SMA20. Do not open new crypto positions due to anti-correlation constraints (max 1 crypto held)."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **82** | 🎯 **43.9%** (36W / 31L / 15BE) | 🔴 **$-0.79 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-20 13:51` | 🟢 BUY | `ETH-USD` | $9.95 | $2452.17 | ETH-USD muestra un excelente impulso de corto plazo con change_1h_pct positivo (+0.55%) y ... |
| `2026-10-20 13:51` | 🔴 SELL (-0.05$) | `GLD` | $9.95 | $377.90 | GLD se encuentra estancado con un rendimiento ligeramente negativo (-0.47%) y un rsi_1h de... |
| `2026-10-20 12:01` | 🟢 BUY | `GLD` | $10.00 | $379.70 | GLD presenta un RSI de 1 hora en 31.4, acercándose a la zona ideal de sobreventa para acti... |
| `2026-10-20 12:01` | 🟢 BUY | `AAPL` | $10.00 | $340.64 | AAPL se encuentra en tendencia alcista diaria con un RSI de 1 hora en 33.1 (cercano a sobr... |
| `2026-10-20 11:10` | 🔴 SELL (+0.12$) | `BTC-USD` | $8.69 | $82949.93 | BTC-USD muestra un RSI de 1 hora en 72.2 (sobrecompra) y un rendimiento positivo de +1.45%... |

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
