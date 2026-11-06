# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-06 17:00:54`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.14 USD** | **$13.43 USD** | **$38.57 USD** | 🔴 **-3.58%** ($-1.43) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $343.32 | $6.46 | 📉 -0.59% | 23h 20m |
| `MSFT` | 0.013089 | $534.82 | $532.35 | $6.97 | 📉 -0.46% | 3h 50m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market remains mostly under pressure with multiple indices and equities trading below their SMA20 lines, indicating prevailing medium-term weakness. Wall Street equities (AAPL, MSFT) are currently open, though AAPL has temporarily dipped below its SMA20 on the snapshot, reinforcing patience as per equity holding rules. Cryptocurrencies are open 24/7, but none currently meet the strict trend and bounce confirmation filter (rsi_1h >= 32 and change_1h_pct > 0 in a confirmed uptrend). Capital preservation is prioritized with adequate cash reserves."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 80%): Holding AAPL per equity patience rule. Current drawdown is minimal (-0.59%), well above the stop-loss threshold. Maintaining position to let the trade play out.
- **[HOLD] MSFT** (Confidence: 85%): Holding MSFT as it remains above its SMA20 trend line with a minimal drawdown (-0.46%). Complying with equity holding patience rules.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Currently holding AAPL and MSFT. Although AAPL shows a brief dip below its SMA20, equity patience rule applies (do not rotate or sell flat/minor drawdown positions prematurely without hitting the -1.8% to -2.0% stop-loss). Will continue monitoring for bounce confirmations on uptrend assets while preserving the $4.00 cash reserve floor."
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
