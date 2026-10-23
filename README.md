# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-23 11:01:06`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$39.25 USD** | **$0.00 USD** | **$39.25 USD** | 🔴 **-1.88%** ($-0.75) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| *(No open positions - 100% in cash)* | - | - | - | - | - | - |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market remains largely under pressure with most major equities, indices, and assets trading below their SMA20, signaling a prevailing bearish or corrective market structure. AAPL is the sole asset maintaining a confirmed uptrend above its SMA20, but its 1-hour RSI is heavily overbought at 78.8 with a minimal 1-hour percentage change. Cryptocurrencies like SOL-USD, ETH-USD, and BTC-USD show positive 24-hour momentum, but are currently below their SMA20 trend filters and fail our strict pullback criteria."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in a confirmed uptrend above the SMA20, meeting our primary asset quality requirement. However, its 1-hour RSI is currently overbought at 78.8 and the 1-hour price change is negligible. We await a healthy pullback where rsi_1h >= 32 and change_1h_pct > 0.0 to execute a safe entry.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Cash reserves are fully intact at $39.25. AAPL remains the only asset in an uptrend above SMA20, but its current 1h RSI is overbought (78.8) and lacks a proper dip with a green 1-hour candle confirmation. We will patiently wait for AAPL to experience a controlled pullback where rsi_1h >= 32 and change_1h_pct > 0.0 before entering. Maintain absolute discipline, preserving capital, and strictly avoiding falling knives."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **85** | 🎯 **44.7%** (38W / 32L / 15BE) | 🔴 **$-0.62 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-22 16:00` | 🔴 SELL (-0.12$) | `MSFT` | $6.88 | $521.40 | MSFT has dropped to a PnL of -1.71%, closely approaching our mandatory stop-loss threshold... |
| `2026-10-22 14:40` | 🔴 SELL (+0.17$) | `AAPL` | $10.17 | $346.52 | AAPL rsi_1h has surpassed 72 (currently 73.4) with a positive return of +1.73%, satisfying... |
| `2026-10-21 12:01` | 🟢 BUY | `MSFT` | $7.00 | $530.45 | MSFT is in a confirmed uptrend above its SMA20. The 1-hour RSI is at 36.7 (above the 32 th... |
| `2026-10-21 10:10` | 🔴 SELL (+0.12$) | `ETH-USD` | $10.07 | $2481.87 | ETH-USD rsi_1h has surpassed 72 (currently 73.7) with a positive return of +1.21%, satisfy... |
| `2026-10-20 13:51` | 🟢 BUY | `ETH-USD` | $9.95 | $2452.17 | ETH-USD muestra un excelente impulso de corto plazo con change_1h_pct positivo (+0.55%) y ... |

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
