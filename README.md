# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-05 12:10:54`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$38.64 USD** | **$0.00 USD** | **$38.64 USD** | 🔴 **-3.41%** ($-1.36) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| *(No open positions - 100% in cash)* | - | - | - | - | - | - |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market is experiencing a severe pullback, with major indices like SPY and QQQ sliding below their SMA20 lines in a downtrend. Crypto assets (SOL-USD, ETH-USD, BTC-USD) are deep in a bear trend with extremely oversold 1-hour RSI metrics (near 10-21) and negative 1-hour and 24-hour returns, violating our strict trend-filter rules. Among equities, MSFT, GLD, and AAPL remain in uptrends above their SMA20, but GLD and AAPL/MSFT show extremely high 1-hour RSI levels (GLD at 91.6, AAPL at 76.1) or negative hourly momentum, indicating we must patiently wait for a proper pullback confirmation with an hourly RSI >= 32 and a positive 1-hour return before deployment."

**Cycle Actions:**
- **[HOLD] GLD** (Confidence: 0%): GLD is in an uptrend above SMA20, but the 1-hour RSI is extremely overbought at 91.6. We wait for a healthy pullback and a confirmed green 1-hour reversal candle before deploying capital.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Preserving capital with $38.64 USD cash. Cryptos and index ETFs are currently in downtrends or failing trend confirmations. GLD, MSFT, and AAPL are in uptrends but overextended or currently printing negative 1-hour candles. Will monitor GLD and AAPL for a healthy pullback to support levels with RSI >= 32 and a green 1-hour candle before executing a standard entry. Maintaining strict discipline regarding stop-losses and risk-reward parameters."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **89** | 🎯 **42.7%** (38W / 36L / 15BE) | 🔴 **$-1.23 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-05 11:20` | 🔴 SELL (-0.15$) | `ETH-USD` | $6.85 | $2374.60 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -2.10% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-05 01:41` | 🟢 BUY | `ETH-USD` | $7.00 | $2425.59 | ETH-USD is in a confirmed uptrend above its SMA20, market status is open 24/7, 1-hour RSI ... |
| `2026-11-04 22:00` | 🔴 SELL (-0.31$) | `MSFT` | $6.69 | $520.99 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -4.44% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-04 11:30` | 🟢 BUY | `MSFT` | $7.00 | $545.20 | MSFT is currently the only asset trading above its SMA20 in a confirmed uptrend with stron... |
| `2026-11-02 11:40` | 🔴 SELL (-0.13$) | `AAPL` | $6.87 | $340.69 | AAPL has slipped further into a bearish trend below its SMA20 with a 1-hour RSI of 24.8 an... |

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
