# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-21 19:30:50`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.20 USD** | **$17.13 USD** | **$39.33 USD** | 🔴 **-1.68%** ($-0.67) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $343.99 | $10.10 | 📈 +0.98% | 1d 7h |
| `MSFT` | 0.013196 | $530.45 | $532.95 | $7.03 | 📈 +0.47% | 7h 29m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Wall Street equities (AAPL, MSFT, SPY, NVDA, QQQ, GLD) are currently closed, with prices frozen. AAPL and MSFT are being held patiently according to equity holding rules, currently showing small positive gains (+0.98% and +0.47% respectively). In the 24/7 crypto markets, BTC-USD is in an uptrend above its SMA20 but its 1-hour candle is currently negative (change_1h_pct: -0.27%) and RSI is elevated at 77.9, failing to meet our pullback and green candle confirmation criteria. ETH-USD, SOL-USD, and NVDA are in downtrends below their SMA20s and are excluded from buying."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): AAPL is in a confirmed uptrend and holding a positive gain (+0.98%). Following equity patience rules, we hold through market closure, awaiting the +3.0% to +5.0% profit target.
- **[HOLD] MSFT** (Confidence: 100%): MSFT is in a confirmed uptrend and showing positive return (+0.47%). Adhering to the equity holding discipline, positions are given time to develop unless stop-losses are triggered.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing equity positions (AAPL and MSFT) through market closure, respecting +3.0% to +5.0% profit targets and -1.8% to -2.0% stop-losses. For crypto, monitor BTC-USD for a healthy pullback into a neutral RSI zone with a confirmed positive 1-hour candle before considering deployment. Do not open new trades until all strict entry and market status criteria are fully met."
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
