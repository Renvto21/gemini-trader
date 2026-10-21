# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-20 22:20:46`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.98 USD** | **$39.11 USD** | 🔴 **-2.23%** ($-0.89) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $342.94 | $10.07 | 📈 +0.68% | 10h 19m |
| `ETH-USD` | 0.004058 | $2452.17 | $2443.60 | $9.92 | 📉 -0.35% | 8h 29m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market shows Wall Street equities closed for the weekend/night with mixed short-term stability. In the crypto sector, ETH-USD and BTC-USD are currently trading with minor hourly pullbacks (change_1h_pct is slightly negative), and ETH-USD remains within our open positions at a minor loss of -0.35%. AAPL is holding steady with a modest gain of +0.68%. No immediate action is required since ETH-USD has not hit our take-profit target (+3.0% to +5.0%) nor the hard stop-loss (-1.8%), and equities must be given time to play out patiently."

**Cycle Actions:**
- **[HOLD] ETH-USD** (Confidence: 85%): ETH-USD is currently down -0.35%, well within normal fluctuation and far above the -1.8% stop-loss threshold. Holding patiently for the profit target window.
- **[HOLD] AAPL** (Confidence: 90%): AAPL is in an established uptrend and shows a small gain (+0.68%). Per equity holding patience rules, equities are given time to play out without premature rotation.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Continue holding AAPL and ETH-USD. Monitor ETH-USD for a bounce above +3.0% profit or a strict stop-loss departure if it touches -1.8%. Maintain AAPL patiently as equities require holding time. Avoid opening new positions until clear trend confirmation and bullish hourly reversals occur in open market assets."
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
