# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-26 11:41:06`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.25 USD** | **$6.97 USD** | **$39.22 USD** | 🔴 **-1.95%** ($-0.78) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $345.73 | $6.97 | 📉 -0.41% | 2d 22h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market continues to exhibit cautious consolidation with major indices like SPY, QQQ, and NVDA trading below their SMA20 lines, reflecting a broader bearish macro trend. Cryptocurrencies such as SOL-USD, ETH-USD, and BTC-USD are also currently in a downtrend below their respective SMA20 levels, keeping our anti-correlation and trend-following filters restricted. Among equities, MSFT and AAPL are maintaining an uptrend above their SMA20. Our existing position in AAPL is experiencing a mild drawdown of -0.41%, well above our hard stop-loss threshold of -1.8%. Following equity holding patience rules, we will hold AAPL to let it develop rather than rotating out prematurely."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is currently in a confirmed uptrend (above SMA20) with a mild, acceptable unrealized loss of -0.41%. Following equity holding patience rules, we do not rotate or sell flat/mildly negative equity positions prematurely unless the hard stop-loss of -1.8% is breached or our take-profit target is achieved.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain the current AAPL position respecting equity holding patience, monitoring closely for either a push toward a take-profit target (RSI 1h > 72 with profit >= +2.5%) or a strict stop-loss trigger at -1.8%. Cash reserves stand at $32.25, ensuring we maintain well above the $4.00 minimum. Keep monitoring MSFT and other uptrend assets for potential pullback entries when strict reversal confirmation criteria (rsi_1h >= 32 and positive 1-hour change) are met."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **85** | 🎯 **44.7%** (38W / 32L / 15BE) | 🔴 **$-0.62 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-23 13:40` | 🟢 BUY | `AAPL` | $7.00 | $347.17 | AAPL is in a confirmed uptrend above its SMA20, satisfying our strict trend filter. The 1-... |
| `2026-10-22 16:00` | 🔴 SELL (-0.12$) | `MSFT` | $6.88 | $521.40 | MSFT has dropped to a PnL of -1.71%, closely approaching our mandatory stop-loss threshold... |
| `2026-10-22 14:40` | 🔴 SELL (+0.17$) | `AAPL` | $10.17 | $346.52 | AAPL rsi_1h has surpassed 72 (currently 73.4) with a positive return of +1.73%, satisfying... |
| `2026-10-21 12:01` | 🟢 BUY | `MSFT` | $7.00 | $530.45 | MSFT is in a confirmed uptrend above its SMA20. The 1-hour RSI is at 36.7 (above the 32 th... |
| `2026-10-21 10:10` | 🔴 SELL (+0.12$) | `ETH-USD` | $10.07 | $2481.87 | ETH-USD rsi_1h has surpassed 72 (currently 73.7) with a positive return of +1.21%, satisfy... |

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
