# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-30 16:10:40`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.23 USD** | **$6.92 USD** | **$39.14 USD** | 🔴 **-2.15%** ($-0.86) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $343.04 | $6.92 | 📉 -1.19% | 7d 2h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market is currently experiencing a strong pullback, with major indices and equities like SPY, QQQ, NVDA, and MSFT trading below their SMA20 trend lines in bearish territory, accompanied by deeply oversold daily RSI levels. AAPL is the only asset in our universe maintaining a confirmed uptrend (above its SMA20), though its current PnL is slightly negative at -1.19%. Cryptocurrencies (SOL-USD, BTC-USD, ETH-USD) are also lingering below their SMA20 lines, failing our reversal criteria since their 1-hour percentage changes are either flat or negative. Given our strict trend filters and patience rules for equities, we will continue holding AAPL and avoid taking any new positions until market conditions stabilize and reclaim uptrends."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is currently in a confirmed uptrend (above SMA20) and our holding time rules dictate patience for equities rather than premature rotation. PnL is at -1.19%, well within our risk parameters and safely away from the -2.0% stop-loss limit.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "We are maintaining our AAPL holding as it remains above the SMA20 trendline, despite a minor pullback. Current PnL is -1.19%, safely above our strict -2.0% stop-loss threshold. We will exercise equity holding patience, monitoring for an upside momentum push towards a +3.0% to +5.0% profit target. No new positions will be opened across stocks or cryptos until assets reclaim their SMA20 lines and fulfill our strict reversal confirmation triggers (1-hour RSI >= 32 and positive 1-hour change)."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **86** | 🎯 **44.2%** (38W / 33L / 15BE) | 🔴 **$-0.64 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-28 13:21` | 🔴 SELL (-0.02$) | `MSFT` | $6.48 | $528.16 | MSFT has shifted to a bearish trend below its SMA20 and current performance is near our st... |
| `2026-10-26 12:01` | 🟢 BUY | `MSFT` | $6.50 | $530.04 | MSFT is in a confirmed uptrend above its SMA20, and the 1-hour RSI (62.8) and 1-hour perce... |
| `2026-10-23 13:40` | 🟢 BUY | `AAPL` | $7.00 | $347.17 | AAPL is in a confirmed uptrend above its SMA20, satisfying our strict trend filter. The 1-... |
| `2026-10-22 16:00` | 🔴 SELL (-0.12$) | `MSFT` | $6.88 | $521.40 | MSFT has dropped to a PnL of -1.71%, closely approaching our mandatory stop-loss threshold... |
| `2026-10-22 14:40` | 🔴 SELL (+0.17$) | `AAPL` | $10.17 | $346.52 | AAPL rsi_1h has surpassed 72 (currently 73.4) with a positive return of +1.73%, satisfying... |

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
