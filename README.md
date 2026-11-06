# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-06 01:50:41`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.14 USD** | **$6.48 USD** | **$38.61 USD** | 🔴 **-3.46%** ($-1.39) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $344.17 | $6.48 | 📉 -0.34% | 8h 9m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The traditional equity and ETF markets are currently closed ('CERRADO'), with prices frozen following a sharp broad market pullback. Major indices like QQQ, SPY, and NVDA are in established bear trends below their SMA20 lines. Meanwhile, crypto markets (BTC, ETH, SOL) remain open 24/7 but continue to trade under strong downward pressure, all exhibiting downtrends and negative 1-hour momentum, failing the strict quantitative reversal trigger (rsi_1h >= 32 and change_1h_pct > 0.0). Our only active position is AAPL, which is currently closed. Although down slightly by -0.34%, it remains above its SMA20 in a confirmed daily uptrend. Following operational rules, patience must be exercised during market closure without prematurely rotating or cutting positions that have not hit stop-loss limits."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is currently in a closed market status ('CERRADO') while holding a minor unrealized loss of -0.34%. Per operational guidelines for equities, we maintain position patience and do not liquidate flat or slightly negative positions unless stop-loss limits (-1.8% to -2.0%) are breached upon market reopening.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain AAPL position patiently while markets remain closed. Watch for profit target between +3.0% and +5.0% or protect capital via the hard circuit breaker stop-loss between -1.8% and -2.0% upon market reopening. Keep all crypto assets excluded due to persistent downtrends, low 1H RSI, and negative 1H returns. Ensure cash reserve remains above $4.00 minimum."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **89** | 🎯 **42.7%** (38W / 36L / 15BE) | 🔴 **$-1.23 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-05 17:40` | 🟢 BUY | `AAPL` | $6.50 | $345.35 | AAPL is in a confirmed uptrend above its SMA20, market status is open, and 1-hour momentum... |
| `2026-11-05 11:20` | 🔴 SELL (-0.15$) | `ETH-USD` | $6.85 | $2374.60 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -2.10% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-05 01:41` | 🟢 BUY | `ETH-USD` | $7.00 | $2425.59 | ETH-USD is in a confirmed uptrend above its SMA20, market status is open 24/7, 1-hour RSI ... |
| `2026-11-04 22:00` | 🔴 SELL (-0.31$) | `MSFT` | $6.69 | $520.99 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -4.44% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-04 11:30` | 🟢 BUY | `MSFT` | $7.00 | $545.20 | MSFT is currently the only asset trading above its SMA20 in a confirmed uptrend with stron... |

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
