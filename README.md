# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-27 11:50:50`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.75 USD** | **$13.50 USD** | **$39.25 USD** | 🔴 **-1.87%** ($-0.75) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $345.83 | $6.97 | 📉 -0.39% | 3d 22h |
| `MSFT` | 0.012263 | $530.04 | $532.62 | $6.53 | 📈 +0.49% | 23h 49m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market remains largely in a cautious or bearish trend on the daily timeframe, with major indices and crypto assets trading below their respective SMA20 lines. However, our currently held equities, AAPL and MSFT, remain securely above their SMA20 lines in confirmed uptrends. AAPL is experiencing a mild pullback (-0.39% PnL) with 1h RSI at 39.2, holding well within normal consolidation parameters. MSFT is showing a positive return (+0.49% PnL) with strong 1h momentum. No immediate stop-loss or take-profit triggers have been reached yet, adhering to the principle of equity holding patience."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 80%): AAPL remains in a confirmed uptrend above its SMA20. The current drawdown (-0.39%) is minor, and equity holding patience dictates letting the position play out without premature exits.
- **[HOLD] MSFT** (Confidence: 85%): MSFT is in a confirmed uptrend above its SMA20 and currently shows a positive PnL (+0.49%). Holding position to allow momentum to approach the +3.0% to +5.0% take-profit target.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing positions AAPL and MSFT. Monitor both assets for take-profit targets between +3.0% and +5.0%, or strict stop-loss discipline if positions drop past -1.8% to -2.0%. Keep cash reserves intact and avoid initiating any crypto positions since all crypto assets are currently below their SMA20 trend lines."
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
