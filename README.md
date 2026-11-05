# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-05 16:10:49`

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

> "The market is experiencing a significant pullback across both equities and crypto, with major assets like SPY, QQQ, NVDA, and all crypto pairs trading below their SMA20 in a short-term bearish structure. Cryptocurrencies are heavily oversold with extremely low 1-hour RSI readings, but do not meet our reversal confirmation trigger (change_1h_pct > 0.0 and rsi_1h >= 32). Among equities, AAPL and MSFT remain in an uptrend (above SMA20) with positive 1-hour percentage changes, though their 1-hour RSI has not dipped into a deep pullback zone yet. GLD is overbought on the 1-hour RSI (89.9) and not suitable for a buy entry. We maintain patience, preserving our cash reserves while waiting for clean trend-following pullback setups with proper bullish confirmation."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 0%): AAPL is in an uptrend above SMA20 with a positive 1-hour change, but the 1-hour RSI is at 64.2, which is not low enough for an optimal pullback entry. We await a deeper dip while preserving cash.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintained capital preservation with 100% cash ($38.64). Avoided catching falling knives in crypto and downtrending equities. Looking for AAPL or MSFT to pull back slightly while maintaining trend status, or waiting for crypto to demonstrate a true 1-hour recovery bounce (rsi_1h >= 32 and change_1h_pct > 0.0) before deploying positions. Strict adherence to stop-losses and position sizing will continue."
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
