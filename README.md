# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-08 14:10:41`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.14 USD** | **$13.39 USD** | **$38.53 USD** | 🔴 **-3.69%** ($-1.47) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $342.37 | $6.44 | 📉 -0.86% | 2d 20h |
| `MSFT` | 0.013089 | $534.82 | $530.61 | $6.94 | 📉 -0.79% | 2d 0h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "All equity markets (AAPL, MSFT, SPY, QQQ, NVDA, GLD) are currently closed for the weekend, and their prices and trends reflect broader macro weakness as most assets are trading below their SMA20 with weak short-term momentum. Cryptocurrencies remain open 24/7, but none satisfy the strict trend filter or reversal confirmation triggers (all remain below SMA20 and lack positive 1-hour changes with required RSI levels). The existing equity positions in AAPL and MSFT are currently showing minor unrealized losses (-0.86% and -0.79% respectively), well within acceptable holding parameters, and must be held patiently through the weekend per equity patience rules."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): Asset is currently in a closed market status and position PnL is well within normal fluctuation range (-0.86%), remaining safely above the -1.8% to -2.0% stop-loss threshold. Equity holding patience rule applies.
- **[HOLD] MSFT** (Confidence: 100%): Asset is currently in a closed market status and position PnL is stable (-0.79%), avoiding premature rotation while adhering to equity holding patience rules.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing AAPL and MSFT equity positions during the weekend closure, respecting the rule to give equities time to play out unless stop-loss limits (-1.8% to -2.0%) are breached. Keep crypto exposure flat as digital assets fail the strict uptrend and reversal triggers. Monitor market reopenings for any shift in trend or momentum."
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
