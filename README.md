# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-21 14:40:45`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.20 USD** | **$17.14 USD** | **$39.34 USD** | 🔴 **-1.66%** ($-0.66) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $344.47 | $10.11 | 📈 +1.12% | 1d 2h |
| `MSFT` | 0.013196 | $530.45 | $532.69 | $7.03 | 📈 +0.42% | 2h 39m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The portfolio currently holds two stable equity positions, AAPL and MSFT, both trending above their SMA20 with positive unrealized returns. AAPL is up 1.12% and MSFT is up 0.42%. Cryptocurrencies are experiencing strong upward momentum on the 24h scale, but their 1h RSI readings remain severely overextended (above 80), making them unviable for new entries under strict trend and pullback confirmation rules. SPY is approaching higher RSI levels without triggering sell conditions, while other tech and equity assets show mixed trends. We maintain patience with existing equity holdings, respecting stop-losses and letting winners run toward the +3.0% to +5.0% take-profit targets."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is in a confirmed uptrend above its SMA20, showing steady performance with an unrealized profit of +1.12%. Following equity holding patience guidelines, we hold this position as it develops toward our take-profit target.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain AAPL and MSFT positions patiently in accordance with equity holding guidelines. Monitor stop-losses strictly at -1.8% to -2.0% and watch for take-profit targets between +3.0% and +5.0%. Keep crypto sidelined due to overextended 1h RSI levels (above 80 across BTC, ETH, and SOL). Wait for a healthy correction to moderate RSI levels (>= 32) combined with positive 1h price action before deploying capital into any crypto asset."
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
