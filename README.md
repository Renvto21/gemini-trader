# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-21 11:31:03`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$29.20 USD** | **$9.99 USD** | **$39.18 USD** | 🔴 **-2.04%** ($-0.82) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $340.21 | $9.99 | 📉 -0.13% | 23h 29m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Market conditions show mixed trends across equities and crypto. AAPL remains in a confirmed uptrend (above SMA20) and is held patiently in accordance with equity holding rules despite flat short-term performance (-0.13%). Other major indices and equities like NVDA, QQQ, SPY, and GLD are currently trading below their SMA20, signaling bearish trends. In crypto, BTC-USD is in an uptrend (above SMA20) but currently overbought with an RSI_1h of 75.2, making it ineligible for entry until a proper pullback occurs. ETH-USD and SOL-USD are below their SMA20 lines. Cash reserves are robust at $29.20 USD, maintaining ample liquidity."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 80%): AAPL is trading above its SMA20 in a confirmed uptrend with a minor unrealized loss of -0.13%. Following equity holding patience rules, we maintain the position and give it time to play out without premature rotation.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "AAPL is maintained patiently as per equity holding rules; we will monitor its stop-loss at -2.0% and take profit at +3.0% to +5.0%. BTC-USD is above SMA20 but overbought (RSI_1h > 72); we will wait for a healthy pullback to a neutral RSI_1h range (>= 32) accompanied by a confirmed green 1-hour candle before entering. Anti-correlation constraint restricts us to holding only one crypto position at a time."
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
