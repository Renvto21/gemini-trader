# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-09 15:00:53`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.14 USD** | **$20.65 USD** | **$38.79 USD** | 🔴 **-3.03%** ($-1.21) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $349.28 | $6.57 | 📈 +1.14% | 3d 21h |
| `MSFT` | 0.013089 | $534.82 | $544.18 | $7.12 | 📈 +1.75% | 3d 1h |
| `GLD` | 0.018501 | $378.35 | $375.92 | $6.96 | 📉 -0.64% | 3h 30m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market is showing signs of recovery with major tech and equities trading positively over the 24-hour period, though some assets remain under their SMA20 daily trends. Among our holdings, AAPL and MSFT remain strong in confirmed uptrends above their SMA20, while GLD experiences minor near-term consolidation but holds a solid bullish daily structure. Crypto assets like BTC, ETH, and SOL continue to trade below their SMA20 lines without meeting the strict 1-hour positive momentum confirmation criteria, meaning we maintain zero crypto exposure to avoid falling knife risks. Our active equity positions are demonstrating resilience, and we maintain discipline by adhering to our stop-loss and take-profit parameters."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is in a confirmed uptrend above its SMA20 with solid positive performance. Holding to let winners run towards our +3.5% to +5.0% profit target.
- **[HOLD] MSFT** (Confidence: 90%): MSFT continues to trade above its SMA20 in a confirmed uptrend. Maintaining position patience per equity holding rules.
- **[HOLD] GLD** (Confidence: 85%): GLD remains above its SMA20 line despite minor intraday pullback. Giving the asset time to play out without premature rotation.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain current holdings in AAPL, MSFT, and GLD. Monitor stop-loss levels strictly at -1.8% to -2.0% and allow winners to run towards +3.5% to +5.0% profit targets. No new buy orders are executed in this cycle as candidates do not fulfill all simultaneous trend and positive 1-hour momentum confirmation triggers."
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
