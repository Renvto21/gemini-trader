# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-10 14:20:39`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.01 USD** | **$13.67 USD** | **$38.68 USD** | 🔴 **-3.31%** ($-1.32) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $348.06 | $6.55 | 📈 +0.78% | 4d 20h |
| `MSFT` | 0.013089 | $534.82 | $543.62 | $7.12 | 📈 +1.65% | 4d 1h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Major equity indices and the broader market remain under moderate pressure, with many assets trading below their SMA20 trend line. However, our core equity holdings (AAPL and MSFT) continue to demonstrate relative strength, maintaining positions above their SMA20 with positive daily and hourly momentum. Crypto assets are showing oversold conditions but remain in overall downtrends below their SMA20, prompting us to maintain a cautious stance and adhere strictly to our anti-trend and anti-correlation filters."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL remains in a confirmed uptrend above its SMA20 with positive momentum (+0.78% PnL). Adhering to the equity holding patience rule, we continue to let the winner run toward our +3.0% to +5.0% profit target.
- **[HOLD] MSFT** (Confidence: 90%): MSFT continues to trade above its SMA20 in a solid uptrend with a positive PnL (+1.65%). Maintaining patience and giving the stock room to play out toward our profit targets while keeping stops protected.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL and MSFT comfortably in confirmed uptrends above their SMA20. Monitor closely for profit targets between +3.0% and +5.0% or maintain patience while respecting the hard stop-loss at -2.0%. Avoid all downtrended assets and crypto until structural trend reversals and positive momentum confirmations are achieved."
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
