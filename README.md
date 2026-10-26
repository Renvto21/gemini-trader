# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-26 13:11:03`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.75 USD** | **$13.44 USD** | **$39.19 USD** | 🔴 **-2.03%** ($-0.81) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $344.11 | $6.94 | 📉 -0.88% | 2d 23h |
| `MSFT` | 0.012263 | $530.04 | $530.09 | $6.50 | 📈 +0.01% | 1h 9m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market is mixed with major indices such as QQQ, SPY, and NVDA currently trading in bearish territory below their SMA20 lines. Among our current holdings, MSFT remains in a confirmed uptrend above the SMA20 with positive 1-hour momentum, while AAPL is experiencing a minor pullback after nearly 3 days of holding. AAPL's 1-hour RSI has dipped to 40.8 and change_1h_pct is negative (-0.45%), but it remains above its SMA20 trend line, respecting equity holding patience rules. Cryptocurrencies continue to trade below their SMA20 trends, confirming that we should remain entirely out of crypto positions to avoid duplicate downside correlation risk."

**Cycle Actions:**
- *No changes this cycle (HOLD)*

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain AAPL and MSFT positions in accordance with equity holding patience guidelines. Do not exit AAPL prematurely on minor fluctuations despite the negative 1h percentage change, as it remains in a valid bullish uptrend above the SMA20. Keep a close watch on the stop-loss threshold (-1.8% to -2.0%) for AAPL which is currently down -0.88%. Target profit taking for both positions between +3.0% and +5.0%. Avoid all crypto assets since they are trading below the SMA20 trend line."
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
