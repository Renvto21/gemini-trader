# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-11 15:50:42`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$31.84 USD** | **$6.68 USD** | **$38.53 USD** | 🔴 **-3.68%** ($-1.47) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $355.16 | $6.68 | 📈 +2.84% | 5d 22h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market is showing mixed recovery signals. Key equity indices like SPY and AAPL remain in confirmed uptrends above their SMA20, with AAPL currently sitting at a +2.84% gain, nearing our +3.5% to +5.0% profit-taking target. Conversely, most tech names, crypto assets, and commodities remain in bearish trends below their SMA20 or exhibit weak pullback confirmations. Adhering strictly to our trend-filtering and anti-catch-falling-knife rules, we avoid buying assets in downtrends. SPY is above SMA20 with a positive 1-hour candle and an RSI of 68.9, presenting a potential secondary entry opportunity, but we keep our cash reserves stable while letting our core AAPL winner run."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in a confirmed uptrend above SMA20 with a current PnL of +2.84%. Adhering to equity holding patience and asymmetric risk/reward principles, we hold the position as it approaches the +3.5% to +5.0% profit target window.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL position as it approaches the +3.5% to +5.0% profit target window, maintaining discipline per equity patience rules. Keep monitoring SPY for potential pullback additions if market conditions remain favorable. Respect strict stop-loss levels (-1.8% to -2.0%) and avoid crypto or downtrend assets."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **91** | 🎯 **41.8%** (38W / 38L / 15BE) | 🔴 **$-1.52 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-11 12:20` | 🔴 SELL (-0.17$) | `MSFT` | $6.83 | $521.92 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -2.41% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-10 11:31` | 🔴 SELL (-0.12$) | `GLD` | $6.87 | $371.60 | GLD has fallen below its SMA20 trend line and its current PnL is approaching the strict st... |
| `2026-11-09 11:30` | 🟢 BUY | `GLD` | $7.00 | $378.35 | GLD is in a confirmed uptrend above its SMA20, market status is open, 1-hour momentum is s... |
| `2026-11-06 13:10` | 🟢 BUY | `MSFT` | $7.00 | $534.82 | MSFT is in a confirmed uptrend above its SMA20, market status is open, 1-hour RSI has reco... |
| `2026-11-05 17:40` | 🟢 BUY | `AAPL` | $6.50 | $345.35 | AAPL is in a confirmed uptrend above its SMA20, market status is open, and 1-hour momentum... |

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
