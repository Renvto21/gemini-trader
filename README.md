# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-21 14:30:45`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.20 USD** | **$17.13 USD** | **$39.33 USD** | 🔴 **-1.68%** ($-0.67) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $344.27 | $10.11 | 📈 +1.07% | 1d 2h |
| `MSFT` | 0.013196 | $530.45 | $532.48 | $7.03 | 📈 +0.38% | 2h 29m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The portfolio currently holds two stable equity positions, AAPL and MSFT, both operating in confirmed uptrends above their respective SMA20 thresholds. AAPL shows a healthy +1.07% return after a day of holding, while MSFT shows a modest +0.38% gain. In the broader market, equities remain mostly open with neutral to mild positive moves. Crypto assets like BTC-USD, ETH-USD, and SOL-USD are exhibiting strong 24h performance, but their 1h RSI levels remain extremely overextended above 80, violating our pullback entry triggers (rsi_1h >= 32 and <= 65/70). Consequently, staying patient with current equity holdings and keeping cash reserves untouched is the optimal risk-managed approach."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in a confirmed uptrend above SMA20, showing a steady positive return (+1.07%). Per equity holding patience rules, positions should not be sold prematurely when performing stably and below take-profit targets.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain current equity positions (AAPL and MSFT) patiently in accordance with equity holding guidelines, monitoring stop-losses closely at -1.8% to -2.0% and aiming for +3.5% take-profit targets. Keep crypto sidelined due to overextended 1H RSI readings above 80 across all major tokens. Wait for a healthy pullback to a moderate RSI level paired with positive 1H price action before deploying capital into any single crypto asset."
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
