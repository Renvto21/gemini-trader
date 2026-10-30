# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-30 11:20:42`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.23 USD** | **$6.97 USD** | **$39.19 USD** | 🔴 **-2.02%** ($-0.81) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $345.54 | $6.97 | 📉 -0.47% | 6d 21h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Broader equity and crypto markets are experiencing downward pressure across the board. Major indices like SPY, QQQ, and NVDA are trading below their SMA20 lines with weak 1-hour and daily RSI readings, signaling a bearish market environment. Cryptocurrencies (BTC-USD, ETH-USD, SOL-USD) are also in downtrends under their respective SMA20 lines, failing our trend filters. AAPL remains the sole asset showing a confirmed uptrend (above SMA20) despite a minor 1-hour pullback (-0.97%)."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is still above its SMA20 in a confirmed uptrend. Per equity holding patience guidelines, we hold the position through temporary consolidation since it has not hit the stop-loss limit and remains healthy.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "We continue to hold our AAPL position as it remains in a confirmed uptrend above the SMA20, with current PnL at -0.47%, comfortably within risk parameters and safely above our -1.8% stop-loss. We maintain our take-profit target between +3.0% and +5.0% ($357.50 to $364.50). Cash reserves stand at $32.23. No new positions will be opened today as other tracked assets are in bearish trends or lack the required positive 1-hour reversal candle confirmation (change_1h_pct > 0.0)."
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
