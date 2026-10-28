# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-28 12:41:02`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.75 USD** | **$13.44 USD** | **$39.19 USD** | 🔴 **-2.04%** ($-0.81) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $345.34 | $6.96 | 📉 -0.53% | 4d 23h |
| `MSFT` | 0.012263 | $530.04 | $527.95 | $6.47 | 📉 -0.39% | 2d 0h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The current market environment shows mixed conditions, with equities like SPY remaining in a confirmed uptrend above the SMA20, while tech heavyweights like MSFT have slipped below their SMA20 trend line, currently showing a slight pullback. Cryptocurrencies continue to trade in a downtrend below their respective SMA20 levels, meaning our strict trend and reversal filters keep us out of crypto assets. Our portfolio currently holds AAPL (in a confirmed uptrend) and MSFT, which has drifted slightly below its SMA20 but remains well above our mandatory -1.8% to -2.0% stop-loss circuit breaker."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 80%): AAPL remains in a confirmed uptrend above its SMA20 with a stable daily RSI. Per equity holding patience rules, we do not rotate or sell flat positions prematurely without hitting a take-profit target or stop-loss.
- **[HOLD] MSFT** (Confidence: 70%): MSFT has slipped below the SMA20 and is showing a minor loss (-0.39%), but it has not triggered our mandatory stop-loss threshold (-1.8% to -2.0%). We retain the position while monitoring downside risk strictly.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain patience with AAPL as it holds its uptrend, giving equity positions time to play out per holding rules. Monitor MSFT closely; its trend has turned bearish (below SMA20), so if it approaches the -1.8% stop-loss limit, cut the position immediately. SPY is showing strong 1-hour momentum and is in an uptrend, but its 1-hour RSI is elevated (79.8), so wait for a mild pullback before entering. Keep cash reserves secure above $4.00 USD."
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
