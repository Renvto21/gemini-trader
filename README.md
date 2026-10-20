# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-20 19:30:42`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.93 USD** | **$39.06 USD** | 🔴 **-2.35%** ($-0.94) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $339.50 | $9.97 | 📉 -0.33% | 7h 29m |
| `ETH-USD` | 0.004058 | $2452.17 | $2456.49 | $9.97 | 📈 +0.18% | 5h 39m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Wall Street equities (AAPL, SPY, QQQ, NVDA, MSFT, GLD) are currently closed, with market status showing CERRADO. Therefore, no equity transactions can be executed per operational rules. In the crypto sector (ABIERTO 24/7), ETH-USD is holding a small positive gain (+0.18%, current price 2456.49) with an hourly RSI approaching overbought levels (71.1). However, the take-profit target of +3.0% to +5.0% has not yet been reached, and holding time is still short. AAPL remains closed and stable with a minor loss (-0.33%), which should be held per equity patience rules. No action is required as we wait for the target profit on ETH-USD and market reopening for equities."

**Cycle Actions:**
- **[HOLD] ETH-USD** (Confidence: 85%): ETH-USD is currently showing positive performance (+0.18%) with an RSI(1h) at 71.1. It has not yet reached the targeted +3.0% to +5.0% profit threshold or an RSI > 72 to trigger an optimal take-profit execution. Holding steady.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing positions in AAPL and ETH-USD. Monitor ETH-USD closely for an RSI(1h) > 72 or a profit target reaching +3.0% to +5.0% to lock in gains. Retain AAPL as it stays above the SMA20 trend, respecting equity holding patience. Avoid trading closed assets and maintain cash reserves above $4.00 USD."
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
