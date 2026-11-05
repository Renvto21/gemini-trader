# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-04 23:00:54`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$38.78 USD** | **$0.00 USD** | **$38.78 USD** | 🔴 **-3.04%** ($-1.22) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| *(No open positions - 100% in cash)* | - | - | - | - | - | - |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Traditional equity and commodity markets are currently closed with prices frozen, showing pervasive bearish trends below their respective SMA20 levels following recent pullbacks. In contrast, cryptocurrency markets remain active 24/7. Among the crypto assets, ETH-USD and BTC-USD are trading in confirmed uptrends above their SMA20. However, BTC-USD features a 1-hour RSI of 79.0 with a negligible 1-hour change of +0.01%, and ETH-USD shows a 1-hour RSI of 77.5 with a negative 1-hour change of -0.05%, failing to meet our strict reversal confirmation trigger ('rsi_1h' >= 32 and 'change_1h_pct' > 0.0 with a proper cooling pullback). Consequently, capital preservation rules dictate a HOLD posture until an optimal entry dip occurs."

**Cycle Actions:**
- **[HOLD] BTC-USD** (Confidence: 85%): BTC-USD is above the SMA20 in an uptrend, but the 1-hour RSI is currently overbought at 79.0 and the 1-hour price change (+0.01%) shows lack of immediate bounce momentum. Waiting for a proper pullback and confirmed green candle per institutional rules.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Capital preserved at $38.78 cash. Traditional markets are closed; crypto assets ETH-USD and BTC-USD remain in confirmed uptrends above the SMA20 but their 1-hour RSI indicators are still elevated (>75) and lacking strong positive 1-hour momentum candles. Will wait patiently for a deeper consolidation phase (RSI cooling down to 45-65) paired with a confirmed positive 1-hour price change before allocating $6.00 to $8.00 into a single crypto position."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **88** | 🎯 **43.2%** (38W / 35L / 15BE) | 🔴 **$-1.08 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-04 22:00` | 🔴 SELL (-0.31$) | `MSFT` | $6.69 | $520.99 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -4.44% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-04 11:30` | 🟢 BUY | `MSFT` | $7.00 | $545.20 | MSFT is currently the only asset trading above its SMA20 in a confirmed uptrend with stron... |
| `2026-11-02 11:40` | 🔴 SELL (-0.13$) | `AAPL` | $6.87 | $340.69 | AAPL has slipped further into a bearish trend below its SMA20 with a 1-hour RSI of 24.8 an... |
| `2026-10-28 13:21` | 🔴 SELL (-0.02$) | `MSFT` | $6.48 | $528.16 | MSFT has shifted to a bearish trend below its SMA20 and current performance is near our st... |
| `2026-10-26 12:01` | 🟢 BUY | `MSFT` | $6.50 | $530.04 | MSFT is in a confirmed uptrend above its SMA20, and the 1-hour RSI (62.8) and 1-hour perce... |

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
