# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-21 08:10:44`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.95 USD** | **$39.07 USD** | 🔴 **-2.31%** ($-0.93) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $339.50 | $9.97 | 📉 -0.33% | 20h 9m |
| `ETH-USD` | 0.004058 | $2452.17 | $2460.37 | $9.98 | 📈 +0.33% | 18h 19m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Wall Street equities (AAPL, NVDA, MSFT, SPY, QQQ, GLD) are currently closed with frozen prices. Market status for traditional assets restricts any execution. In crypto markets, ETH-USD is holding a mild positive return (+0.33%) with an RSI of 54.6, remaining below its SMA20 trend filter. AAPL is currently in an uptrend (above SMA20) and is holding steady within our equity patience rules despite minor negative daily change."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): AAPL is an equity asset currently in a closed market state. Adhering to the equity holding patience rule, we maintain the position as it remains above its SMA20 trend line.
- **[HOLD] ETH-USD** (Confidence: 100%): ETH-USD is currently showing positive performance (+0.33%) and has not reached our take-profit target (+3.0% to +5.0%) or stop-loss threshold (-1.8%). We hold to let the winner run.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing positions in AAPL and ETH-USD. AAPL is protected under equity patience guidelines while above its SMA20. ETH-USD is tracking towards our +3.0% to +5.0% take-profit target or stop-loss protection at -1.8%. Anti-correlation rules prevent opening additional crypto positions. We will monitor BTC-USD and equities upon market reopen."
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
