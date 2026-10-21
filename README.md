# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-21 16:50:43`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.20 USD** | **$17.14 USD** | **$39.34 USD** | 🔴 **-1.65%** ($-0.66) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $344.36 | $10.11 | 📈 +1.09% | 1d 4h |
| `MSFT` | 0.013196 | $530.45 | $533.04 | $7.03 | 📈 +0.49% | 4h 49m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The market shows selective bullish trends in equities, with AAPL and MSFT holding steady above their SMA20 lines and demonstrating stable upward behavior. Cryptocurrencies like BTC-USD remain in an uptrend but are currently experiencing elevated 1-hour RSI levels above 72, indicating overbought short-term conditions and discouraging immediate new entries. Other key assets such as NVDA, QQQ, and ETH-USD are currently trading below their SMA20 lines, remaining off-limits per the strict trend-following pullback rules."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in a confirmed uptrend above SMA20 with a solid profit of +1.09%. Adhering to the equity holding patience rule, we continue to let the winner run toward our +3.0% to +5.0% target.
- **[HOLD] MSFT** (Confidence: 85%): MSFT is in a confirmed uptrend above SMA20 and has been held for less than 24 hours. Maintaining the position to allow the trend to develop fully while respecting stop-losses.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing equity positions in AAPL and MSFT, letting winners run toward the +3.0% to +5.0% profit targets while strictly monitoring the -1.8% stop-loss limit. For cryptocurrencies like BTC-USD, wait for a cooler 1-hour RSI between 32 and 65 alongside a positive 1-hour price bounce confirmation before considering entry. Preserve cash above the $4.00 USD threshold."
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
