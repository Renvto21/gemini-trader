# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-21 12:01:09`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.20 USD** | **$17.07 USD** | **$39.27 USD** | 🔴 **-1.83%** ($-0.73) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $343.17 | $10.07 | 📈 +0.74% | 23h 59m |
| `MSFT` | 0.013196 | $530.45 | $530.45 | $7.00 | 📈 +0.00% | 0m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The portfolio currently holds AAPL, which is showing steady performance above its SMA20 with a positive PnL of +0.74%. Following equity holding rules, patience is maintained as the position has only been open for 24 hours. In the broader market, MSFT is trading in an uptrend above SMA20 with an RSI_1H of 36.7 and a positive 1-hour change of +0.2%, fulfilling our reversal confirmation trigger for a high-quality pullback. BTC-USD is in an uptrend but has an overbought RSI_1H of 81.8, making it unsuitable for entry at this moment. Other assets are either in downtrends or do not meet strict reversal criteria."

**Cycle Actions:**
- **[BUY] MSFT** (Confidence: 85%): MSFT is in a confirmed uptrend above its SMA20. The 1-hour RSI is at 36.7 (above the 32 threshold) and the 1-hour change is positive (+0.2%), confirming a healthy pullback and bounce entry according to our quantitative rules.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Hold AAPL patiently aiming for a take-profit target between +3.0% and +5.0% while monitoring the stop-loss circuit breaker at -2.0%. Monitor MSFT for continued confirmation and consider opening a position if conditions persist. Keep crypto sidelined due to anti-correlation constraints and overbought conditions."
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
