# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-12 06:50:36`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$31.84 USD** | **$6.69 USD** | **$38.54 USD** | 🔴 **-3.66%** ($-1.46) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $355.63 | $6.69 | 📈 +2.98% | 6d 13h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Wall Street equities and ETFs (AAPL, MSFT, QQQ, NVDA, GLD, SPY) are currently in 'CERRADO' (closed) status, with prices frozen. Cryptocurrencies (SOL-USD, ETH-USD, BTC-USD) are trading 24/7, but all of them remain in strict downtrends (below their SMA20) with weak 1-hour RSI readings (<32) and negative 1-hour momentum candles, meaning no valid bounce confirmations have triggered. Our sole open position, AAPL, is in a confirmed uptrend (above SMA20) and is showing a healthy unrealized profit of +2.98% (rsi_1h at 70.4). Because market hours are closed for equities and AAPL has not yet crossed our profit-taking threshold of +3.5% to +5.0% (or rsi_1h > 72), we adhere to equity holding patience rules."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in a solid uptrend above SMA20 with a +2.98% unrealized gain. Since equity markets are currently closed and the position has not yet reached the +3.5% to +5.0% profit-taking target or RSI threshold > 72, equity holding patience applies, and we maintain the position.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain the AAPL holding under equity holding patience and monitor for take-profit execution if PnL reaches +3.5% to +5.0% or 1-hour RSI exceeds 72 upon market reopening. Keep all crypto assets sidelined as they remain in downtrends below SMA20 without positive momentum triggers (rsi_1h >= 32 and positive 1-hour candle). Cash reserves remain protected at $31.84."
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
