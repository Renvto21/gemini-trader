# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-21 03:50:43`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.86 USD** | **$38.99 USD** | 🔴 **-2.53%** ($-1.01) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $339.50 | $9.97 | 📉 -0.33% | 15h 49m |
| `ETH-USD` | 0.004058 | $2452.17 | $2438.84 | $9.90 | 📉 -0.54% | 13h 59m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The portfolio is currently holding AAPL (equity, market closed) and ETH-USD (crypto, market open). Both positions are experiencing minor unrealized losses well within acceptable stop-loss parameters (-0.33% and -0.54%, respectively). Wall Street equities are currently closed, keeping AAPL prices frozen. ETH-USD is in a minor consolidation phase with an RSI of 42.7 and a slightly positive 1-hour change, remaining above the strict -1.8% stop-loss threshold. We adhere to equity holding patience and anti-correlation constraints, avoiding any new crypto exposure while ETH-USD is active."

**Cycle Actions:**
- **[HOLD] ETH-USD** (Confidence: 80%): ETH-USD is currently down -0.54%, far above the -1.8% stop-loss limit. The position needs time to develop toward our +3.0% to +5.0% take-profit target without premature selling.
- **[HOLD] AAPL** (Confidence: 80%): AAPL market is currently closed. Following equity holding patience rules, we maintain the position as it is only down -0.33% and well above the stop-loss threshold.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain current holdings in AAPL and ETH-USD. Monitor ETH-USD for a take-profit target between +3.0% and +5.0% or a stop-loss if it drops past -1.8%. Continue holding AAPL patiently during the equity market closure. Keep at least $4.00 in cash reserve and avoid opening duplicate crypto exposures."
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
