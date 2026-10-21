# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-21 00:00:49`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.89 USD** | **$39.01 USD** | 🔴 **-2.47%** ($-0.99) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $339.50 | $9.97 | 📉 -0.33% | 11h 59m |
| `ETH-USD` | 0.004058 | $2452.17 | $2445.05 | $9.92 | 📉 -0.29% | 10h 9m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The market is currently mixed with Wall Street assets remaining closed (market status CERRADO). Cryptocurrencies are actively trading 24/7, but most remain in a broader daily downtrend (below SMA20). AAPL is holding steady above SMA20 in an uptrend despite being closed, while ETH-USD shows minor consolidation with a slight negative 1h change (-0.04%), holding close to entry price (-0.29% PnL). No immediate stop-loss or take-profit thresholds have been triggered yet for our open positions."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 80%): AAPL is in an uptrend above SMA20 and has only been held for ~12 hours. Adhering to equity holding patience rules, we maintain the position as it is stable and market status is closed.
- **[HOLD] ETH-USD** (Confidence: 80%): ETH-USD is currently down -0.29%, well above our -1.8% to -2.0% stop-loss threshold. We wait for momentum to push towards our +3.0% to +5.0% take-profit target.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain current positions in AAPL and ETH-USD. AAPL is safely above SMA20 and requires patience during market closure. ETH-USD is in consolidation; keep monitoring for a take-profit target between +3.0% and +5.0%, or a strict stop-loss cut at -2.0%. Do not open new crypto positions due to anti-correlation and strict trend rules."
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
