# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-21 13:30:52`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.20 USD** | **$17.10 USD** | **$39.30 USD** | 🔴 **-1.76%** ($-0.70) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $343.49 | $10.08 | 📈 +0.84% | 1d 1h |
| `MSFT` | 0.013196 | $530.45 | $531.69 | $7.02 | 📈 +0.23% | 1h 29m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The portfolio currently holds two equity positions, AAPL and MSFT, both trending above their respective SMA20s and showing mild positive gains. Equity holding patience dictates keeping these positions open as they have not hit stop-loss levels or reached our +3.0% to +5.0% take-profit targets. In the crypto sector, BTC-USD is above its SMA20 but its 1-hour RSI is severely overbought at 88.8, and its 1-hour change is minimal (-0.18% to +0.18% oscillating), lacking a proper pullback entry configuration. Other crypto assets like ETH-USD and SOL-USD are below their SMA20s (downtrend filters block them). Market conditions remain disciplined with cash reserves intact."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 80%): AAPL is in an established uptrend above SMA20 with a current profit of +0.84%. Adhering to equity holding patience and asymmetric reward principles, we hold the position to let winners run toward our +3.0% target.
- **[HOLD] MSFT** (Confidence: 80%): MSFT is in an uptrend above SMA20 and was recently opened. In line with equity holding patience rules, we do not rotate or sell flat positions prematurely without hitting stop-losses or profit targets.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain patience with AAPL and MSFT equity positions, allowing them time to play out toward the +3.0% to +5.0% take-profit target while respecting the strict -1.8% to -2.0% stop-loss limits. Keep crypto sidelined until BTC-USD or another qualifying asset experiences a healthy pullback to neutral RSI levels (between 32 and 65) while staying above its SMA20 with a confirmed positive 1-hour reversal candle."
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
