# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-21 02:50:41`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.87 USD** | **$38.99 USD** | 🔴 **-2.52%** ($-1.01) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $339.50 | $9.97 | 📉 -0.33% | 14h 49m |
| `ETH-USD` | 0.004058 | $2452.17 | $2440.17 | $9.90 | 📉 -0.49% | 12h 59m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The traditional equity markets are currently closed (CERRADO), and major indices like SPY, QQQ, and NVDA remain below their SMA20, indicating cautious or bearish technical conditions. AAPL remains above its SMA20 in an uptrend and is currently held in our portfolio. In crypto markets (ABIERTO 24/7), ETH-USD is experiencing slight short-term consolidation with a negative 1-hour change (-0.08%), though it is currently held within our maximum 1-crypto position limit. Overall, patience is required as equity positions must be given time to play out and crypto positions are monitored against strict stop-loss and take-profit boundaries."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): AAPL is in a confirmed uptrend above its SMA20 and is currently exhibiting normal minor fluctuations. Per equity holding patience rules, we do not sell or rotate based on flat short-term performance.
- **[HOLD] ETH-USD** (Confidence: 100%): ETH-USD is currently held within our strict anti-correlation limit (max 1 crypto position). It has not hit the take-profit target (+3.0% to +5.0%) or the stop-loss threshold (-2.0%), so we let the position run.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain current positions in AAPL and ETH-USD. Monitor ETH-USD for a take-profit target between +3.0% and +5.0%, or cut if it triggers the -2.0% stop-loss threshold. Do not open additional crypto positions due to the max 1 crypto position constraint. Keep cash reserves secure at $19.12 and wait for market hours to open for equities or clearer pullback signals."
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
