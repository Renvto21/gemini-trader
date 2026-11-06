# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-06 17:40:46`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.14 USD** | **$13.43 USD** | **$38.57 USD** | 🔴 **-3.59%** ($-1.43) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $343.63 | $6.47 | 📉 -0.50% | 1d 0h |
| `MSFT` | 0.013089 | $534.82 | $531.83 | $6.96 | 📉 -0.56% | 4h 30m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The portfolio currently holds AAPL and MSFT, both of which are in confirmed uptrends above their SMA20 daily lines, complying with equity holding patience rules despite minor short-term pullbacks (-0.50% and -0.56% respectively). Most broader market indices and assets like SPY, QQQ, NVDA, and GLD remain in bearish trends below their SMA20 lines. Cryptocurrencies like ETH-USD, BTC-USD, and SOL-USD show mixed 1-hour momentum but lack clean reversal triggers or are currently trading in bearish trends, meaning no new crypto positions will be opened to avoid correlation and trend violations."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is maintaining its position above the daily SMA20 trend line. Per equity holding patience rules, short-term flat action or minor pullbacks do not warrant selling unless the stop-loss of -1.8% to -2.0% is triggered.
- **[HOLD] MSFT** (Confidence: 85%): MSFT is holding firmly above its SMA20 daily trend line. We maintain the position in line with equity holding patience rules, awaiting upside movement toward the +3.0% to +5.0% profit target.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain patient holding of AAPL and MSFT equity positions as they are above SMA20 and have not breached the -1.8% to -2.0% stop-loss threshold. Keep monitoring crypto assets for proper uptrend recovery and positive 1H momentum confirmation before considering any 24/7 liquidity allocation. Cash reserves remain solid at $25.14 USD."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **89** | 🎯 **42.7%** (38W / 36L / 15BE) | 🔴 **$-1.23 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-06 13:10` | 🟢 BUY | `MSFT` | $7.00 | $534.82 | MSFT is in a confirmed uptrend above its SMA20, market status is open, 1-hour RSI has reco... |
| `2026-11-05 17:40` | 🟢 BUY | `AAPL` | $6.50 | $345.35 | AAPL is in a confirmed uptrend above its SMA20, market status is open, and 1-hour momentum... |
| `2026-11-05 11:20` | 🔴 SELL (-0.15$) | `ETH-USD` | $6.85 | $2374.60 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -2.10% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-05 01:41` | 🟢 BUY | `ETH-USD` | $7.00 | $2425.59 | ETH-USD is in a confirmed uptrend above its SMA20, market status is open 24/7, 1-hour RSI ... |
| `2026-11-04 22:00` | 🔴 SELL (-0.31$) | `MSFT` | $6.69 | $520.99 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -4.44% hit safety limit (-2.0%). Liquidated by code... |

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
