# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-20 20:30:42`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.89 USD** | **$39.01 USD** | 🔴 **-2.47%** ($-0.99) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $339.50 | $9.97 | 📉 -0.33% | 8h 29m |
| `ETH-USD` | 0.004058 | $2452.17 | $2445.28 | $9.92 | 📉 -0.28% | 6h 39m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Traditional equity markets are currently closed (CERRADO), leaving active liquidity restricted to 24/7 crypto assets. Our current holdings consist of AAPL (equity) and ETH-USD (crypto). AAPL remains above the SMA20 trend filter in a confirmed bull trend and is down a minimal -0.33%, which requires patience per our equity holding rules. ETH-USD is currently experiencing a minor pullback with a negative 1-hour change (-0.34%) and is below the SMA20 trend filter. However, its losses remain well within risk parameters (-0.28%), so we will maintain it unless stop-loss limits are breached. No new buys are warranted at this moment since available crypto assets lack the necessary reversal confirmation triggers (positive 1h change while above SMA20) and equities are closed."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): AAPL is an equity position currently in an uptrend (above SMA20) with a minor drawdown (-0.33%). Equity holding rules require patience over 24-48 hour horizons unless stop-loss limits are reached.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing positions AAPL and ETH-USD without premature rotation. AAPL will be held patiently as an equity position. ETH-USD will be monitored for either a recovery towards the +3.0% to +5.0% take-profit target or a strict stop-loss departure if it approaches -1.8% to -2.0%. Keep cash reserves intact and wait for valid trend-following pullback setups on open markets."
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
