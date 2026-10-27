# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-27 10:50:55`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.75 USD** | **$13.41 USD** | **$39.16 USD** | 🔴 **-2.11%** ($-0.84) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $342.98 | $6.92 | 📉 -1.21% | 3d 21h |
| `MSFT` | 0.012263 | $530.04 | $529.36 | $6.49 | 📉 -0.13% | 22h 49m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market remains mixed with major indices and equities under pressure or sitting below their SMA20, categorized as bearish trends. Among our holdings, AAPL and MSFT remain above their SMA20 despite minor intraday pullbacks. MSFT's 1-hour change is slightly negative (-0.63%), while AAPL is experiencing a mild pullback with an RSI_1h of 30.4. Neither position has hit the strict stop-loss threshold (-1.8%), and per equity holding patience rules, we maintain these positions to allow them room to recover and reach take-profit targets between +3.0% and +5.0%. No new entries are initiated as market conditions lack clear bullish continuation triggers across the broader snapshot."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 80%): AAPL is still above the SMA20 in a confirmed uptrend structure. The current minor pullback is normal price action, and holding aligns with our equity holding patience rule.
- **[HOLD] MSFT** (Confidence: 80%): MSFT remains above its SMA20 with a minor unrealized loss well within our acceptable risk limits. Patiently holding for a recovery toward our target profit zone.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain AAPL and MSFT equity positions as they remain above the SMA20 trend filter. Monitor for take-profit targets of +3.0% to +5.0% or stop-loss execution at -1.8%. Avoid opening new positions until broader market indices reclaim their SMA20 and trigger bullish reversal conditions."
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
