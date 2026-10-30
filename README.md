# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-30 14:20:39`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.23 USD** | **$7.00 USD** | **$39.22 USD** | 🔴 **-1.94%** ($-0.78) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $347.12 | $7.00 | 📉 -0.01% | 7d 0h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Broader market conditions reflect broad-based weakness with major indices and equities (SPY, QQQ, NVDA, MSFT) trading in bearish territory below their SMA20 lines. AAPL remains the sole high-quality asset maintaining an uptrend above its SMA20 with stable relative strength, while crypto assets are currently suppressed below key trend filters."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL remains comfortably above its SMA20 in a confirmed uptrend with a healthy daily RSI of 58.9. Following equity holding patience guidelines, we maintain the position as it oscillates near our entry price, waiting for the take-profit target (+3.5% to +5.0%) while keeping our stop-loss strict at -1.8% to -2.0%.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintaining our existing AAPL position in adherence to equity holding patience guidelines as it holds its uptrend above the SMA20. PnL is near flat (-0.01%). Stop-loss remains protected at -1.8% to -2.0% and take-profit target at +3.5% to +5.0%. Cash reserves are maintained at $32.23 USD. No new entries will be made until confirmed uptrend assets display a valid 1-hour reversal trigger."
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
