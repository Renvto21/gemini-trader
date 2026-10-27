# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-27 12:40:53`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.75 USD** | **$13.55 USD** | **$39.30 USD** | 🔴 **-1.76%** ($-0.70) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $347.28 | $7.00 | 📈 +0.03% | 3d 23h |
| `MSFT` | 0.012263 | $530.04 | $533.73 | $6.55 | 📈 +0.70% | 1d 0h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The portfolio currently holds two active equity positions in AAPL and MSFT, both maintaining an uptrend above their respective SMA20 lines. AAPL is up slightly by +0.03% and holding steady after 3 days, respecting equity holding patience rules. MSFT is up +0.70% with an RSI of 75.0 on the 1-hour chart, approaching our target profit zone of +3.0% to +5.0% or an extended RSI condition. Other major assets like SPY, QQQ, NVDA, and GLD remain in downtrends below their SMA20 lines, while cryptos (SOL-USD, ETH-USD, BTC-USD) are also under their SMA20 lines, reinforcing our strict trend filters to avoid buying falling knives. Cash reserves are healthy at $25.75 USD."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL remains in a confirmed uptrend above its SMA20 with positive performance. Holding in accordance with equity holding patience guidelines.
- **[HOLD] MSFT** (Confidence: 90%): MSFT is in an established uptrend above its SMA20 with a positive return of +0.70% and a 1h RSI of 75.0. Letting the winner run toward the +3.0% to +5.0% target.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain current equity positions in AAPL and MSFT. Exercise equity holding patience as per rules, letting winners run towards our +3.0% to +5.0% profit target or until 1h RSI exceeds 72 with profits >= +2.5%. Enforce the hard stop-loss circuit breaker at -1.8% to -2.0% if market conditions reverse. Continue avoiding crypto and assets trading below their SMA20 trend line."
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
