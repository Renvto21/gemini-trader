# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-06 14:50:44`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.14 USD** | **$13.44 USD** | **$38.58 USD** | 🔴 **-3.56%** ($-1.42) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $343.59 | $6.47 | 📉 -0.51% | 21h 10m |
| `MSFT` | 0.013089 | $534.82 | $532.65 | $6.97 | 📉 -0.41% | 1h 39m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The current market environment shows broad weakness across major equities and crypto assets, with most trading below their SMA20 lines reflecting lingering downward pressure. However, our existing positions in AAPL and MSFT remain above their respective SMA20 trend filters, confirming that they are higher-quality assets currently experiencing a routine pullback rather than structural breakdowns. Both holdings are within acceptable minor drawdown limits (-0.51% and -0.41%), well clear of the -1.8% stop-loss threshold. No new entries are warranted at this moment as crypto assets remain in bear trends and equities lack positive 1-hour momentum confirmation (change_1h_pct > 0.0). We adhere to equity holding patience and wait for bounce confirmations."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL remains in a confirmed uptrend above its SMA20. The current drawdown (-0.51%) is minor and well within our equity holding patience rules. We do not panic-sell flat or slightly negative positions that maintain structural uptrends.
- **[HOLD] MSFT** (Confidence: 85%): MSFT is holding above its SMA20 trend line with a minor unrealized loss of -0.41%. Equity holding patience applies here; we allow the position time to recover and play out toward our profit targets.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain patience with AAPL and MSFT holdings following strict risk parameters. Monitor stop-loss levels closely at -1.8% to -2.0% and keep take-profit targets between +3.0% and +5.0%. For any future allocation, ensure assets are in a confirmed uptrend (above SMA20) and display a positive 1-hour momentum bounce (change_1h_pct > 0.0 and rsi_1h >= 32). Preserve cash reserves above $4.00."
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
