# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-30 06:30:44`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.23 USD** | **$7.04 USD** | **$39.26 USD** | 🔴 **-1.85%** ($-0.74) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $348.91 | $7.04 | 📈 +0.50% | 6d 16h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market remains mostly under pressure with equities and key crypto assets trading below their respective SMA20 trends. AAPL is the single notable exception, maintaining a confirmed bullish trend above its SMA20 with strong daily momentum, currently showing a modest unrealized gain of +0.5%. All other monitored assets, including major cryptocurrencies (BTC, ETH, SOL), are currently in bearish trends below the SMA20 or lack the required 1-hour positive momentum triggers. Given that Wall Street equities are currently closed, trading activity is strictly restricted to open crypto assets where conditions do not yet meet our strict pullback entry requirements."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in a confirmed uptrend above its SMA20 and is currently up +0.5%. Per equity holding patience rules, we do not sell or rotate positions simply for being flat or slow-moving unless take-profit targets (+3.0% to +5.0%) or stop-loss triggers are reached.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Continue holding AAPL patiently as it remains above its SMA20 trend filter. Monitor AAPL for take-profit targets between $357 and $364 (+3.0% to +5.0%) or stop-loss triggers near -1.8%. Crypto markets currently show negative 1-hour percentage changes and/or RSI readings below threshold, so cash reserve is preserved well above the $4.00 minimum. Await confirmed green 1-hour candles and RSI >= 32 on uptrend assets before deploying capital into new positions."
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
