# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-22 13:00:58`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.20 USD** | **$17.08 USD** | **$39.28 USD** | 🔴 **-1.80%** ($-0.72) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $345.47 | $10.14 | 📈 +1.42% | 2d 0h |
| `MSFT` | 0.013196 | $530.45 | $526.10 | $6.94 | 📉 -0.82% | 1d 0h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market remains mostly under pressure with major indices and stocks trading below their respective SMA20 trends, reflecting a cautious macroeconomic environment. AAPL stands out as a strong performer, holding a confirmed uptrend above its SMA20 with solid daily and hourly momentum, currently showing a +1.42% profit. MSFT experienced a slight pullback (-0.82%) but remains well within acceptable risk limits above the -1.8% stop-loss threshold, adhering to our equity holding patience policy. Cryptocurrencies and other assets show weak momentum or remain in bearish trends below the SMA20, prompting us to avoid new crypto entries."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 80%): AAPL is in a confirmed uptrend above its SMA20 with solid profits (+1.42%). Following the asymmetric risk/reward rule, we let winners run and wait for take-profit criteria (rsi_1h > 72 with profit >= +2.5%) or price target achievement.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL and MSFT. AAPL is approaching take-profit territory (+3.0% to +5.0% or rsi_1h > 72 with profit >= +2.5%); will monitor closely for exit conditions. MSFT is stable above our hard stop-loss threshold despite trading below its SMA20 at entry; adhering to equity holding patience. No new positions will be opened until clear trend and RSI recovery criteria are met on available assets."
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
