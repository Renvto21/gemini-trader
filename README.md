# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-20 21:40:37`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$20.01 USD** | **$39.14 USD** | 🔴 **-2.16%** ($-0.86) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $342.94 | $10.07 | 📈 +0.68% | 9h 38m |
| `ETH-USD` | 0.004058 | $2452.17 | $2450.94 | $9.95 | 📉 -0.05% | 7h 49m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market shows Wall Street equities closed for the session with mixed sentiments. Major indices and stocks like AAPL and MSFT remain stable. AAPL continues to hold above the SMA20 trend line, fulfilling our equity patience rule. In the crypto sector, ETH-USD is open 24/7, hovering near our entry price with a minor loss (-0.05%), showing a positive 1-hour change (+0.69%) and healthy 1-hour RSI (65.2). Since ETH-USD has not hit our target profit (+3.0% to +5.0%) nor the hard stop-loss (-1.8%), and following the anti-correlation constraint and equity holding patience, we maintain our current holdings."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in an established uptrend above SMA20 and is currently flat with a small positive gain (+0.68%). Adhering to the equity holding patience rule, we will give the stock time to develop without premature rotation.
- **[HOLD] ETH-USD** (Confidence: 80%): ETH-USD is holding stable near entry price (-0.05% PnL) with positive short-term momentum. It has not reached our asymmetric reward target (+3.0% to +5.0%) or triggered the -1.8% stop-loss threshold. We maintain the position.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing positions AAPL and ETH-USD. Monitor ETH-USD for a take-profit target of +3.0% to +5.0% or until RSI 1H exceeds 72, while strictly respecting the hard stop-loss at -1.8%. Keep AAPL untouched as it is above the SMA20 trend line and gives time to play out per equity patience rules. Refrain from opening new crypto trades due to the anti-correlation constraint holding max 1 crypto position."
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
