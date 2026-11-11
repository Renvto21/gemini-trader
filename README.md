# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-11 14:50:46`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$31.84 USD** | **$6.67 USD** | **$38.52 USD** | 🔴 **-3.71%** ($-1.48) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $354.56 | $6.67 | 📈 +2.67% | 5d 21h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market shows selective strength with major indices and select equities recovering. AAPL maintains a robust uptrend above its SMA20 with a positive PnL (+2.67%), approaching overbought territory with an RSI_1h of 69.3. Cryptocurrencies like BTC-USD, ETH-USD, and SOL-USD remain below their SMA20 trend lines despite brief 1-hour green candles, categorizing them as bearish setups where we must avoid catching falling knives. SPY is showing a confirmed uptrend above the SMA20 with positive momentum, offering a potential watchlist candidate, while other equities and commodities like MSFT, GLD, and NVDA remain in a downtrend below the SMA20."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in a healthy uptrend above the SMA20 with a solid PnL of +2.67%. Following equity holding patience guidelines, we maintain the position as it continues to perform well without hitting any stop-loss or take-profit thresholds.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL position as it continues to exhibit strong uptrend behavior above the SMA20. Will monitor AAPL for potential take-profit if the RSI_1h crosses 72 or if price nears our +3% to +5% target. Cash reserves stand healthy at $31.84 USD. We maintain strict compliance with the trend filter, avoiding crypto assets and downtrending equities until a clear pullback in an established uptrend occurs with proper reversal confirmation."
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
