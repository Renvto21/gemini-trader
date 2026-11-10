# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-10 18:50:50`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.01 USD** | **$13.54 USD** | **$38.55 USD** | 🔴 **-3.63%** ($-1.45) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $348.51 | $6.56 | 📈 +0.92% | 5d 1h |
| `MSFT` | 0.013089 | $534.82 | $533.16 | $6.98 | 📉 -0.31% | 4d 5h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Major equity indices and traditional assets like GLD are currently closed (CERRADO) for the weekend, exhibiting bearish macro sentiment and trading below their SMA20 lines. In the crypto markets (ABIERTO 24/7), assets such as BTC-USD, ETH-USD, and SOL-USD remain in confirmed downtrends below their SMA20 with weak 1-hour momentum, violating our strict trend filter rules. Our current equity holdings, AAPL and MSFT, are stable and adhering to holding patience rules despite flat short-term movements."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is in an uptrend above its SMA20 and is currently profitable. Following equity holding rules, we maintain our position and ignore short-term fluctuations.
- **[HOLD] MSFT** (Confidence: 90%): MSFT remains in a confirmed uptrend above its SMA20. In accordance with equity holding rules, positions are given time to play out unless stop-loss limits are breached.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL and MSFT per equity holding rules as they remain above SMA20. Will continue monitoring crypto assets for structural trend recovery above SMA20 and confirmation triggers (rsi_1h >= 32 and change_1h_pct > 0.0) before executing any 24/7 exposure. Strict stop-losses at -2.0% and profit targets at +3.0% to +5.0% remain in place."
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
