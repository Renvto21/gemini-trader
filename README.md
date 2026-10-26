# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-26 09:40:57`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.25 USD** | **$7.01 USD** | **$39.26 USD** | 🔴 **-1.85%** ($-0.74) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $347.73 | $7.01 | 📈 +0.16% | 2d 20h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market is currently experiencing a weekend shutdown for equities, with all tracked stocks and ETFs showing a status of 'CERRADO' and trading below their SMA20 trend lines in bearish setups. Cryptocurrencies remain open 24/7, but major coins like SOL-USD, BTC-USD, and ETH-USD are also currently in bearish trends (below SMA20) with negative or flat 1-hour changes, failing to meet our strict reversal confirmation trigger (rsi_1h >= 32 and positive 1-hour candle change). Our single open equity position, AAPL, is currently held through the weekend consolidation phase, sitting comfortably in an uptrend above its SMA20 with an unrealized gain of +0.16%."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL remains in a confirmed uptrend above SMA20 with a positive unrealized PnL. Equity holding patience applies over the weekend, and we await market reopening for further upside continuation toward our +3.0% to +5.0% take-profit target.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain the AAPL position patiently as it is in an established uptrend above the SMA20, respecting equity holding patience rules. Monitor AAPL closely for take-profit opportunities once the market re-opens, targeting +3.0% to +5.0% gains or a 1-hour RSI above 72 with profit >= +2.5%. Keep strict stop-loss protections ready at -1.8% to -2.0%. Continue to sideline all crypto assets as they lack confirmed bullish reversal triggers and are trending below SMA20."
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
