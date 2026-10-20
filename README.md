# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-20 18:40:48`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.90 USD** | **$39.02 USD** | 🔴 **-2.45%** ($-0.98) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $339.50 | $9.97 | 📉 -0.33% | 6h 39m |
| `ETH-USD` | 0.004058 | $2452.17 | $2447.27 | $9.93 | 📉 -0.20% | 4h 49m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The market shows mixed conditions with most major equity indices and crypto assets currently trading below their SMA20, indicating a prevailing cautious or bearish short-term structure. AAPL remains an exception among equities as it is in an uptrend (above SMA20). Wall Street markets are closed (CERRADO), meaning no actions can be taken on stocks like AAPL until the next open. Crypto markets are open (24/7), but ETH-USD is currently below its SMA20, though it is holding steady with minor losses. We maintain equity holding patience for AAPL and continue monitoring ETH-USD for a potential take-profit target or stop-loss trigger according to strict risk management rules."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): AAPL is in an uptrend (above SMA20) and market status is CERRADO. Following equity holding patience, the position should be maintained while giving it time to develop.
- **[HOLD] ETH-USD** (Confidence: 100%): ETH-USD is currently within normal drawdown limits (-0.20%) well above the -1.8% to -2.0% stop-loss threshold. We hold to let the trade play out towards the +3.0% to +5.0% profit target.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain AAPL and ETH-USD positions. AAPL is in a confirmed uptrend (above SMA20) and requires patience despite flat performance. ETH-USD is currently below SMA20; monitor for a take-profit target between +3.0% and +5.0% or if rsi_1h surpasses 72, while respecting the hard stop-loss at -1.8% to -2.0%. No new entries are warranted at this moment due to the single crypto limit and closed market status for equities."
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
