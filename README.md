# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-21 02:10:41`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.90 USD** | **$39.02 USD** | 🔴 **-2.45%** ($-0.98) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $339.50 | $9.97 | 📉 -0.33% | 14h 9m |
| `ETH-USD` | 0.004058 | $2452.17 | $2446.92 | $9.93 | 📉 -0.21% | 12h 19m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Wall Street equities (AAPL, SPY, QQQ, GLD, MSFT, NVDA) are currently closed, with prices frozen. AAPL remains in an uptrend above SMA20, while MSFT also holds its bullish structure. In the crypto sector (open 24/7), ETH-USD is currently held in our portfolio but displays a bearish trend status relative to its SMA20 despite a mild positive hourly change (+0.19%). However, adhering to equity holding patience and asymmetric rules, we will hold current positions as neither have hit take-profit targets (+3% to +5%) nor stop-loss boundaries (-1.8% to -2.0%). No new crypto buys are initiated to respect the anti-correlation constraint (MAX 1 crypto position)."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in an uptrend above SMA20 and market status is closed. Adhering to the equity holding patience rule, flat or minor negative movement over short durations does not warrant a premature sale. Current PnL is minimal (-0.33%).
- **[HOLD] ETH-USD** (Confidence: 80%): ETH-USD is currently within acceptable risk boundaries with a minor PnL of -0.21%. Holding to let potential upside run toward the +3% to +5% take-profit target while respecting the strict stop-loss limit.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing positions in AAPL and ETH-USD. Monitor ETH-USD for a take-profit target between +3% and +5%, or execute stop-loss if it breaches -1.8% to -2.0%. Keep cash reserve at $19.12. When Wall Street reopens, re-evaluate MSFT and AAPL for potential trend pullback entries if conditions meet strict trend filter and reversal triggers."
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
