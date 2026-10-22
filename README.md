# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-22 13:31:14`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.20 USD** | **$17.11 USD** | **$39.30 USD** | 🔴 **-1.74%** ($-0.70) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $346.17 | $10.16 | 📈 +1.62% | 2d 1h |
| `MSFT` | 0.013196 | $530.45 | $526.26 | $6.94 | 📉 -0.79% | 1d 1h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market is exhibiting a broad pullback with most major indices and stocks trading below their SMA20 lines, reflecting short-term bearish pressure. AAPL remains a resilient outlier, holding an uptrend above its SMA20 with solid daily momentum and approaching take-profit territory as its 1-hour RSI climbs near 67.2. Other assets like MSFT, NVDA, SPY, QQQ, and crypto assets are currently below their SMA20 with negative 1-hour changes, failing to satisfy our strict trend filter and reversal trigger rules. Consequently, we maintain our equity positions while preserving robust cash reserves."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL remains in a confirmed uptrend above its SMA20 with strong daily momentum and positive PnL (+1.62%). Holding patiently to let the winner run towards our +3.0% to +5.0% target.
- **[HOLD] MSFT** (Confidence: 75%): MSFT position is experiencing slight short-term weakness (-0.79% PnL) but is within acceptable volatility limits. Adhering to the equity holding patience rule while monitoring the hard stop-loss at -1.8% to -2.0%.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Continue to hold AAPL and monitor for profit-taking targets (+3.0% to +5.0% gain, or rsi_1h > 72 with profit >= +2.5%). Hold MSFT patiently despite short-term consolidation below SMA20, respecting the hard stop-loss at -1.8% to -2.0%. Keep cash reserves high and wait for validated pullback entry triggers (rsi_1h >= 32 and change_1h_pct > 0.0) in assets confirmed above their SMA20 trend."
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
