# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-21 02:00:48`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.88 USD** | **$39.00 USD** | 🔴 **-2.49%** ($-1.00) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $339.50 | $9.97 | 📉 -0.33% | 13h 59m |
| `ETH-USD` | 0.004058 | $2452.17 | $2442.58 | $9.91 | 📉 -0.39% | 12h 9m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The portfolio holds AAPL and ETH-USD. Wall Street markets are currently closed, keeping equity prices frozen. AAPL remains above its SMA20 in a confirmed uptrend with a minor unrealized loss (-0.33%), complying with equity holding patience guidelines. ETH-USD is open, showing a slight positive change (+0.02%) and holding above our stop-loss threshold while anti-correlation constraints are respected since it is our only crypto position. Other crypto assets like BTC-USD and SOL-USD are also trading, but we maintain our position in ETH-USD."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 80%): AAPL is in a confirmed uptrend (above SMA20) and complies with equity holding patience guidelines, currently experiencing a minor flat pullback (-0.33%) well above our stop-loss limits.
- **[HOLD] ETH-USD** (Confidence: 80%): ETH-USD is maintaining stability within acceptable loss parameters (-0.39%), respecting anti-correlation constraints as our single crypto holding while waiting for the target upside of +3.0% to +5.0%.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing positions in AAPL and ETH-USD. Monitor ETH-USD for a potential take-profit target between +3% and +5%, or cut losses strictly if it breaches the -1.8% to -2.0% stop-loss boundary. Keep cash reserve at $19.12. When Wall Street reopens, re-evaluate MSFT for potential trend pullback entry."
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
