# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-22 11:40:52`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.20 USD** | **$16.96 USD** | **$39.16 USD** | 🔴 **-2.10%** ($-0.84) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $342.74 | $10.06 | 📈 +0.62% | 1d 23h |
| `MSFT` | 0.013196 | $530.45 | $523.07 | $6.90 | 📉 -1.39% | 23h 39m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market is experiencing a broad pullback with major indices and stocks trading below their SMA20 lines, indicating a temporary bearish sentiment or consolidation phase. AAPL remains resilient in a confirmed uptrend above its SMA20 with solid daily momentum. Other assets like MSFT, QQQ, and SPY are showing weakness but adhering to our equity patience rule. Crypto assets are currently depressed with low RSI levels and negative short-term momentum, keeping us out of crypto positions per our strict trend and reversal confirmation rules."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in a confirmed uptrend above its SMA20 and showing positive performance (+0.62%). Per equity holding patience rules, we maintain the position to let winners run toward our +3% to +5% profit target.
- **[HOLD] MSFT** (Confidence: 75%): MSFT is currently experiencing a minor pullback (-1.39%), well within our acceptable risk limits above the -1.8% to -2.0% hard stop-loss threshold. We maintain the position and give it time to recover.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain patience with current equity holdings (AAPL and MSFT). AAPL is profitable (+0.62%) and holding above SMA20; let it run toward target gains (+3% to +5%). MSFT is slightly down (-1.39%) but within acceptable limits; do not panic sell prematurely. Monitor MSFT and equity positions for stop-loss triggers at -1.8% to -2.0% or recovery above SMA20. Stay on the sidelines for crypto until clear trend reversals and positive 1-hour changes appear."
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
