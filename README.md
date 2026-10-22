# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-21 21:30:49`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.20 USD** | **$16.99 USD** | **$39.18 USD** | 🔴 **-2.05%** ($-0.82) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $339.50 | $9.97 | 📉 -0.33% | 1d 9h |
| `MSFT` | 0.013196 | $530.45 | $531.87 | $7.02 | 📈 +0.27% | 9h 29m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The US equity markets are currently closed (CERRADO), and equity positions AAPL and MSFT remain active and stable with low holding durations, adhering to the patience rule. Among crypto assets open 24/7, BTC-USD is in an uptrend above SMA20, but its current 1-hour candle is negative (change_1h_pct = -0.71%), failing the reversal confirmation trigger. ETH-USD, SOL-USD, and major equity indices are currently in downtrends or lacking active entry triggers."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): AAPL is an equity position currently held during closed market hours. Adhering to the equity holding patience rule, it should not be rotated or sold prematurely while flat or slightly down, keeping its stop-loss intact.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing equity positions AAPL and MSFT targeting +3.0% to +5.0% gains while keeping strict stop-losses at -2.0%. For BTC-USD, wait for a confirmed positive 1-hour candle (change_1h_pct > 0.0 with rsi_1h >= 32) before considering a pullback entry. Keep cash reserves above $4.00 USD intact."
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
