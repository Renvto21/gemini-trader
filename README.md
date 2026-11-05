# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-05 07:00:59`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$31.78 USD** | **$6.98 USD** | **$38.76 USD** | 🔴 **-3.10%** ($-1.24) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.002886 | $2425.59 | $2417.66 | $6.98 | 📉 -0.33% | 5h 19m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Traditional equity markets are currently closed (CERRADO), leaving crypto as the only active venue (24/7). ETH-USD remains in a confirmed uptrend above its SMA20 and is currently consolidating with a slightly negative 1-hour change (-0.0%). Meanwhile, BTC-USD is also above its SMA20 with a neutral 1-hour candle. Since we already hold ETH-USD and our anti-correlation constraint limits us to one crypto position, and traditional markets are closed, we maintain our current ETH-USD position and wait for a clear 1-hour green candle confirmation before considering any further additions or adjustments."

**Cycle Actions:**
- **[HOLD] ETH-USD** (Confidence: 85%): ETH-USD is in a confirmed uptrend above its SMA20 and is holding steady with a minor pullback. Traditional markets are closed, and our anti-correlation constraint allows only one crypto position. We hold to let the trend play out toward our +3.5% target while respecting the -2.0% stop-loss.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding ETH-USD position currently down -0.33%. Will monitor ETH-USD for a clear 1-hour positive momentum confirmation (change_1h_pct > 0.0) with RSI >= 32 before adding to the position if capital allows. Target profit is +3.5% to +5.0%, with a strict stop-loss at -2.0%. Keep cash reserve above $4.00."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **88** | 🎯 **43.2%** (38W / 35L / 15BE) | 🔴 **$-1.08 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-05 01:41` | 🟢 BUY | `ETH-USD` | $7.00 | $2425.59 | ETH-USD is in a confirmed uptrend above its SMA20, market status is open 24/7, 1-hour RSI ... |
| `2026-11-04 22:00` | 🔴 SELL (-0.31$) | `MSFT` | $6.69 | $520.99 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -4.44% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-04 11:30` | 🟢 BUY | `MSFT` | $7.00 | $545.20 | MSFT is currently the only asset trading above its SMA20 in a confirmed uptrend with stron... |
| `2026-11-02 11:40` | 🔴 SELL (-0.13$) | `AAPL` | $6.87 | $340.69 | AAPL has slipped further into a bearish trend below its SMA20 with a 1-hour RSI of 24.8 an... |
| `2026-10-28 13:21` | 🔴 SELL (-0.02$) | `MSFT` | $6.48 | $528.16 | MSFT has shifted to a bearish trend below its SMA20 and current performance is near our st... |

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
