# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-09 16:50:47`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.14 USD** | **$20.78 USD** | **$38.92 USD** | 🔴 **-2.71%** ($-1.08) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $351.39 | $6.61 | 📈 +1.75% | 3d 23h |
| `MSFT` | 0.013089 | $534.82 | $547.31 | $7.16 | 📈 +2.34% | 3d 3h |
| `GLD` | 0.018501 | $378.35 | $378.53 | $7.00 | 📈 +0.05% | 5h 19m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The portfolio is currently holding three strong uptrend positions (AAPL, MSFT, and GLD), all of which are trading above their respective SMA20 thresholds with positive momentum. MSFT and AAPL are showing solid gains (+2.34% and +1.75% respectively), approaching our initial take-profit window of +3.0% to +5.0%. GLD is stable and holding steady. Broad markets are mixed; while large-cap equities show localized recoveries, many major benchmarks and crypto assets remain below their SMA20, prompting us to adhere strictly to the rule of avoiding falling knives and unconfirmed trends. No stop-loss thresholds have been breached, and cash reserves are safely maintained above the minimum threshold."

**Cycle Actions:**
- **[HOLD] MSFT** (Confidence: 90%): MSFT remains in a solid confirmed uptrend above the SMA20 with a profit of +2.34%. Following equity holding patience rules, we let winners run toward the +3.0% to +5.0% take-profit target rather than closing prematurely.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing positions in AAPL, MSFT, and GLD as they respect their structural uptrends. Monitor MSFT and AAPL closely for take-profit opportunities if 1-hour RSI exceeds 72 or if gains reach +3.0% to +5.0%. Keep strict stop-loss levels at -2.0% across all positions. Continue avoiding crypto and below-SMA20 assets until confirmed reversal criteria are fully met."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **89** | 🎯 **42.7%** (38W / 36L / 15BE) | 🔴 **$-1.23 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-09 11:30` | 🟢 BUY | `GLD` | $7.00 | $378.35 | GLD is in a confirmed uptrend above its SMA20, market status is open, 1-hour momentum is s... |
| `2026-11-06 13:10` | 🟢 BUY | `MSFT` | $7.00 | $534.82 | MSFT is in a confirmed uptrend above its SMA20, market status is open, 1-hour RSI has reco... |
| `2026-11-05 17:40` | 🟢 BUY | `AAPL` | $6.50 | $345.35 | AAPL is in a confirmed uptrend above its SMA20, market status is open, and 1-hour momentum... |
| `2026-11-05 11:20` | 🔴 SELL (-0.15$) | `ETH-USD` | $6.85 | $2374.60 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -2.10% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-05 01:41` | 🟢 BUY | `ETH-USD` | $7.00 | $2425.59 | ETH-USD is in a confirmed uptrend above its SMA20, market status is open 24/7, 1-hour RSI ... |

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
