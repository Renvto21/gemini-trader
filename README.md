# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-11 11:50:40`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.01 USD** | **$13.59 USD** | **$38.60 USD** | 🔴 **-3.50%** ($-1.40) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $353.65 | $6.66 | 📈 +2.40% | 5d 18h |
| `MSFT` | 0.013089 | $534.82 | $529.72 | $6.93 | 📉 -0.95% | 4d 22h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The equity market is showing mixed recovery signals, with tech rebounding following strong earnings sentiment from infrastructure plays like CoreWeave. AAPL remains exceptionally strong, maintaining a confirmed uptrend above its SMA20 with solid positive momentum (+1.44% 1h change, RSI 1H at 60.3), approaching our early take-profit objective. MSFT has slipped slightly below its SMA20 trend line with a negative 1h change, placing its PnL near our tactical threshold, but we exercise equity holding patience per our core rules. Cryptocurrencies and several major index ETFs remain under their respective SMA20 lines, failing strict trend filters. No new buy signals satisfy all strict pullback rules across the board today."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in a confirmed uptrend above its SMA20 with strong positive momentum. PnL is currently +2.4%, approaching our target of +3.0% to +5.0%. Exercising equity holding patience and letting the winner run.
- **[HOLD] MSFT** (Confidence: 80%): MSFT is currently experiencing a minor dip below its SMA20 trend line with a PnL of -0.95%. Per our equity holding patience and risk rules, we do not panic sell on flat or minor noise unless the hard circuit breaker (-1.8% to -2.0%) is hit.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain AAPL and MSFT positions, exercising equity holding patience. Monitor AAPL closely for take-profit targets (+3.0% to +5.0%) if RSI extends past 72. Keep strict stop-loss rules active (-1.8% to -2.0%) for MSFT and overall capital protection. Refrain from opening new positions until target assets fulfill all strict quantitative filters (above SMA20, 1H RSI >= 32, and 1H change > 0.0%). Maintain cash reserves above $4.00 USD."
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
