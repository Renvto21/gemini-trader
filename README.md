# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-12 06:30:52`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$31.84 USD** | **$6.69 USD** | **$38.54 USD** | 🔴 **-3.66%** ($-1.46) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $355.63 | $6.69 | 📈 +2.98% | 6d 12h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader equity and crypto markets remain in a defensive posture with most key assets trading below their SMA20 lines, indicating ongoing consolidation or bear trends. Stock markets (AAPL, SPY, QQQ, MSFT, GLD, NVDA) are currently closed (market status: CERRADO), preventing any stock actions. Cryptocurrencies (SOL-USD, BTC-USD, ETH-USD) remain open 24/7 but are failing to show confirmed bullish reversal triggers (rsi_1h remains below 32 and 1-hour changes are flat or negative), confirming we must avoid catching falling knives. Our sole open position, AAPL, continues to hold a solid profit of +2.98% while staying above its SMA20 trend line in an uptrend, with its 1-hour RSI nearing overbought levels (70.4). Adhering to equity holding patience and asymmetric reward targets, we maintain the AAPL position while preserving cash."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is in a confirmed uptrend above its SMA20, currently showing a +2.98% profit. Sticking to equity holding patience rules, we allow the winning trade room to develop toward our +3.5% to +5.0% take-profit target or an RSI > 72 reading.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain the AAPL holding under equity patience rules. Watch for take-profit execution if AAPL's 1-hour RSI crosses above 72 or PnL hits the +3.5% to +5.0% range. Keep all closed-market assets and crypto sidelined until they cleanly reclaim their SMA20 lines and show confirmed positive momentum triggers (rsi_1h >= 32 and positive 1-hour candles). Cash reserves remain well-protected at $31.84."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **91** | 🎯 **41.8%** (38W / 38L / 15BE) | 🔴 **$-1.52 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-11 12:20` | 🔴 SELL (-0.17$) | `MSFT` | $6.83 | $521.92 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -2.41% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-10 11:31` | 🔴 SELL (-0.12$) | `GLD` | $6.87 | $371.60 | GLD has fallen below its SMA20 trend line and its current PnL is approaching the strict st... |
| `2026-11-09 11:30` | 🟢 BUY | `GLD` | $7.00 | $378.35 | GLD is in a confirmed uptrend above its SMA20, market status is open, 1-hour momentum is s... |
| `2026-11-06 13:10` | 🟢 BUY | `MSFT` | $7.00 | $534.82 | MSFT is in a confirmed uptrend above its SMA20, market status is open, 1-hour RSI has reco... |
| `2026-11-05 17:40` | 🟢 BUY | `AAPL` | $6.50 | $345.35 | AAPL is in a confirmed uptrend above its SMA20, market status is open, and 1-hour momentum... |

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
