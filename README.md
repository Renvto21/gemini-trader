# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-07 02:30:46`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.14 USD** | **$13.39 USD** | **$38.53 USD** | 🔴 **-3.69%** ($-1.47) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $342.37 | $6.44 | 📉 -0.86% | 1d 8h |
| `MSFT` | 0.013089 | $534.82 | $530.61 | $6.94 | 📉 -0.79% | 13h 20m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market condition remains challenging with major equity indices and crypto assets showing bearish momentum and trading below their respective SMA20 lines. Wall Street is currently closed for the weekend, leaving equities frozen while crypto markets trade 24/7. However, crypto assets like SOL-USD, BTC-USD, and ETH-USD are still under daily downtrends and failing to meet strict trend-following pullback criteria (not consistently above SMA20 with required confirmation triggers). Our existing positions in AAPL and MSFT are equities held through the weekend; per rule 6, equity holding patience is maintained since stocks require time to play out unless stop-loss limits are breached."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 80%): Holding equity position patiently according to rule 6 (Equity Holding Patience). Price is currently experiencing a minor unrealized loss of -0.86%, well within acceptable boundaries before hitting the hard stop-loss circuit breaker (-2.0%).
- **[HOLD] MSFT** (Confidence: 80%): Holding equity position patiently according to rule 6. Unrealized loss is minimal (-0.79%) and well clear of the stop-loss threshold. Giving the stock sufficient time to play out over the coming days.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL and MSFT positions through the weekend. Will monitor equity price action closely upon Monday market open. Do not open any new crypto positions as current trends are bearish below SMA20. Maintain high cash reserves ($25.14 USD) and wait for a clean, confirmed breakout above SMA20 with positive 1H momentum and RSI >= 32 before deploying fresh capital."
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
