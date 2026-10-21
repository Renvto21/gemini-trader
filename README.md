# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-21 14:10:39`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.20 USD** | **$17.14 USD** | **$39.34 USD** | 🔴 **-1.65%** ($-0.66) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $344.32 | $10.11 | 📈 +1.08% | 1d 2h |
| `MSFT` | 0.013196 | $530.45 | $533.11 | $7.04 | 📈 +0.50% | 2h 9m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The equity markets are currently open with major indices and holdings like AAPL and MSFT maintaining steady uptrends above their SMA20 lines. AAPL (+1.08%) and MSFT (+0.5%) are performing well with healthy 1h RSI levels (57.1 and 49.0 respectively), adhering to our equity holding patience rule. In the crypto sector, BTC-USD is in an uptrend above SMA20 but its 1h RSI is heavily overbought at 87.6 with a negative 1h price change (-0.12%), violating the reversal confirmation trigger for new entries. Other cryptos like ETH-USD and SOL-USD are either in downtrends or overbought. Therefore, maintaining our existing equity positions and holding cash is the optimal strategy."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): AAPL is in an established uptrend above SMA20 with a positive PnL of +1.08%. Adhering to the equity holding patience rule, we will let this winner run without premature rotation.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain patience with AAPL and MSFT equity holdings as they are performing stably above their SMAs. Keep crypto sidelined; wait for BTC-USD or another high-quality crypto asset to pull back to an RSI between 32 and 65 with a confirmed positive 1h price change before deploying capital into the single allowed crypto position."
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
