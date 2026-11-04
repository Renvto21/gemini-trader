# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-04 11:30:58`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.09 USD** | **$7.00 USD** | **$39.09 USD** | 🔴 **-2.26%** ($-0.91) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012839 | $545.20 | $545.20 | $7.00 | 📈 +0.00% | 0m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The market is reacting strongly to recent political shifts with major equities and indices experiencing a relief bounce following election results. However, from a quantitative standpoint, almost all tracked assets remain in a medium-term downtrend (trading below their SMA20 lines), reflecting persistent macro headwinds. MSFT stands out as the single major asset that has successfully reclaimed its uptrend above its SMA20, backed by strong momentum (+4.85% 1-hour change and 1-hour RSI at 63.3). Cryptocurrencies show mild positive hourly movement, but remain structurally below their SMA20 thresholds, preventing any compliant crypto entries under our strict trend rules."

**Cycle Actions:**
- **[BUY] MSFT** (Confidence: 85%): MSFT is currently the only asset trading above its SMA20 in a confirmed uptrend with strong momentum (1-hour change +4.85%, 1-hour RSI 63.3). This satisfies our Rule of Gold and Reversal Confirmation triggers for a high-quality trend-following entry.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintained capital preservation protocol while screening for confirmed structural breakouts. MSFT has successfully reclaimed its SMA20 and meets all trend filter and reversal confirmation criteria. Planning to allocate $7.00 USD into MSFT as a pullback/reclaim buy. Will target a +3.5% to +5.0% gain for take-profit and strictly enforce a -2.0% stop-loss circuit breaker."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **87** | 🎯 **43.7%** (38W / 34L / 15BE) | 🔴 **$-0.77 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-04 11:30` | 🟢 BUY | `MSFT` | $7.00 | $545.20 | MSFT is currently the only asset trading above its SMA20 in a confirmed uptrend with stron... |
| `2026-11-02 11:40` | 🔴 SELL (-0.13$) | `AAPL` | $6.87 | $340.69 | AAPL has slipped further into a bearish trend below its SMA20 with a 1-hour RSI of 24.8 an... |
| `2026-10-28 13:21` | 🔴 SELL (-0.02$) | `MSFT` | $6.48 | $528.16 | MSFT has shifted to a bearish trend below its SMA20 and current performance is near our st... |
| `2026-10-26 12:01` | 🟢 BUY | `MSFT` | $6.50 | $530.04 | MSFT is in a confirmed uptrend above its SMA20, and the 1-hour RSI (62.8) and 1-hour perce... |
| `2026-10-23 13:40` | 🟢 BUY | `AAPL` | $7.00 | $347.17 | AAPL is in a confirmed uptrend above its SMA20, satisfying our strict trend filter. The 1-... |

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
