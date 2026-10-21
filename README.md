# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-21 06:20:43`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.95 USD** | **$39.08 USD** | 🔴 **-2.30%** ($-0.92) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $339.50 | $9.97 | 📉 -0.33% | 18h 19m |
| `ETH-USD` | 0.004058 | $2452.17 | $2461.61 | $9.99 | 📈 +0.38% | 16h 29m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The portfolio currently holds AAPL (equity) and ETH-USD (crypto). US stock markets are currently closed (CERRADO), so no actions can be taken on equities right now, and equity holding patience must be respected for AAPL. ETH-USD is in positive territory (+0.38%), though its trend remains bearish under SMA20; we hold it carefully tracking toward our +3.0% to +5.0% profit target while keeping stop-loss rules in mind. BTC-USD is the only crypto asset in a confirmed uptrend (above SMA20), but our anti-correlation constraint prevents holding multiple crypto positions simultaneously."

**Cycle Actions:**
- **[HOLD] ETH-USD** (Confidence: 80%): ETH-USD is slightly in profit (+0.38%) and holding above entry. It has not yet reached our take-profit target (+3.0% to +5.0%) nor triggered our stop-loss limit. Holding per asymmetric risk/reward guidelines.
- **[HOLD] AAPL** (Confidence: 80%): AAPL market is currently closed (CERRADO). Per equity holding patience rules, we do not rotate or sell flat positions prematurely without hitting stop-loss limits.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain current holdings AAPL and ETH-USD. ETH-USD is currently showing a mild positive PnL (+0.38%); monitor closely for either reaching the take-profit target (+3.0% to +5.0%) or cutting losses if it hits the -1.8% to -2.0% stop-loss threshold. Respect equity holding patience for AAPL while markets remain closed. Do not open new positions to preserve our minimum cash reserve."
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
