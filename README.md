# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-22 11:03:19`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.20 USD** | **$17.06 USD** | **$39.25 USD** | 🔴 **-1.86%** ($-0.75) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $344.77 | $10.12 | 📈 +1.21% | 1d 23h |
| `MSFT` | 0.013196 | $530.45 | $525.75 | $6.94 | 📉 -0.89% | 23h 2m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Broad market weakness persists across both traditional equities and cryptocurrencies, with SPY, QQQ, NVDA, BTC-USD, and ETH-USD trading in confirmed downtrends below their respective 20-period SMAs. AAPL remains the sole asset demonstrating relative strength in a confirmed uptrend (above SMA20) with positive hourly momentum (+0.20% 1h, RSI 59.5). MSFT has pulled back below its SMA20 to -0.89% PnL, but remains comfortably within our -1.80% to -2.00% risk tolerance threshold, warranting equity holding patience."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is maintaining an uptrend above its SMA20 with positive 1h momentum. PnL is currently +1.21%, which has not yet reached our asymmetric profit target of +3.0% to +5.0% or an overbought RSI 1h > 72. Letting the winner run.
- **[HOLD] MSFT** (Confidence: 80%): MSFT shows an unrealized loss of -0.89%, well above our mandatory stop-loss cutoff (-1.8% to -2.0%). In accordance with Equity Holding Patience (Rule 6), we do not exit tech equities prematurely on intraday chop.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL towards the target profit window of +3.0% to +5.0% ($350.85 - $357.65) or exit if 1h RSI exceeds 72 with sufficient gains. Holding MSFT with a strict stop-loss alert set at $519.84 (-2.0%). Cash reserve remains strong at $22.20 USD (56.5% of equity). Strict trend-filter rules prohibit buying dipping assets (BTC, ETH, SOL, QQQ, NVDA) until they reclaim SMA20 and print confirmed 1h reversal candles."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **83** | 🎯 **44.6%** (37W / 31L / 15BE) | 🔴 **$-0.67 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-21 12:01` | 🟢 BUY | `MSFT` | $7.00 | $530.45 | MSFT is in a confirmed uptrend above its SMA20. The 1-hour RSI is at 36.7 (above the 32 th... |
| `2026-10-21 10:10` | 🔴 SELL (+0.12$) | `ETH-USD` | $10.07 | $2481.87 | ETH-USD rsi_1h has surpassed 72 (currently 73.7) with a positive return of +1.21%, satisfy... |
| `2026-10-20 13:51` | 🟢 BUY | `ETH-USD` | $9.95 | $2452.17 | ETH-USD muestra un excelente impulso de corto plazo con change_1h_pct positivo (+0.55%) y ... |
| `2026-10-20 13:51` | 🔴 SELL (-0.05$) | `GLD` | $9.95 | $377.90 | GLD se encuentra estancado con un rendimiento ligeramente negativo (-0.47%) y un rsi_1h de... |
| `2026-10-20 12:01` | 🟢 BUY | `GLD` | $10.00 | $379.70 | GLD presenta un RSI de 1 hora en 31.4, acercándose a la zona ideal de sobreventa para acti... |

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
