# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-11 04:50:35`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.01 USD** | **$13.54 USD** | **$38.55 USD** | 🔴 **-3.63%** ($-1.45) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $348.51 | $6.56 | 📈 +0.92% | 5d 11h |
| `MSFT` | 0.013089 | $534.82 | $533.16 | $6.98 | 📉 -0.31% | 4d 15h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broad stock market is currently closed (market status 'CERRADO'), with key equities like AAPL and MSFT maintaining healthy uptrends above their SMA20 lines. Our open equity positions are resilient, with AAPL showing positive momentum (+0.92% PnL) and MSFT trading flat near our entry cost. In the cryptocurrency sector (open 24/7), major assets such as BTC-USD, ETH-USD, and SOL-USD remain trapped in bearish trends below their SMA20 levels. Following our strict quantitative rules, we do not catch falling knives or buy crypto assets in bear trends. Therefore, we remain fully compliant with trend-filtering and anti-correlation constraints."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL remains in a confirmed uptrend above its SMA20 with a positive PnL (+0.92%). Adhering to the equity holding patience rule, we will let this winner run towards our +3.0% to +5.0% profit target while market status is closed.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain patience with active equity positions AAPL and MSFT as they continue to hold above their SMA20 trends. Wall Street remains closed, preventing any stock executions. Crypto assets remain in bear trends, keeping us sidelined despite positive 1-hour candles. We will monitor for market reopening to evaluate profit targets (+3.0% to +5.0%) for AAPL and manage risk on MSFT while strictly adhering to the -2.0% stop-loss threshold."
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
