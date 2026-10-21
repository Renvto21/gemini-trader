# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-21 12:11:19`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.20 USD** | **$17.06 USD** | **$39.26 USD** | 🔴 **-1.86%** ($-0.74) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $342.85 | $10.06 | 📈 +0.65% | 1d 0h |
| `MSFT` | 0.013196 | $530.45 | $530.26 | $7.00 | 📉 -0.04% | 10m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Equities are currently open with major assets like AAPL and MSFT exhibiting solid uptrends above their SMA20. AAPL is holding steady with modest positive gains, while MSFT remains stable after its recent entry. In crypto, BTC-USD shows an uptrend above SMA20, but its 1-hour RSI is heavily overbought at 82.9, making new entries unviable due to strict reversal and overbought filtering rules. We maintain patience on existing equity holdings and keep cash reserves ready."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 80%): AAPL is in a confirmed uptrend above SMA20 with a positive PnL (+0.65%). Adhering to equity holding patience, we will let the position run towards our take-profit target of +3.0% to +5.0%.
- **[HOLD] MSFT** (Confidence: 80%): MSFT was recently opened in a confirmed uptrend. Following the rule of equity patience, we hold the position to give it time to play out without rotating prematurely.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Hold AAPL and MSFT patiently according to equity holding patience rules, tracking take-profit targets between +3.0% and +5.0% and the stop-loss circuit breaker at -2.0%. Keep crypto sidelined due to extreme 1H RSI overbought conditions despite uptrends. Do not force trades and preserve cash."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **83** | 🎯 **44.6%** (37W / 31L / 15BE) | 🔴 **$-0.67 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-21 12:01` | 🟢 BUY | `MSFT` | $7.00 | $530.45 | MSFT is in a confirmed uptrend above its SMA20. The 1-hour RSI is at 36.7 (above the 32 th... |
| `2026-10-21 10:10` | 🔴 SELL (+0.12$) | `ETH-USD` | $10.07 | $2481.87 | ETH-USD rsi_1h has surpassed 72 (currently 73.7) with a positive return of +1.21%, satisfy... |
| `2026-10-20 13:51` | 🟢 BUY | `ETH-USD` | $9.95 | $2452.17 | ETH-USD muestra un excelente impulso de corto plazo con change_1h_pct positivo (+0.55%) y ... |
| `2026-10-20 13:51` | 🔴 SELL (-0.05$) | `GLD` | $9.95 | $377.90 | GLD se encuentra estancado con un rendimiento ligeramente negativo (-0.47%) y un rsi_1h de... |
| `2026-10-20 12:01` | 🟢 BUY | `GLD` | $10.00 | $379.70 | GLD presenta un RSI de 1 hora en 31.4, acercándose a la zona ideal de sobreventa para acti... |

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
