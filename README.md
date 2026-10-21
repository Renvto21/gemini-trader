# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-20 21:20:40`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$20.01 USD** | **$39.14 USD** | 🔴 **-2.15%** ($-0.86) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $342.94 | $10.07 | 📈 +0.68% | 9h 19m |
| `ETH-USD` | 0.004058 | $2452.17 | $2451.42 | $9.95 | 📉 -0.03% | 7h 29m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The portfolio currently holds AAPL and ETH-USD. Wall Street equities are closed (market_status 'CERRADO'), meaning no action can be taken on stocks like AAPL, which continues to hold above its SMA20 in an uptrend with a positive overall posture. Cryptocurrencies remain active 24/7. ETH-USD is currently trading slightly below entry (-0.03%), but still within normal holding fluctuations and far from the strict -1.8% stop-loss threshold. Although ETH-USD is currently below its daily SMA20, anti-correlation constraints prevent opening duplicate crypto exposure, and patience is warranted. No take-profit targets (+3.0% to +5.0%) have been reached yet."

**Cycle Actions:**
- **[HOLD] ETH-USD** (Confidence: 85%): ETH-USD is holding near our entry price (-0.03% PnL), well above the stop-loss threshold (-1.8%). It has not yet achieved our take-profit target (+3.0% to +5.0%). We maintain patience and let the trade develop.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing positions AAPL and ETH-USD. Monitor ETH-USD for progression toward our +3.0% to +5.0% take-profit target while respecting the hard -1.8% stop-loss limit. Keep AAPL untouched during market closure as it remains in an uptrend above SMA20. Avoid opening any additional crypto or equity positions until current holdings are resolved or clear pullback triggers occur in active uptrend assets."
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
