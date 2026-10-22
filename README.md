# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-22 14:31:41`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.20 USD** | **$17.08 USD** | **$39.28 USD** | 🔴 **-1.81%** ($-0.72) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $346.17 | $10.16 | 📈 +1.62% | 2d 2h |
| `MSFT` | 0.013196 | $530.45 | $524.21 | $6.92 | 📉 -1.18% | 1d 2h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market is experiencing a cautious and bearish correction, with major assets like SPY, QQQ, and NVDA trading below their SMA20 trends. AAPL remains a strong outlier, maintaining its uptrend above SMA20 with 1-hour RSI reaching 72.7 and a current unrealized gain of +1.62%. MSFT has dipped slightly below its SMA20 trend line with a PnL of -1.18%, holding well above our strict -1.8% to -2.0% stop-loss threshold. Cryptocurrencies are mostly in downtrends, with BTC-USD and ETH-USD showing low 1-hour RSIs and negative 24-hour performance."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is in an established uptrend above SMA20, and its rsi_1h is currently at 72.7 with a positive return of +1.62%. We will let the winner run toward our +3.0% to +5.0% target or until reversal confirmation.
- **[HOLD] MSFT** (Confidence: 80%): MSFT is currently down -1.18%, which is well within our acceptable holding threshold before reaching the -1.8% to -2.0% stop-loss boundary. Equity patience applies.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Continue to hold AAPL and monitor its profit closely for a potential take-profit action if rsi_1h stays elevated or profit targets (+3.0% to +5.0%) are reached. Hold MSFT while respecting the hard stop-loss threshold at -1.8% to -2.0%. Do not open new crypto or stock positions until assets firmly reclaim their uptrend above SMA20 and fulfill the 1-hour reversal trigger criteria."
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
