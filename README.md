# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-23 19:00:53`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.25 USD** | **$7.01 USD** | **$39.26 USD** | 🔴 **-1.85%** ($-0.74) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $347.73 | $7.01 | 📈 +0.16% | 5h 20m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "All major equity markets and gold are currently closed (CERRADO) with frozen prices, keeping active liquidity restricted to cryptocurrencies which are open 24/7. However, all available cryptocurrencies (BTC-USD, ETH-USD, SOL-USD) are currently in a downtrend below their SMA20, violating our strict trend filter rule against catching falling knives. Meanwhile, our single equity position in AAPL is healthy, trading in a confirmed uptrend above SMA20 with a current PnL of +0.16% after 5h 20m of holding time. Given equity holding patience and market closures, no new buys or sells are warranted at this moment."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): AAPL is currently in a confirmed uptrend above SMA20 with positive PnL (+0.16%). Market is closed (CERRADO), and equity holding patience mandates keeping the position until take-profit (+3.0% to +5.0% or rsi_1h > 72) or stop-loss (-1.8% to -2.0%) triggers.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL patiently as mandated by equity holding patience rules. AAPL is in an uptrend (above SMA20) with rsi_1h at 66.0; monitoring for take-profit criteria if rsi_1h surpasses 72 or price achieves a +3.0% to +5.0% gain upon market reopening. Stop-loss remains firmly respected at -1.8% to -2.0%. Cryptocurrencies are avoided due to being in bearish trends despite being open 24/7. Cash reserve is $32.25."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **85** | 🎯 **44.7%** (38W / 32L / 15BE) | 🔴 **$-0.62 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-23 13:40` | 🟢 BUY | `AAPL` | $7.00 | $347.17 | AAPL is in a confirmed uptrend above its SMA20, satisfying our strict trend filter. The 1-... |
| `2026-10-22 16:00` | 🔴 SELL (-0.12$) | `MSFT` | $6.88 | $521.40 | MSFT has dropped to a PnL of -1.71%, closely approaching our mandatory stop-loss threshold... |
| `2026-10-22 14:40` | 🔴 SELL (+0.17$) | `AAPL` | $10.17 | $346.52 | AAPL rsi_1h has surpassed 72 (currently 73.4) with a positive return of +1.73%, satisfying... |
| `2026-10-21 12:01` | 🟢 BUY | `MSFT` | $7.00 | $530.45 | MSFT is in a confirmed uptrend above its SMA20. The 1-hour RSI is at 36.7 (above the 32 th... |
| `2026-10-21 10:10` | 🔴 SELL (+0.12$) | `ETH-USD` | $10.07 | $2481.87 | ETH-USD rsi_1h has surpassed 72 (currently 73.7) with a positive return of +1.21%, satisfy... |

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
