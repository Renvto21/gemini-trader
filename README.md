# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-21 13:01:55`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.20 USD** | **$17.13 USD** | **$39.32 USD** | 🔴 **-1.70%** ($-0.68) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $344.36 | $10.11 | 📈 +1.09% | 1d 1h |
| `MSFT` | 0.013196 | $530.45 | $531.67 | $7.02 | 📈 +0.23% | 1h 0m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The current market environment shows mixed conditions with several key tech stocks and indices remaining above their SMA20 trend filters, while others are consolidating or trading below their respective SMA20 lines. AAPL and MSFT are currently held in the portfolio, both showing mild positive gains. AAPL is approaching profitable territory (+1.09%) in a confirmed uptrend, while MSFT is slightly up (+0.23%) and maintaining a stable posture above its SMA20. Cryptocurrencies like BTC-USD are in an uptrend but currently display overbought short-term conditions (rsi_1h > 72), failing to meet the clean pullback criteria needed for entry. Other assets like NVDA, QQQ, and ETH-USD are currently trading below their SMA20, prompting strict avoidance under our trend-following rules."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in a confirmed uptrend above its SMA20 with a positive unrealized gain (+1.09%). Adhering to the equity holding patience rule, we continue holding this position to let the winner run toward the +3.0% to +5.0% take-profit target.
- **[HOLD] MSFT** (Confidence: 80%): MSFT is holding steady in a confirmed uptrend above its SMA20. In accordance with equity holding patience rules, we maintain the position as it gives time for the trade to develop.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain patience with existing AAPL and MSFT equity positions per equity holding rules. Monitor AAPL closely for take-profit execution if it achieves the +3.0% to +5.0% target range. Keep crypto exposure sidelined until BTC-USD or another qualifying crypto experiences a healthy pullback to neutral RSI levels (>=32 and <=65) while remaining above its SMA20 with a confirmed positive 1-hour reversal candle."
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
