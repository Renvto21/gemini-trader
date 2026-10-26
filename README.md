# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-26 12:51:09`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.75 USD** | **$13.46 USD** | **$39.21 USD** | 🔴 **-1.98%** ($-0.79) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $345.12 | $6.96 | 📉 -0.59% | 2d 23h |
| `MSFT` | 0.012263 | $530.04 | $530.14 | $6.50 | 📈 +0.02% | 49m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market shows mixed conditions, with major indices and crypto assets mostly trading below their SMA20 trend lines, denoting cautious or bearish trends. However, AAPL and MSFT remain securely in confirmed uptrends above their SMA20 lines. AAPL is experiencing a mild pullback with a -0.15% 1-hour change and an RSI of 44.7, while MSFT maintains positive momentum (+0.49% 1h, RSI 59.7). Crypto assets remain in downtrends, keeping us sidelined per the strict trend filter and anti-correlation constraints. Cash reserves are healthy at $25.75."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL remains in a confirmed uptrend above its SMA20. The current drawdown (-0.59%) is minor and well within our tolerance, adhering to the equity holding patience rule.
- **[HOLD] MSFT** (Confidence: 85%): MSFT is trading above its SMA20 with positive 1-hour momentum (+0.49%). Position is flat to slightly positive; holding for the take-profit target.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing equity positions in AAPL and MSFT as they remain in bullish uptrends above the SMA20. Respect equity holding patience and do not exit prematurely on minor fluctuations. Monitor stop-loss closely at -1.8% to -2.0% and take-profit targets between +3.0% and +5.0%. Avoid entering crypto positions while they remain below their SMA20 trend lines."
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
