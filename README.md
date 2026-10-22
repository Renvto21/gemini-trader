# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-22 12:40:56`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.20 USD** | **$17.06 USD** | **$39.26 USD** | 🔴 **-1.86%** ($-0.74) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $345.41 | $10.14 | 📈 +1.40% | 2d 0h |
| `MSFT` | 0.013196 | $530.45 | $524.50 | $6.92 | 📉 -1.12% | 1d 0h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market continues to exhibit broad weakness, with major indices and equities trading below their SMA20 daily trends due to macroeconomic headwinds. AAPL remains a notable exception, maintaining its position in a confirmed uptrend (above SMA20) with steady performance, while MSFT has dipped slightly below its SMA20 trend, currently showing minor negative returns (-1.12%). Cryptocurrencies and other assets are largely in a bearish short-term posture with weak 1-hour momentum, requiring extreme patience and strict adherence to trend and reversal filters."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 80%): AAPL remains in a confirmed uptrend above its SMA20 with solid positive performance (+1.4%). Adhering to the equity holding patience rule, we continue to hold for potential take-profit conditions (RSI > 72 and profit >= +2.5%).

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL and MSFT positions patiently per equity holding rules. AAPL is approaching take-profit consideration if 1-hour RSI exceeds 72 with profit >= +2.5%. MSFT is closely monitored for stop-loss compliance (-1.8% to -2.0%); holding patiently despite the slight dip below SMA20 since it has not hit the hard circuit breaker. No new entries are warranted until assets confirm a solid reversal with positive 1H momentum and RSI >= 32 in confirmed uptrends."
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
