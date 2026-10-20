# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-20 18:50:50`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.91 USD** | **$39.03 USD** | 🔴 **-2.42%** ($-0.97) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $339.50 | $9.97 | 📉 -0.33% | 6h 49m |
| `ETH-USD` | 0.004058 | $2452.17 | $2449.56 | $9.94 | 📉 -0.11% | 4h 59m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The traditional equity markets are currently closed with prices frozen, while cryptocurrencies remain open 24/7. AAPL is holding steady in a confirmed uptrend (above SMA20) with a minor negative daily return, requiring patience as per equity holding rules. ETH-USD is currently open and held in the portfolio, showing positive 24-hour momentum (+1.86%) although trading below its SMA20. Other crypto assets such as BTC-USD and SOL-USD also trade below their SMA20 trends. Given the anti-correlation constraint allowing only one crypto position, and the fact that equity markets are closed, no new trades are warranted during this cycle."

**Cycle Actions:**
- *No changes this cycle (HOLD)*

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing positions in AAPL and ETH-USD. AAPL remains an equity holding showing stability above SMA20; maintain patience and let the trade play out. ETH-USD is currently held under the single crypto constraint; monitor for a take-profit target between +3.0% and +5.0% or an RSI(1h) exceeding 72, while strictly enforcing the stop-loss limit between -1.8% and -2.0%. Do not open new crypto positions."
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
