# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-21 08:00:53`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.93 USD** | **$39.05 USD** | 🔴 **-2.37%** ($-0.95) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $339.50 | $9.97 | 📉 -0.33% | 19h 59m |
| `ETH-USD` | 0.004058 | $2452.17 | $2454.70 | $9.96 | 📈 +0.10% | 18h 9m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Wall Street equities (AAPL, MSFT, NVDA, QQQ, SPY, GLD) are currently closed for the weekend/market hours, meaning prices are frozen and no execution is allowed on stocks/ETFs per operational rules. In the crypto markets (open 24/7), ETH-USD is held in our portfolio but currently trades slightly below its SMA20 trend filter, showing a moderate recovery posture with positive 1h changes. BTC-USD is above its SMA20 in a confirmed uptrend, but our anti-correlation constraint limits us to a single crypto asset."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): Asset market is closed and equity holding patience dictates maintaining positions that are not violating stop-loss limits.
- **[HOLD] ETH-USD** (Confidence: 100%): Holding current crypto position as it works towards the take-profit target, respecting anti-correlation limits.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing positions in AAPL and ETH-USD. AAPL remains protected under equity patience guidelines while above its SMA20. ETH-USD is monitored closely for our take-profit target between +3.0% and +5.0% or a stop-loss protection at -1.8%. We adhere strictly to the anti-correlation rule by avoiding any additional crypto purchases."
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
