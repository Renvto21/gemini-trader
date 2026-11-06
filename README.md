# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-06 20:20:50`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.14 USD** | **$13.39 USD** | **$38.53 USD** | 🔴 **-3.69%** ($-1.47) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $342.37 | $6.44 | 📉 -0.86% | 1d 2h |
| `MSFT` | 0.013089 | $534.82 | $530.61 | $6.94 | 📉 -0.79% | 7h 10m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market condition remains cautious, with Wall Street equity markets closed (CERRADO) and major assets such as AAPL, MSFT, SPY, QQQ, and NVDA currently trading below their respective SMA20 trends. Cryptocurrencies are operating 24/7, but most digital assets (BTC-USD, ETH-USD, SOL-USD) are also positioned below their SMA20 trend lines, preventing new buy executions under our strict trend-following pullback rules. Our existing equity positions in AAPL and MSFT are currently experiencing minor unrealized losses (-0.86% and -0.79% respectively), well above the -1.8% to -2.0% stop-loss circuit breaker threshold. In accordance with equity holding patience rules, we will hold these positions steady through the weekend while monitoring price action and momentum recovery."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): Holding current AAPL position in accordance with equity holding patience rules. The asset is down slightly (-0.86%), well clear of the hard stop-loss circuit breaker at -2.0%. Wall Street is closed.
- **[HOLD] MSFT** (Confidence: 85%): Holding current MSFT position patiently. Unrealized loss is minimal (-0.79%) and within normal fluctuation range for an equity position. Wall Street is currently closed.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL and MSFT patiently. Both are currently below their SMA20 lines due to broader market pullbacks, but holding times are short and neither has breached the -1.8% to -2.0% stop-loss limit. No new equity or crypto positions will be opened until markets reopen and specific assets reclaim their SMA20 uptrends with confirmed 1-hour green candle momentum and RSI >= 32."
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
