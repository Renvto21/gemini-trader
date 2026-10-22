# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-22 15:20:48`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.37 USD** | **$6.92 USD** | **$39.29 USD** | 🔴 **-1.79%** ($-0.71) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.013196 | $530.45 | $524.16 | $6.92 | 📉 -1.19% | 1d 3h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market is currently experiencing a corrective phase with most assets trading below their SMA20 trendlines. Specifically, MSFT is currently below its SMA20 (-1.19% PnL) but remains protected by our equity patience rule as it has not hit the hard stop-loss threshold of -1.8% to -2.0%. AAPL is in a confirmed uptrend (above SMA20) with high RSI (>72), but we do not currently hold it. Other potential buy candidates do not meet the rigorous pullback criteria (uptrend confirmation combined with RSI >= 32 and positive 1-hour candle). Cash reserves are maintained safely above the minimum threshold."

**Cycle Actions:**
- **[HOLD] MSFT** (Confidence: 85%): MSFT is currently experiencing a minor pullback with an unrealized loss of -1.19%, which is well within our acceptable risk limits. In accordance with equity patience rules for stocks, we will hold the position and let it play out rather than prematurely selling.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Continue holding MSFT under equity patience rules while strictly monitoring the -1.8% to -2.0% stop-loss level. Wait for confirmed pullbacks in verified uptrend assets before deploying additional cash reserves into new trades."
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
