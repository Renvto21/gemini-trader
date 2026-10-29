# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-29 11:31:06`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.23 USD** | **$7.06 USD** | **$39.28 USD** | 🔴 **-1.80%** ($-0.72) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $349.93 | $7.06 | 📈 +0.79% | 5d 21h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market is currently experiencing a corrective phase, with most major assets (BTC, ETH, SPY, QQQ, NVDA, GLD) trading below their SMA20 in a bearish trend. AAPL remains the sole standout in a confirmed bullish trend above SMA20, showing resilience with a daily RSI of 67.4 and positive 24h momentum (+1.77%). Most other candidates fail our strict trend filter or do not satisfy the required pullback parameters. Our open position in AAPL is currently in a minor profit (+0.79%) and adheres to our equity holding patience policy."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL remains in a confirmed uptrend above its SMA20 with positive momentum. Per equity holding patience guidelines, we are holding the position and letting it run toward our take-profit target (+3% to +5%), while protecting downside risk via our stop-loss.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL within the open portfolio. Will continue to let profits run toward the +3.0% to +5.0% target zone while maintaining a strict stop-loss at -1.8%. No new positions will be initiated due to the prevailing bearish trend across the rest of the market and adherence to our strict trend filter."
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
