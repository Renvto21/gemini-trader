# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-30 14:30:43`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.23 USD** | **$6.99 USD** | **$39.21 USD** | 🔴 **-1.97%** ($-0.79) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $346.56 | $6.99 | 📉 -0.18% | 7d 0h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Broad market conditions remain heavily defensive with major indices and equities trading below their respective SMA20 trends amidst negative 24-hour and 7-day momentum. AAPL is the sole asset maintaining a confirmed uptrend above its SMA20, demonstrating relative resilience with a minimal -0.18% PnL despite broader market headwinds. Crypto assets continue to trade in bearish trends below the SMA20, lacking valid reversal triggers with negative 1-hour or minimal green momentum."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is holding steady above its SMA20 in a confirmed uptrend. Per equity holding patience guidelines, we maintain the position as it fluctuates near breakeven (-0.18%), allowing the trade time to develop toward our +3.5% to +5.0% take-profit target.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintaining our AAPL equity holding in line with equity holding patience rules, as it remains above the SMA20. Stop-loss remains protected around -1.8% to -2.0% and take-profit targeted at +3.5% to +5.0%. Cash reserves are secured at $32.23 USD. We will continue to hold AAPL and wait for other assets to reclaim their SMA20 trends and provide valid 1-hour reversal confirmation before committing additional capital."
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
