# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-08 19:40:42`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.14 USD** | **$13.39 USD** | **$38.53 USD** | 🔴 **-3.69%** ($-1.47) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $342.37 | $6.44 | 📉 -0.86% | 3d 1h |
| `MSFT` | 0.013089 | $534.82 | $530.61 | $6.94 | 📉 -0.79% | 2d 6h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market is currently experiencing a widespread risk-off pullback, with both major equities and cryptocurrencies trading below their respective SMA20 trend lines and flashing bearish signals. Wall Street assets (AAPL, MSFT, SPY, QQQ, NVDA, GLD) are currently closed for the weekend with frozen prices, and many have slipped slightly below our strict trend filter or are approaching stop-loss thresholds. Cryptocurrencies (BTC-USD, ETH-USD, SOL-USD) are open 24/7 but remain firmly in a downtrend below the SMA20 with negative 1-hour momentum, failing to meet our reversal confirmation triggers (rsi_1h >= 32 and change_1h_pct > 0). Given the strict quantitative rule never to catch falling knives and to respect market closure hours, no new positions can be opened. Existing equity positions in AAPL and MSFT must be held patiently in accordance with equity patience rules, monitoring their current slight drawdowns closely against the -1.8% to -2.0% circuit breakers."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): Asset is currently in a weekend market closure and remains within acceptable holding parameters above the stop-loss limit despite temporary softness.
- **[HOLD] MSFT** (Confidence: 100%): Asset is currently in a weekend market closure and remains within acceptable holding parameters above the stop-loss limit despite temporary softness.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing positions in AAPL and MSFT over the weekend closure. Monitor current drawdowns against the hard stop-loss circuit breaker near -2.0% (AAPL currently at -0.86%, MSFT at -0.79%). Do not execute any trades in crypto since all digital assets are in a confirmed downtrend below SMA20 and lack 1-hour reversal confirmation. Wait for Wall Street to reopen and for assets to decisively reclaim their SMA20 uptrend before deploying additional capital from our $25.14 cash reserves."
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
