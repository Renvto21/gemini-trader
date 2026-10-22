# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-22 12:31:05`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.20 USD** | **$17.05 USD** | **$39.25 USD** | 🔴 **-1.88%** ($-0.75) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $344.92 | $10.13 | 📈 +1.26% | 2d 0h |
| `MSFT` | 0.013196 | $530.45 | $524.98 | $6.93 | 📉 -1.03% | 1d 0h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market is currently exhibiting a bearish stance with most major assets and equities trading below their SMA20 trend lines. AAPL remains a notable exception, maintaining its position in an uptrend (above SMA20) with strong daily and 1-hour RSI metrics, showing positive progression toward take-profit targets (+3.0% to +5.0%). MSFT has dropped slightly below its entry price (-1.03%) but remains well within acceptable holding parameters, avoiding the hard stop-loss threshold of -2.0% while respecting equity holding patience guidelines. Other assets, including cryptocurrencies and broader indices, fail to meet our strict pullback criteria due to ongoing downtrends and negative 1-hour percentage changes."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in a confirmed uptrend above SMA20 with solid positive performance (+1.26%). Holding to let profits run toward the +3.0% to +5.0% target zone.
- **[HOLD] MSFT** (Confidence: 80%): MSFT is currently down -1.03%, remaining well above the strict -1.8% to -2.0% stop-loss threshold. Applying equity holding patience rule to let the position play out.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL and MSFT positions. AAPL is approaching take-profit consideration if 1-hour RSI exceeds 72 with profit >= +2.5%. MSFT is closely monitored for stop-loss compliance (-1.8% to -2.0%); will hold patiently unless trend breakdown forces exit. No new entries are warranted until crypto or equity assets confirm a solid reversal with positive 1H momentum and RSI >= 32 in confirmed uptrends."
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
