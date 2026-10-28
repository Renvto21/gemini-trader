# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-28 12:12:15`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.75 USD** | **$13.44 USD** | **$39.19 USD** | 🔴 **-2.03%** ($-0.81) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $345.32 | $6.96 | 📉 -0.53% | 4d 22h |
| `MSFT` | 0.012263 | $530.04 | $528.28 | $6.48 | 📉 -0.33% | 2d 0h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market exhibits mixed technical conditions with several key indices and equities hovering near or below their SMA20, signaling caution. AAPL remains in a confirmed uptrend above its SMA20 with positive 1-hour momentum, maintaining steady posture despite minor consolidation. MSFT has dipped slightly below its SMA20 trend line, but under our equity holding patience rule, it is retained to allow recovery room as long as it respects the mandatory -1.8% circuit breaker. Crypto assets like BTC, ETH, and SOL continue to trade in bearish trends below their respective SMA20 levels, keeping them strictly off our buy list."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is maintaining a confirmed uptrend above its SMA20 with positive short-term momentum. Complying with equity holding patience, we hold the position to capture the +3.0% to +5.0% target.
- **[HOLD] MSFT** (Confidence: 80%): MSFT is currently experiencing a minor pullback below its SMA20, but its PnL (-0.33%) remains well above our strict -1.8% circuit breaker. Per equity patience guidelines, we give the stock time to recover.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Continue holding AAPL and MSFT patiently according to equity holding rules, watching for profit targets (+3.0% to +5.0%) on AAPL and monitoring MSFT closely to ensure it avoids hitting the -1.8% stop-loss circuit breaker. Keep crypto exposure at zero due to persistent downtrends below SMA20. Maintain robust cash reserves of at least $4.00 USD and wait for strong trend-following pullback confirmations before executing new trades."
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
