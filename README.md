# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-29 20:40:42`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.23 USD** | **$7.04 USD** | **$39.26 USD** | 🔴 **-1.85%** ($-0.74) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $348.91 | $7.04 | 📈 +0.50% | 6d 6h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader equity markets (SPY, QQQ, NVDA, MSFT, GLD) and cryptocurrencies (BTC-USD, ETH-USD, SOL-USD) remain largely under downward pressure, trading below their respective SMA20 lines. AAPL is the sole asset maintaining a confirmed uptrend above its SMA20 with stable performance (current PnL +0.5%). Wall Street markets are currently closed (CERRADO), and crypto assets are showing negative 1-hour percentage changes and bearish momentum without a confirmed green candle bounce above our required trigger parameters. Therefore, adherence to equity patience and strict filtering is necessary."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL remains in a confirmed uptrend above the SMA20 with positive PnL (+0.5%). Under equity holding patience rules, we do not rotate or sell flat positions prematurely, waiting for the target +3.0% to +5.0% gain or an RSI 1H > 72 while respecting the stop-loss.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Continue holding AAPL under equity holding patience rules, as it is our only position above the SMA20 uptrend filter (currently at $348.91, +0.5% PnL). Monitor AAPL for take-profit targets between +3.0% and +5.0% ($357.60 to $366.60) or an RSI 1H > 72, while strictly respecting the -2.0% stop-loss circuit breaker. Keep all crypto and other assets sidelined due to closed market hours, bearish trends below SMA20, or lack of clear positive 1-hour reversal confirmation."
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
