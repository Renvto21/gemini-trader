# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-21 13:40:41`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.20 USD** | **$17.12 USD** | **$39.32 USD** | 🔴 **-1.70%** ($-0.68) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $343.93 | $10.10 | 📈 +0.97% | 1d 1h |
| `MSFT` | 0.013196 | $530.45 | $532.46 | $7.03 | 📈 +0.38% | 1h 39m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Market conditions show continued stability across equity holdings AAPL and MSFT, both maintaining positive momentum in confirmed uptrends above their SMA20. In the crypto sector, BTC-USD is in an uptrend above its SMA20 but features an extremely high 1-hour RSI of 89.0, signaling overbought conditions and ruling out immediate entry until a healthy pullback occurs. Cash reserves remain solid at $22.20 USD, allowing for patience while we hold our current positions toward our target asymmetric risk/reward levels."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in a confirmed uptrend above its SMA20 with a positive daily and 1-hour performance. Per equity holding rules, we maintain patience and allow the position time to develop toward our take-profit target.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Continue holding AAPL and MSFT equity positions patiently, letting them advance toward the +3.0% to +5.0% take-profit target while enforcing the -1.8% to -2.0% stop-loss limits. Keep crypto sidelined until BTC-USD or another qualifying asset experiences a healthy pullback to neutral RSI levels (between 32 and 65) while staying above its SMA20 with a confirmed positive 1-hour reversal candle."
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
