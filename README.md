# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-10 15:20:50`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.01 USD** | **$13.49 USD** | **$38.50 USD** | 🔴 **-3.74%** ($-1.50) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $347.85 | $6.55 | 📈 +0.72% | 4d 21h |
| `MSFT` | 0.013089 | $534.82 | $530.60 | $6.94 | 📉 -0.79% | 4d 2h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market is currently experiencing a pullback, with key indices and many prominent assets dipping below their SMA20 lines, indicating short-term bearish pressure. AAPL remains the sole notable asset maintaining an uptrend above its SMA20 line, though its 1-hour momentum has turned slightly negative. Crypto assets like BTC, ETH, and SOL continue to hover in oversold daily RSI territory, but lack confirmed sustained green candles meeting our strict reversal criteria. MSFT has slipped below the SMA20 threshold, putting its PnL slightly into negative territory (-0.79%), but given equity holding patience rules, it remains well above the strict stop-loss floor."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL remains in a confirmed uptrend above its SMA20 and is currently in profit (+0.72%). Adhering to equity holding patience and asymmetric risk/reward to let the winner run.
- **[HOLD] MSFT** (Confidence: 85%): MSFT is currently experiencing a minor drawdown (-0.79%) but is well above our strict -1.8% to -2.0% stop-loss floor. Giving equities time to play out per strategy rules.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing positions in AAPL and MSFT, exercising strict equity holding patience as neither has hit the -1.8% to -2.0% stop-loss threshold. Monitor MSFT closely since it has dipped below the SMA20 line; if it breaches the stop-loss level, cut immediately. Keep crypto and other potential buy targets sidelined until a clear uptrend reasserts itself above the SMA20 accompanied by confirmed 1-hour green candles and RSI >= 32. Preserve the $25.01 cash buffer."
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
