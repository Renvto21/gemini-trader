# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-05 19:50:36`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.14 USD** | **$6.48 USD** | **$38.61 USD** | 🔴 **-3.46%** ($-1.39) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $344.17 | $6.48 | 📉 -0.34% | 2h 9m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader equity and crypto markets remain under pressure with major indices and digital assets trading below their respective 20-period simple moving averages (SMA20), reflecting a general bearish sentiment. Wall Street equity markets are currently closed (CERRADO), freezing stock prices. Among equities, MSFT, GLD, and AAPL maintain uptrend statuses above the SMA20, but strict market hour rules prohibit trading closed assets. In the cryptocurrency sector (open 24/7), extreme downside volatility persists with all tracked cryptos (BTC-USD, ETH-USD, SOL-USD) sitting below their SMA20 with weak 1-hour momentum, failing our strict trend and reversal confirmation criteria. Consequently, no new positions can be entered, and our existing equity position in AAPL must be held in accordance with equity holding patience rules."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): AAPL remains in a confirmed uptrend above its SMA20. Per equity holding patience rules, we do not rotate or sell flat/minor drawdown positions prematurely. Market is closed, so we hold and monitor against the -2.0% stop-loss threshold.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL position which is currently showing a minor unrealized loss (-0.34%), comfortably above the stop-loss threshold (-2.0%). Wall Street is closed, so no adjustments can be made. Crypto assets are in severe downtrends with negative momentum and low RSI levels, completely failing our trend filter (never catch falling knives). Will continue monitoring MSFT and GLD for potential pullbacks once markets reopen, and wait for confirmed green 1-hour candles before considering new entries."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **89** | 🎯 **42.7%** (38W / 36L / 15BE) | 🔴 **$-1.23 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-05 17:40` | 🟢 BUY | `AAPL` | $6.50 | $345.35 | AAPL is in a confirmed uptrend above its SMA20, market status is open, and 1-hour momentum... |
| `2026-11-05 11:20` | 🔴 SELL (-0.15$) | `ETH-USD` | $6.85 | $2374.60 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -2.10% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-05 01:41` | 🟢 BUY | `ETH-USD` | $7.00 | $2425.59 | ETH-USD is in a confirmed uptrend above its SMA20, market status is open 24/7, 1-hour RSI ... |
| `2026-11-04 22:00` | 🔴 SELL (-0.31$) | `MSFT` | $6.69 | $520.99 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -4.44% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-04 11:30` | 🟢 BUY | `MSFT` | $7.00 | $545.20 | MSFT is currently the only asset trading above its SMA20 in a confirmed uptrend with stron... |

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
