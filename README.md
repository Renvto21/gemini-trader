# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-10 11:41:03`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.01 USD** | **$13.72 USD** | **$38.73 USD** | 🔴 **-3.17%** ($-1.27) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $351.36 | $6.61 | 📈 +1.74% | 4d 18h |
| `MSFT` | 0.013089 | $534.82 | $542.90 | $7.11 | 📈 +1.51% | 3d 22h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Major equity indices like SPY and QQQ remain in bearish trends below their SMA20 lines following hotter-than-expected CPI reports. High-flying large-cap technology equities such as AAPL and MSFT remain resilient, maintaining confirmed uptrends above their SMA20 lines. Crypto assets (BTC-USD, ETH-USD, SOL-USD) are predominantly in downtrends below their SMA20 levels with daily RSIs depressed, failing our strict trend filter despite brief 1-hour bounce candles. Our current portfolio holdings (AAPL and MSFT) are continuing to perform well in positive territory, respecting equity holding patience guidelines."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL remains in a strong uptrend above its SMA20 with positive unrealized gains (+1.74%). Adhering to equity holding patience and asymmetric reward principles, we will let this winner run until take-profit targets or stop-loss rules are triggered.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL and MSFT as they sustain their confirmed uptrends. AAPL's 1-hour RSI is elevated at 72.5, so we will monitor for potential take-profit targets if momentum extends toward a +3% to +5% gain. MSFT is stable with positive unrealized gains. Avoid all crypto assets as they are currently trading below their SMA20 trend filters and do not meet pullback criteria. Maintain cash reserves above $4.00."
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
