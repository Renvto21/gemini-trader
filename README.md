# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-21 09:50:37`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.98 USD** | **$39.10 USD** | 🔴 **-2.24%** ($-0.90) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $339.50 | $9.97 | 📉 -0.33% | 21h 48m |
| `ETH-USD` | 0.004058 | $2452.17 | $2467.70 | $10.01 | 📈 +0.63% | 19h 59m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The market shows mixed conditions. Major equity indices and several popular ETFs are closed with prices frozen. AAPL remains in an uptrend above its SMA20 and is being held patiently according to equity holding rules. In crypto, BTC-USD is trading above its SMA20 in an uptrend, while ETH-USD is currently holding a small profit (+0.63%) but sits below the SMA20 trend filter. Given our anti-correlation constraint and holding discipline, we maintain current positions and wait for take-profit targets or stop-loss limits without forcing new trades."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): AAPL is in an uptrend above its SMA20 and follows the equity holding patience rule. It has only been held for ~22 hours and is performing stably despite minor daily fluctuations.
- **[HOLD] ETH-USD** (Confidence: 100%): ETH-USD is currently showing positive unrealized gains (+0.63%). We hold the position patiently towards our asymmetric risk/reward take-profit target of +3.0% to +5.0% while respecting the stop-loss limit at -2.0%.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing AAPL and ETH-USD positions. Wait for ETH-USD to reach our take-profit target of +3.0% to +5.0% or hit the stop-loss limit at -2.0%. Hold AAPL patiently according to equity holding rules. Do not open new crypto positions due to the anti-correlation single crypto constraint."
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
