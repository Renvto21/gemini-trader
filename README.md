# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-25 17:20:43`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.25 USD** | **$7.01 USD** | **$39.26 USD** | 🔴 **-1.85%** ($-0.74) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $347.73 | $7.01 | 📈 +0.16% | 2d 3h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The majority of equity and crypto assets are currently exhibiting bearish trends below their respective SMA20 lines, accompanied by weak daily RSI levels. Wall Street equity markets are currently closed (CERRADO), meaning no actions can or should be taken on stocks like AAPL, which remains our single open position. AAPL is holding steady with a holding time of over 2 days, showing a minor gain of +0.16%, well within our acceptable holding range. Crypto assets are open 24/7, but all major cryptos (ETH-USD, SOL-USD, BTC-USD) remain below their SMA20 trend filters, preventing any new buy signals according to our strict trend-following pullback rules."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): AAPL remains in a confirmed uptrend above the SMA20 with a positive PnL. Equity markets are currently closed, and per our patience rule for equity holdings, we continue holding until take-profit targets (+3.0% to +5.0% or rsi_1h > 72) or stop-loss limits (-1.8%) are reached.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Continue holding AAPL as it stays above the SMA20 trend filter. Monitor AAPL closely when markets reopen for take-profit opportunities if the 1-hour RSI approaches or surpasses 72 or if gains reach the +3.0% to +5.0% target band. Keep the strict stop-loss at -1.8%. Maintain all crypto assets sidelined due to bearish trends and lack of confirmed bullish reversal structures above the SMA20."
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
