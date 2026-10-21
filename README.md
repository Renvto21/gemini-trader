# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-21 09:00:51`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.97 USD** | **$39.09 USD** | 🔴 **-2.27%** ($-0.91) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $339.50 | $9.97 | 📉 -0.33% | 20h 59m |
| `ETH-USD` | 0.004058 | $2452.17 | $2464.35 | $10.00 | 📈 +0.50% | 19h 9m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The traditional equity markets are currently closed (CERRADO), meaning no stock or ETF positions can be modified according to protocol. In the crypto sector, ETH-USD is held in a minor profit (+0.5%), but its trend is classified as bearish below SMA20. AAPL is held patiently in line with equity holding patience rules, showing a minor unrealized loss of -0.33% while above its SMA20 trend line. No new crypto positions can be opened due to the anti-correlation constraint (MAX 1 CRYPTO POSITION) and lack of bullish trend / confirmation triggers."

**Cycle Actions:**
- **[HOLD] ETH-USD** (Confidence: 80%): ETH-USD is currently showing positive performance (+0.5%) but hasn't reached the take-profit target of +3.0% to +5.0% or the stop-loss threshold. Holding position.
- **[HOLD] AAPL** (Confidence: 80%): AAPL is an equity position with market currently closed, and equity holding patience rules dictate giving stocks time to play out unless stop-loss is hit. Holding position.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing AAPL equity position and ETH-USD crypto position. Monitor ETH-USD for take-profit target (+3.0% to +5.0%) or stop-loss limit (-1.8% to -2.0%). Hold off on new asset acquisitions until market conditions and trend filters align with strict rules."
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
