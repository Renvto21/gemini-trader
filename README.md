# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-26 12:01:15`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.75 USD** | **$13.49 USD** | **$39.24 USD** | 🔴 **-1.91%** ($-0.76) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $346.58 | $6.99 | 📉 -0.17% | 2d 22h |
| `MSFT` | 0.012263 | $530.04 | $530.04 | $6.50 | 📈 +0.00% | 0m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market shows a mixed environment with most broad indexes and assets remaining in a downtrend below their SMA20, except for MSFT and AAPL which are confirmed in an uptrend (ALCISTA sobre SMA20). AAPL position is currently held with a minor drawdown of -0.17%, well within normal equity holding patience guidelines. MSFT is showing positive momentum (rsi_1h at 62.8, change_1h_pct at +0.41%, and above SMA20), presenting a valid pullback entry opportunity."

**Cycle Actions:**
- **[BUY] MSFT** (Confidence: 85%): MSFT is in a confirmed uptrend above its SMA20, and the 1-hour RSI (62.8) and 1-hour percentage change (+0.41%) confirm a solid bounce from the pullback, satisfying our strict trend filter and reversal confirmation trigger.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain current AAPL position respecting equity holding patience and our stop-loss/take-profit boundaries (+3% to +5% target or RSI 1h > 72 with profit >= +2.5%, stop-loss at -1.8%). Entered MSFT following strict trend-following pullback rules as it is above SMA20 with positive 1h change and rsi_1h >= 32. Continue to preserve cash reserves above the $4.00 minimum and monitor crypto assets for future setups once uptrends are confirmed."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **85** | 🎯 **44.7%** (38W / 32L / 15BE) | 🔴 **$-0.62 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-26 12:01` | 🟢 BUY | `MSFT` | $6.50 | $530.04 | MSFT is in a confirmed uptrend above its SMA20, and the 1-hour RSI (62.8) and 1-hour perce... |
| `2026-10-23 13:40` | 🟢 BUY | `AAPL` | $7.00 | $347.17 | AAPL is in a confirmed uptrend above its SMA20, satisfying our strict trend filter. The 1-... |
| `2026-10-22 16:00` | 🔴 SELL (-0.12$) | `MSFT` | $6.88 | $521.40 | MSFT has dropped to a PnL of -1.71%, closely approaching our mandatory stop-loss threshold... |
| `2026-10-22 14:40` | 🔴 SELL (+0.17$) | `AAPL` | $10.17 | $346.52 | AAPL rsi_1h has surpassed 72 (currently 73.4) with a positive return of +1.73%, satisfying... |
| `2026-10-21 12:01` | 🟢 BUY | `MSFT` | $7.00 | $530.45 | MSFT is in a confirmed uptrend above its SMA20. The 1-hour RSI is at 36.7 (above the 32 th... |

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
