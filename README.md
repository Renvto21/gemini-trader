# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-21 14:50:52`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.20 USD** | **$17.14 USD** | **$39.34 USD** | 🔴 **-1.65%** ($-0.66) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $344.67 | $10.12 | 📈 +1.18% | 1d 2h |
| `MSFT` | 0.013196 | $530.45 | $532.47 | $7.03 | 📈 +0.38% | 2h 49m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The current market environment shows equity holdings AAPL and MSFT comfortably holding above their SMA20 uptrends with positive performance (+1.18% and +0.38% respectively). Both positions are well within our holding guidelines and far from stop-loss or take-profit thresholds. In the crypto sector, BTC-USD is in an uptrend above SMA20, but its 1-hour RSI is extremely overextended at 91.6, preventing any entry under our pullback and trend-filtering rules. Other crypto assets like ETH-USD and SOL-USD are currently trading below their SMA20 (downtrend). Overall macro sentiment calls for patient capital preservation and holding existing winning equity positions while waiting for healthier pullbacks in crypto."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is in a confirmed uptrend above SMA20 with a solid PnL of +1.18%. Following equity holding patience guidelines, we hold the position as it has not reached our +3.0% to +5.0% take-profit target nor hit stop-loss levels.
- **[HOLD] MSFT** (Confidence: 90%): MSFT remains above its SMA20 in a confirmed uptrend with a positive return of +0.38%. Adhering to equity holding rules, we continue to hold and let the stock develop over the next 24-48 hours.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain current equity positions in AAPL and MSFT patiently according to holding rules, monitoring stop-losses at -1.8% to -2.0% and take-profit targets at +3.0% to +5.0%. Keep crypto sidelined due to overextended 1h RSI levels above 80. Wait for a meaningful correction where 1h RSI moderates to >= 32 with a positive 1-hour candle before entering any new crypto asset."
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
