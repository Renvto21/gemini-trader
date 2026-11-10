# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-10 13:00:55`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.01 USD** | **$13.64 USD** | **$38.65 USD** | 🔴 **-3.37%** ($-1.35) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $347.26 | $6.54 | 📈 +0.55% | 4d 19h |
| `MSFT` | 0.013089 | $534.82 | $542.95 | $7.11 | 📈 +1.52% | 3d 23h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market is exhibiting cautious conditions with major indexes like SPY and QQQ trading in bearish trends below their SMA20 lines following hot inflation data and tech sector headwinds. Cryptocurrencies remain in downtrends as well, with most down over 4% on the 24-hour window. However, our core holdings AAPL and MSFT remain resiliently positioned in confirmed uptrends above their SMA20 lines, demonstrating positive performance and respecting our equity holding patience rule."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL remains in a confirmed uptrend above its SMA20 line with positive PnL. Per equity holding patience rules, we do not rotate out of stable flat or winning positions prematurely.
- **[HOLD] MSFT** (Confidence: 90%): MSFT is in a confirmed uptrend above the SMA20 with solid positive PnL. We maintain the position to let it run toward the +3.0% to +5.0% profit target.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL and MSFT securely above their SMA20 lines. Both are showing steady performance with positive PnL (+0.55% and +1.52%). We will continue to let winners run toward our +3.0% to +5.0% profit target while respecting the hard stop-loss at -2.0%. Cash reserves are healthy at $25.01 USD. Avoid all crypto assets and downtrending equities due to bearish macro sentiment and strict trend-following filters."
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
