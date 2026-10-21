# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-21 04:40:53`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.90 USD** | **$39.02 USD** | 🔴 **-2.44%** ($-0.98) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $339.50 | $9.97 | 📉 -0.33% | 16h 39m |
| `ETH-USD` | 0.004058 | $2452.17 | $2448.00 | $9.93 | 📉 -0.17% | 14h 49m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The portfolio currently holds two assets: AAPL (equity, market closed) and ETH-USD (crypto, market open 24/7). AAPL remains in a confirmed uptrend above the SMA20 with minor short-term fluctuations, and per equity holding patience rules, it should be given time to develop despite being flat. ETH-USD is slightly down by -0.17%, remaining well above our -1.8% stop-loss threshold. Several potential equities like MSFT are showing positive trends above the SMA20, but because Wall Street markets are currently closed, no new equity trades can be executed. Crypto assets generally reflect bearish trends relative to their SMA20, restricting new crypto entries."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 80%): AAPL is in an established uptrend above the SMA20 and has been held for less than 24 hours. Per equity holding patience rules, flat periods are normal and positions should not be prematurely rotated.
- **[HOLD] ETH-USD** (Confidence: 80%): ETH-USD is currently down only -0.17%, well above our -1.8% stop-loss threshold. We are letting the trade play out towards our +3.0% to +5.0% take-profit target.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain positions in AAPL and ETH-USD. Monitor ETH-USD for a continuation towards the +3.0% to +5.0% take-profit target or exit if it breaches the -1.8% stop-loss threshold. Hold AAPL patiently through its consolidation phase above SMA20. Keep cash reserves intact until market hours open for equities or a high-probability pullback setup triggers in crypto."
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
