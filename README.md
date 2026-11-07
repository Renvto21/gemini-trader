# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-07 10:50:42`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.14 USD** | **$13.39 USD** | **$38.53 USD** | 🔴 **-3.69%** ($-1.47) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $342.37 | $6.44 | 📉 -0.86% | 1d 17h |
| `MSFT` | 0.013089 | $534.82 | $530.61 | $6.94 | 📉 -0.79% | 21h 39m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Traditional equity and commodity markets are currently closed (CERRADO), featuring frozen prices and ongoing downward pressure with most assets trading below their SMA20. In the crypto sector, markets remain open 24/7, but assets like ETH-USD and SOL-USD continue to exhibit bearish trends below their respective SMA20 lines, violating our strict trend-following filters. We currently hold open positions in AAPL and MSFT. Although both are temporarily under their SMA20 due to weekend/market close conditions, rule #6 mandates equity holding patience, instructing us not to rotate or sell equity positions prematurely unless stop-loss levels are breached. No crypto positions are held, keeping us safe from high downside correlations."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): Equity holding patience applies. AAPL is held through the weekend market closure; minor fluctuations do not trigger a sale per rule #6, and stop-loss levels have not been breached.
- **[HOLD] MSFT** (Confidence: 85%): Equity holding patience applies. MSFT remains in the portfolio through the market closure, respecting the rule to give quality equities time to play out unless stop-losses are triggered.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain strict discipline holding AAPL and MSFT positions through the weekend close. Do not panic or sell on flat or mildly negative equity fluctuations unless the strict stop-loss threshold (-1.8% to -2.0%) is hit when markets reopen. For crypto, avoid all buy orders because all available crypto assets remain in a confirmed downtrend below SMA20. Continue preserving cash reserves above $4.00 USD and wait for a structural trend reversal and confirmed uptrends before deploying additional capital."
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
