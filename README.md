# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-10 21:50:45`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.01 USD** | **$13.54 USD** | **$38.55 USD** | 🔴 **-3.63%** ($-1.45) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $348.51 | $6.56 | 📈 +0.92% | 5d 4h |
| `MSFT` | 0.013089 | $534.82 | $533.16 | $6.98 | 📉 -0.31% | 4d 8h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broad market is experiencing downward pressure with most equities and crypto assets trading below their SMA20 trend lines due to recent hot inflation data and surging treasury yields. Wall Street markets are currently closed (CERRADO), leaving prices frozen for equities. Among our current holdings, AAPL and MSFT remain in a confirmed uptrend above the SMA20, though MSFT is showing slight consolidation. Crypto assets (BTC, ETH, SOL) are all in a bearish trend with negative 24-hour changes and lack the necessary confirmation triggers (rsi_1h >= 32 and positive 1h change) to justify new entries."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in a confirmed uptrend above its SMA20 and is currently profitable (+0.92%). Adhering to the equity holding patience rule, we give it time to run rather than rotating out prematurely.
- **[HOLD] MSFT** (Confidence: 85%): MSFT remains above its SMA20 trend line despite minor short-term consolidation. Following equity holding patience rules, we maintain the position as long as it stays above the strict stop-loss threshold.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintained existing positions in AAPL and MSFT as they remain in a confirmed uptrend above the SMA20, respecting equity holding patience rules. Kept crypto positions closed due to widespread bearish trends and lack of confirmed upward bounce triggers. Will continue to monitor stop-losses strictly around -1.8% to -2.0% and preserve our $25.01 cash reserve until Wall Street reopens and high-quality pullbacks present valid entry signals."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **90** | 🎯 **42.2%** (38W / 37L / 15BE) | 🔴 **$-1.35 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-10 11:31` | 🔴 SELL (-0.12$) | `GLD` | $6.87 | $371.60 | GLD has fallen below its SMA20 trend line and its current PnL is approaching the strict st... |
| `2026-11-09 11:30` | 🟢 BUY | `GLD` | $7.00 | $378.35 | GLD is in a confirmed uptrend above its SMA20, market status is open, 1-hour momentum is s... |
| `2026-11-06 13:10` | 🟢 BUY | `MSFT` | $7.00 | $534.82 | MSFT is in a confirmed uptrend above its SMA20, market status is open, 1-hour RSI has reco... |
| `2026-11-05 17:40` | 🟢 BUY | `AAPL` | $6.50 | $345.35 | AAPL is in a confirmed uptrend above its SMA20, market status is open, and 1-hour momentum... |
| `2026-11-05 11:20` | 🔴 SELL (-0.15$) | `ETH-USD` | $6.85 | $2374.60 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -2.10% hit safety limit (-2.0%). Liquidated by code... |

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
