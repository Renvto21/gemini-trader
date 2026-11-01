# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-31 21:20:44`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.23 USD** | **$6.95 USD** | **$39.17 USD** | 🔴 **-2.06%** ($-0.83) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $344.63 | $6.95 | 📉 -0.73% | 8d 7h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The majority of major equity indices and alternative assets are currently trading in bearish territory below their respective 20-day Simple Moving Averages (SMA20). Key indices and stocks such as SPY, QQQ, NVDA, and MSFT are closed and show weak daily momentum. Among crypto assets operating 24/7, BTC-USD and ETH-USD show positive 1-hour ticks and RSI levels above 32, but their overall daily trend remains bearish (below SMA20), which prevents new long entries under our strict trend-following pullback rules. AAPL is the sole position currently held, remaining in a confirmed bullish trend above its SMA20 with a current PnL of -0.73%, well within our acceptable risk limits. Given that equity markets are currently closed and crypto assets do not satisfy our trend filter, patience and capital preservation are prioritized."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL remains in a confirmed uptrend above its SMA20. Its current drawdown (-0.73%) is well within our acceptable range and far above the hard stop-loss limit. In accordance with equity holding patience guidelines, we maintain the position while awaiting further upside movement toward our +3.0% to +5.0% profit target.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Continue holding AAPL as it remains above the SMA20 trendline and has not breached the hard stop-loss threshold of -1.8% to -2.0%. Cash reserves are maintained safely at $32.23. Do not engage in crypto trading since available assets remain in a bearish trend below the SMA20. Monitor AAPL for a rebound toward our +3.0% to +5.0% profit target or exit immediately if the stop-loss is triggered. Await market re-openings for further equity pullback opportunities."
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
