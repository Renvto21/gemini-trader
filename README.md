# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-21 10:31:11`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$29.20 USD** | **$9.97 USD** | **$39.16 USD** | 🔴 **-2.10%** ($-0.84) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $339.49 | $9.97 | 📉 -0.34% | 22h 29m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market shows mixed signals with several major equities and crypto assets below their SMA20 trend lines, classified as bearish or consolidating. AAPL remains held patiently in line with equity holding rules despite a minor current pullback, as it is in an uptrend above SMA20. In the crypto sector, BTC-USD is in an uptrend (above SMA20) with a 1-hour RSI at 68.3 and a positive 1-hour change (+0.10%), but we are waiting for a deeper dip into a healthier RSI range (35-50) before initiating an entry, adhering strictly to our pullback and risk-management principles. Since we currently hold an equity position (AAPL), and market hours are open for equities, we maintain our position and cash reserves."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is maintaining its position within normal intraday fluctuation ranges while sitting above the SMA20 uptrend line. Complying with equity holding patience rules, we hold the position without rotation, closely monitoring the stop-loss level.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "AAPL is held patiently as per equity holding rules; current PnL is slightly negative (-0.34%) but well within acceptable boundaries above our -1.8% to -2.0% stop-loss threshold. BTC-USD remains on watch as the only crypto asset in an uptrend (above SMA20), but current rsi_1h is elevated at 68.3. We will wait for a healthier pullback into the 35-50 RSI zone with a confirmed green 1-hour candle before deploying capital into crypto."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **83** | 🎯 **44.6%** (37W / 31L / 15BE) | 🔴 **$-0.67 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-21 10:10` | 🔴 SELL (+0.12$) | `ETH-USD` | $10.07 | $2481.87 | ETH-USD rsi_1h has surpassed 72 (currently 73.7) with a positive return of +1.21%, satisfy... |
| `2026-10-20 13:51` | 🟢 BUY | `ETH-USD` | $9.95 | $2452.17 | ETH-USD muestra un excelente impulso de corto plazo con change_1h_pct positivo (+0.55%) y ... |
| `2026-10-20 13:51` | 🔴 SELL (-0.05$) | `GLD` | $9.95 | $377.90 | GLD se encuentra estancado con un rendimiento ligeramente negativo (-0.47%) y un rsi_1h de... |
| `2026-10-20 12:01` | 🟢 BUY | `GLD` | $10.00 | $379.70 | GLD presenta un RSI de 1 hora en 31.4, acercándose a la zona ideal de sobreventa para acti... |
| `2026-10-20 12:01` | 🟢 BUY | `AAPL` | $10.00 | $340.64 | AAPL se encuentra en tendencia alcista diaria con un RSI de 1 hora en 33.1 (cercano a sobr... |

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
