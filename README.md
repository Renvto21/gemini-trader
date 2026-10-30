# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-30 14:00:52`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.23 USD** | **$6.99 USD** | **$39.22 USD** | 🔴 **-1.95%** ($-0.78) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $346.90 | $6.99 | 📉 -0.08% | 7d 0h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The macro and technical conditions show widespread weakness across major equity indices and assets, with SPY, QQQ, NVDA, and GLD all trading below their SMA20 lines in a bearish posture. AAPL is the sole asset maintaining a confirmed uptrend (above SMA20) and a healthy daily RSI, while our existing AAPL position remains remarkably resilient, hovering near break-even despite the broader market turbulence. Cryptocurrencies are open 24/7, but none currently meet our strict trend filter and reversal confirmation pullback criteria simultaneously on a confirmed uptrend."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is currently the only asset holding a confirmed uptrend above its SMA20. Per equity holding patience rules, we maintain the position as it is flat and healthy despite broader market weakness.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding our single AAPL position in line with equity holding patience guidelines, as it remains above the SMA20 trend filter and near break-even (-0.08%). Will maintain cash reserves and patiently wait for either a take-profit target (+3.5% to +5.0%) or a strict stop-loss trigger (-1.8%). No new entries will be made until additional pullback opportunities emerge in confirmed uptrend assets."
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
