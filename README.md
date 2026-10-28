# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-28 18:30:50`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.23 USD** | **$6.93 USD** | **$39.16 USD** | 🔴 **-2.11%** ($-0.84) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $343.83 | $6.93 | 📉 -0.96% | 5d 4h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market shows Wall Street equities currently closed with frozen prices. Apple (AAPL) remains in an uptrend above its SMA20, currently exhibiting a mild pullback with a -0.96% PnL, which complies with equity holding patience guidelines. Cryptocurrencies (BTC-USD, ETH-USD, SOL-USD) are open 24/7, but all are currently trading below their SMA20 trend lines (downtrend) and lack the required positive 1-hour percentage change to trigger a reversal entry. Therefore, no crypto trades are executed and AAPL is maintained."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL remains in a confirmed uptrend above its SMA20. In accordance with equity holding patience rules, flat performance or minor pullbacks do not warrant premature selling unless the -1.8% stop-loss limit is approached.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Continue holding AAPL as it stays above the SMA20 trend line and has not hit the -1.8% stop-loss threshold. Keep monitoring crypto assets for when they reclaim their SMA20 lines and show a positive 1-hour momentum confirmation. Watch for Wall Street market hours to reopen before considering any new equity position adjustments."
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
