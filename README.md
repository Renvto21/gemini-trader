# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-05 09:20:50`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$31.78 USD** | **$6.96 USD** | **$38.74 USD** | 🔴 **-3.15%** ($-1.26) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.002886 | $2425.59 | $2410.11 | $6.96 | 📉 -0.64% | 7h 39m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market shows equities and traditional assets closed for the session. In the crypto sector, ETH-USD remains in a confirmed uptrend above its SMA20 but is currently experiencing a minor pullback with a 1-hour RSI of 34.9 and a negative 1-hour change (-0.35%), meaning the rebound trigger (change_1h_pct > 0.0) has not yet been met. We currently hold ETH-USD and must wait for price stabilization and confirmation before adding or exiting. AAPL and MSFT are in confirmed uptrends but their markets are closed. All other assets are currently trading below their SMA20 trend filters."

**Cycle Actions:**
- **[HOLD] ETH-USD** (Confidence: 80%): ETH-USD remains above its SMA20 in a valid uptrend. Although the 1-hour change is currently negative (-0.35%), the position has not breached the strict stop-loss threshold (-2.0%). Maintaining the position in adherence with holding patience and risk management rules.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Currently holding ETH-USD with a small unrealized loss (-0.64%). Monitoring the 1-hour change and RSI to ensure the position remains above the stop-loss limit of -2.0%. Will hold the position until a clear reversal or profit target (+3.0% to +5.0%) is reached. No new buys are initiated since crypto 1-hour candles are still slightly negative."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **88** | 🎯 **43.2%** (38W / 35L / 15BE) | 🔴 **$-1.08 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-05 01:41` | 🟢 BUY | `ETH-USD` | $7.00 | $2425.59 | ETH-USD is in a confirmed uptrend above its SMA20, market status is open 24/7, 1-hour RSI ... |
| `2026-11-04 22:00` | 🔴 SELL (-0.31$) | `MSFT` | $6.69 | $520.99 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -4.44% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-04 11:30` | 🟢 BUY | `MSFT` | $7.00 | $545.20 | MSFT is currently the only asset trading above its SMA20 in a confirmed uptrend with stron... |
| `2026-11-02 11:40` | 🔴 SELL (-0.13$) | `AAPL` | $6.87 | $340.69 | AAPL has slipped further into a bearish trend below its SMA20 with a 1-hour RSI of 24.8 an... |
| `2026-10-28 13:21` | 🔴 SELL (-0.02$) | `MSFT` | $6.48 | $528.16 | MSFT has shifted to a bearish trend below its SMA20 and current performance is near our st... |

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
