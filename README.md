# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-27 06:20:41`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.75 USD** | **$13.47 USD** | **$39.21 USD** | 🔴 **-1.96%** ($-0.79) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $343.91 | $6.93 | 📉 -0.94% | 3d 16h |
| `MSFT` | 0.012263 | $530.04 | $532.60 | $6.53 | 📈 +0.48% | 18h 19m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market reflects a mixed environment with major equities currently closed and crypto assets hovering near consolidation ranges under bearish daily trends. AAPL and MSFT remain our active equity holdings in confirmed uptrends above the SMA20. MSFT shows strong momentum with an RSI of 80.0, nearing our take-profit window, while AAPL experiences mild consolidation with a PnL of -0.94%. Crypto markets remain untradable due to strict trend filters, as all digital assets are positioned below their SMA20 benchmarks."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 80%): AAPL is in a confirmed uptrend above its SMA20. Per equity holding patience rules, we maintain the position despite minor consolidation, awaiting a recovery toward take-profit targets while keeping our stop-loss strict at -1.8%.
- **[HOLD] MSFT** (Confidence: 85%): MSFT is in a confirmed uptrend above its SMA20 and is currently showing strong momentum (RSI 80.0). We hold to let the winner run toward our +3.0% to +5.0% take-profit target while markets remain closed.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing equity positions in AAPL and MSFT during market closure per equity holding patience rules. Monitor MSFT for potential take-profit execution once markets reopen if momentum reaches the +3.0% to +5.0% range. Keep strict stop-loss discipline on AAPL to protect against a drop past -1.8%. Continue avoiding crypto assets until confirmed uptrends and reversal triggers emerge above the SMA20."
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
