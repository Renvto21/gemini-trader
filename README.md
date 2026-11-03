# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-03 02:40:39`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$39.09 USD** | **$0.00 USD** | **$39.09 USD** | 🔴 **-2.26%** ($-0.91) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| *(No open positions - 100% in cash)* | - | - | - | - | - | - |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market remains in a defensive posture with all major tracked equities (MSFT, AAPL, NVDA, SPY, QQQ) and cryptos (SOL-USD, ETH-USD, BTC-USD) currently trading below their respective SMA20 thresholds, indicating a persistent bearish trend. Wall Street markets are closed, freezing prices for equities, while crypto markets trade 24/7. However, crypto assets are also failing to show a valid reversal setup, as 1-hour percentage changes are negative or flat (BTC-USD change_1h_pct is -0.36%, ETH-USD is -0.30%, SOL-USD is -0.42%). In accordance with our strict trend-following rules, catching falling knives or buying assets below the SMA20 without a confirmed positive hourly price bounce is strictly prohibited. Therefore, capital preservation remains paramount, and we will maintain a 100% cash position."

**Cycle Actions:**
- **[HOLD] BTC-USD** (Confidence: 0%): No trade action required. Although BTC-USD has an RSI_1h of 32.6, its 1-hour change is negative (-0.36%) and it remains in a bearish trend below the SMA20. We strictly avoid buying falling knives until a verified green hourly candle occurs.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintained 100% cash position ($39.09). All available assets are currently trading in a bearish trend below the SMA20. Cryptos like BTC-USD and ETH-USD show RSI values near or above 32, but their 1-hour candles are negative (-0.36% and -0.30%), lacking the required positive momentum trigger (change_1h_pct > 0.0). Will continue to wait patiently for a confirmed hourly reversal candle and a reclaim of the SMA20 before deploying capital."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **87** | 🎯 **43.7%** (38W / 34L / 15BE) | 🔴 **$-0.77 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-02 11:40` | 🔴 SELL (-0.13$) | `AAPL` | $6.87 | $340.69 | AAPL has slipped further into a bearish trend below its SMA20 with a 1-hour RSI of 24.8 an... |
| `2026-10-28 13:21` | 🔴 SELL (-0.02$) | `MSFT` | $6.48 | $528.16 | MSFT has shifted to a bearish trend below its SMA20 and current performance is near our st... |
| `2026-10-26 12:01` | 🟢 BUY | `MSFT` | $6.50 | $530.04 | MSFT is in a confirmed uptrend above its SMA20, and the 1-hour RSI (62.8) and 1-hour perce... |
| `2026-10-23 13:40` | 🟢 BUY | `AAPL` | $7.00 | $347.17 | AAPL is in a confirmed uptrend above its SMA20, satisfying our strict trend filter. The 1-... |
| `2026-10-22 16:00` | 🔴 SELL (-0.12$) | `MSFT` | $6.88 | $521.40 | MSFT has dropped to a PnL of -1.71%, closely approaching our mandatory stop-loss threshold... |

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
