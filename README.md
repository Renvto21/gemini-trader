# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-22 15:50:45`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.37 USD** | **$6.89 USD** | **$39.26 USD** | 🔴 **-1.86%** ($-0.74) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.013196 | $530.45 | $521.98 | $6.89 | 📉 -1.60% | 1d 3h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market remains largely under pressure with most assets trading below their SMA20, signaling a prevailing bearish macro environment. AAPL is a notable exception, maintaining a confirmed bullish trend above its SMA20 with strong daily and hourly momentum, though its 1-hour RSI is currently elevated at 77.4. Our current holding MSFT is experiencing mild drawdown (-1.6%), hovering just above our strict -1.8% to -2.0% stop-loss threshold. We continue to exercise equity holding patience in accordance with our rules, monitoring MSFT closely for a potential stop-loss breach or a recovery."

**Cycle Actions:**
- **[HOLD] MSFT** (Confidence: 80%): MSFT is down -1.6%, approaching our stop-loss threshold of -1.8% to -2.0%. Adhering to our equity holding patience rule, we will hold through temporary flatness/minor drawdown unless the hard stop-loss is breached.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Monitor MSFT closely as it approaches the -1.8% to -2.0% stop-loss threshold. Maintain equity holding patience unless the stop-loss is triggered. AAPL remains above SMA20 but its RSI is currently overextended; wait for a healthy pullback with 1-hour RSI >= 32 and positive 1-hour price action before attempting any new entries. Keep cash reserves protected."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **84** | 🎯 **45.2%** (38W / 31L / 15BE) | 🔴 **$-0.50 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-22 14:40` | 🔴 SELL (+0.17$) | `AAPL` | $10.17 | $346.52 | AAPL rsi_1h has surpassed 72 (currently 73.4) with a positive return of +1.73%, satisfying... |
| `2026-10-21 12:01` | 🟢 BUY | `MSFT` | $7.00 | $530.45 | MSFT is in a confirmed uptrend above its SMA20. The 1-hour RSI is at 36.7 (above the 32 th... |
| `2026-10-21 10:10` | 🔴 SELL (+0.12$) | `ETH-USD` | $10.07 | $2481.87 | ETH-USD rsi_1h has surpassed 72 (currently 73.7) with a positive return of +1.21%, satisfy... |
| `2026-10-20 13:51` | 🟢 BUY | `ETH-USD` | $9.95 | $2452.17 | ETH-USD muestra un excelente impulso de corto plazo con change_1h_pct positivo (+0.55%) y ... |
| `2026-10-20 13:51` | 🔴 SELL (-0.05$) | `GLD` | $9.95 | $377.90 | GLD se encuentra estancado con un rendimiento ligeramente negativo (-0.47%) y un rsi_1h de... |

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
