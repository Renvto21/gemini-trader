# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-06 10:40:38`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.14 USD** | **$6.48 USD** | **$38.61 USD** | 🔴 **-3.46%** ($-1.39) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $344.17 | $6.48 | 📉 -0.34% | 16h 59m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Major equity indices and stocks remain closed for the weekend/market pause, with most key benchmarks such as SPY, QQQ, and NVDA trading in confirmed downtrends below their SMA20 following the recent macro tech sell-off. AAPL is holding its ground above its SMA20 in an uptrend, currently exhibiting a minor flat consolidation. Cryptocurrencies are trading 24/7, but major assets like SOL-USD, ETH-USD, and BTC-USD remain below their respective SMA20 trend lines, failing to meet our strict trend-following criteria. Consequently, we maintain patience with our single open equity position (AAPL) and refrain from initiating new crypto entries due to lack of confirmed bullish trend conditions."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is currently in a confirmed uptrend above its SMA20. Following equity holding patience rules, we do not rotate or sell an equity position just because it has been flat for a short duration. We continue holding toward our +3.0% to +5.0% take-profit target while maintaining our strict stop-loss.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL position patiently as it remains above the SMA20 during market closure. Will monitor AAPL upon market reopening for take-profit targets (+3.0% to +5.0%) or maintain strict adherence to the -2.0% stop-loss threshold. Cryptocurrencies (SOL, ETH, BTC) remain excluded due to ongoing downtrends below the SMA20. Cash reserves remain robust at $32.14 USD."
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
