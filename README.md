# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-20 21:10:43`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.99 USD** | **$39.12 USD** | 🔴 **-2.21%** ($-0.88) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $342.94 | $10.07 | 📈 +0.68% | 9h 9m |
| `ETH-USD` | 0.004058 | $2452.17 | $2445.96 | $9.92 | 📉 -0.25% | 7h 19m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Wall Street equities remain closed with frozen prices, keeping AAPL in a stable holding pattern above SMA20 with a slight positive PnL (+0.68%). Cryptocurrencies are trading actively 24/7. ETH-USD is currently holding our single permitted crypto slot at a minor drawdown (-0.25%), but shows healthy short-term momentum with a positive 1-hour change (+0.49%) and an hourly RSI of 64.2. Other crypto options like SOL-USD and BTC-USD also show positive momentum, but we strictly respect the anti-correlation constraint limiting us to a single crypto position. Equity holdings like AAPL will be held patiently as per the equity holding patience rule."

**Cycle Actions:**
- **[HOLD] ETH-USD** (Confidence: 85%): ETH-USD is currently active within our single allowed crypto position, showing stable 1-hour momentum (+0.49%) and healthy hourly RSI (64.2). It has not reached either our +3% take-profit goal or the -1.8% stop-loss limit, so we hold to let the trade play out.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing positions AAPL and ETH-USD. Monitor ETH-USD for progression toward our +3.0% to +5.0% take-profit target or protect capital with the strict -1.8% stop-loss threshold. Keep AAPL untouched during market closure as it maintains an uptrend above SMA20. Respect anti-correlation constraints and avoid adding further crypto assets."
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
