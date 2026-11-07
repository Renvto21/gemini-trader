# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-07 16:20:40`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.14 USD** | **$13.39 USD** | **$38.53 USD** | 🔴 **-3.69%** ($-1.47) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $342.37 | $6.44 | 📉 -0.86% | 1d 22h |
| `MSFT` | 0.013089 | $534.82 | $530.61 | $6.94 | 📉 -0.79% | 1d 3h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market remains in a cautious state with most major equities and cryptocurrencies trading below their respective SMA20 trend filters, classifying them in bearish trends. Wall Street assets are currently closed (CERRADO), leaving active liquidity confined to 24/7 crypto markets. While BTC-USD shows a slight positive 1-hour change (+0.01%) and an RSI of 36.4, it still fails the strict trend requirement as it is below the SMA20. Existing equity positions in AAPL and MSFT are currently experiencing minor unrealized drawdowns (-0.86% and -0.79% respectively), but adherence to equity holding patience dictates letting them play out rather than panic selling, provided they remain above the hard stop-loss threshold of -2.0%."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 80%): Holding current AAPL position in accordance with equity holding patience guidelines. Position is well above the -2.0% stop-loss threshold and markets are currently closed.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Hold existing positions in AAPL and MSFT while equities markets remain closed through the weekend. Monitor crypto assets (BTC-USD, SOL-USD, ETH-USD) for confirmed upside momentum, ensuring any future entry strictly meets the criteria of being above SMA20 (or wait for trend recovery), RSI >= 32, and a positive 1-hour change. Maintain cash reserves above $4.00 USD and adhere to strict stop-loss limits (-2.0%)."
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
