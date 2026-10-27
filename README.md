# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-27 14:30:58`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.75 USD** | **$13.50 USD** | **$39.24 USD** | 🔴 **-1.89%** ($-0.76) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $345.48 | $6.97 | 📉 -0.49% | 4d 0h |
| `MSFT` | 0.012263 | $530.04 | $532.52 | $6.53 | 📈 +0.47% | 1d 2h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The current market environment shows major equity indices and cryptocurrencies mostly trading below their SMA20 trend lines, presenting caution. However, our open equity positions in AAPL and MSFT remain in confirmed uptrends (above SMA20). MSFT is showing positive momentum with an hourly RSI near 71.9 and a slight gain, while AAPL remains stable after holding for 4 days. Adhering to the equity holding patience rule, we continue to hold both positions as neither has hit our strict stop-loss levels (-1.8% to -2.0%) or take-profit targets (+3.0% to +5.0%). No new crypto positions are opened due to strict trend filters (crypto assets remain below SMA20) and anti-correlation constraints."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in a confirmed uptrend (above SMA20) and complies with equity holding patience rules. Holding position steady as it has not hit stop-loss or take-profit targets.
- **[HOLD] MSFT** (Confidence: 85%): MSFT is in a confirmed uptrend (above SMA20) with positive short-term momentum. Maintaining position per equity holding patience rules while monitoring for take-profit opportunities.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing positions in AAPL and MSFT. Monitor MSFT closely as its 1-hour RSI approaches overbought levels near 72, preparing to take profit if it hits the +3.0% to +5.0% target range. Keep strict stop-loss discipline at -1.8% to -2.0%. Avoid opening crypto positions until they reclaim their SMA20 trend lines."
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
