# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-28 15:20:55`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.23 USD** | **$6.94 USD** | **$39.17 USD** | 🔴 **-2.08%** ($-0.83) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $344.31 | $6.94 | 📉 -0.82% | 5d 1h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Major equity indices and cryptocurrencies are currently showing neutral to slight bearish short-term momentum with most assets trading below their SMA20, reflecting a cautious macroeconomic landscape. AAPL remains our sole active position, successfully maintaining its bullish trend above its SMA20 despite a minor intraday pullback. Other tracked assets fail to meet our strict trend-following filters or lack the required 1-hour reversal confirmation (positive 1-hour change)."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is still trading above its SMA20 in a confirmed uptrend, and our equity holding patience rule dictates giving stocks time to play out without reacting to minor flat or negative intraday noise, provided it stays well clear of our stop-loss limit.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain our current AAPL holding in accordance with equity holding patience guidelines as it trades above its SMA20. Monitor AAPL closely for a push toward our profit target (+3.0% to +5.0%) or maintain the stop-loss limit discipline at -1.8% to -2.0%. Ensure cash reserves stay safely above the $4.00 USD minimum threshold. Continue waiting for valid pullbacks in assets above SMA20 with RSI >= 32 and positive 1-hour percentage change before deploying new capital."
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
