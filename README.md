# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-20 20:40:36`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.89 USD** | **$39.01 USD** | 🔴 **-2.47%** ($-0.99) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $339.50 | $9.97 | 📉 -0.33% | 8h 38m |
| `ETH-USD` | 0.004058 | $2452.17 | $2444.73 | $9.92 | 📉 -0.30% | 6h 49m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The portfolio currently holds AAPL (equity) and ETH-USD (crypto). Wall Street markets are closed (market_status: CERRADO), meaning no actions can be executed on equities or ETFs like MSFT, SPY, GLD, AAPL, NVDA, and QQQ. Cryptocurrencies remain active 24/7. ETH-USD is currently experiencing a minor pullback (-0.3%) with a negative 1-hour percentage change (-0.37%), but it has not reached the strict stop-loss threshold of -1.8% to -2.0% nor the take-profit target of +3.0% to +5.0%. Following equity holding patience guidelines, AAPL is maintained without premature rotation. No new crypto entries are warranted as ETH-USD is already held (anti-correlation constraint) and market trends for open crypto assets do not currently present optimal breakout confirmations with positive hourly changes."

**Cycle Actions:**
- **[HOLD] ETH-USD** (Confidence: 100%): ETH-USD position is well within normal fluctuation limits (-0.30% PnL), far from the -2.0% stop-loss circuit breaker and target objectives. Holding as per equity and crypto patience rules.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing positions AAPL and ETH-USD. Monitor ETH-USD for a bounce towards the +3.0% to +5.0% profit target or a strict cut if losses approach -1.8% to -2.0%. Keep cash reserves safe and wait for market hours and robust trend pullback setups for subsequent cycles."
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
