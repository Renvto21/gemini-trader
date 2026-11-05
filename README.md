# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-05 14:20:43`

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

> "The broader market is experiencing significant downward pressure with major indices like QQQ, SPY, and crypto assets (BTC, ETH, SOL, NVDA) trading firmly in a bear trend below their respective SMA20 levels. RSI levels on 1-hour timeframes indicate heavily oversold conditions across the board, but strict quantitative trend-following filters dictate that we do not catch falling knives. Only assets like MSFT, AAPL, and GLD remain above their SMA20. Specifically, GLD shows an uptrend with positive 1-hour momentum, but its 1-hour RSI is extremely overbought at 93.5, signaling an imminent cooling-off period rather than an ideal entry. Given current conditions and strict reversal confirmation triggers (requiring 1-hour RSI >= 32 and positive 1-hour change), no new buy setups currently meet our asymmetric risk/reward criteria."

**Cycle Actions:**
- **[HOLD] MSFT** (Confidence: 80%): MSFT is currently in a confirmed uptrend above its SMA20 with solid daily strength, but its 1-hour candle is currently negative (-0.44%). We hold cash and wait for a proper pullback confirmation with a green hourly candle before re-entering.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintained capital preservation with 38.64 USD in cash reserves after previous stop-loss triggers. Awaiting solid trend-following pullback confirmations in uptrend assets (e.g., MSFT or AAPL) where 1-hour RSI recovers to >= 32 with positive hourly price action. Continuing to avoid all crypto assets and falling market indices until clear structural reversals emerge."
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
