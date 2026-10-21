# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-21 06:50:42`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.94 USD** | **$39.06 USD** | 🔴 **-2.34%** ($-0.94) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $339.50 | $9.97 | 📉 -0.33% | 18h 49m |
| `ETH-USD` | 0.004058 | $2452.17 | $2457.27 | $9.97 | 📈 +0.21% | 16h 59m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Wall Street equities remain closed with frozen prices, keeping our AAPL position stable with minimal movement. In crypto markets, ETH-USD shows a slight positive PnL (+0.21%) and steady upward momentum with an hourly RSI of 64.9, though it is currently classified under a bearish daily trend relative to the SMA20. BTC-USD has crossed into a bullish trend above the SMA20 with an hourly RSI of 72.8. However, due to anti-correlation constraints restricting us to a single crypto position and the rule requiring us to hold positions until take-profit (+3.0% to +5.0%) or stop-loss limits (-1.8% to -2.0%) are reached, ETH-USD is held. Equity patience is applied to AAPL as it has only been held for ~18 hours."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): Adhering to equity holding patience. The position is stable (-0.33%) and markets are closed; holding until structural changes or stop-loss thresholds are reached.
- **[HOLD] ETH-USD** (Confidence: 90%): Position is in slight profit (+0.21%). Waiting for the take-profit target range of +3.0% to +5.0% while keeping risk managed under the -1.8% stop-loss threshold.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain current holdings AAPL and ETH-USD. Monitor ETH-USD for a take-profit target between +3.0% and +5.0% or a stop-loss if it drops past -1.8%. Respect equity holding patience for AAPL while markets remain closed. Preserve cash reserves above $4.00 USD and wait for high-quality pullbacks in confirmed uptrend assets once markets reopen."
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
