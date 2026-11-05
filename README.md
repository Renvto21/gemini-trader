# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-05 10:40:42`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$31.78 USD** | **$6.89 USD** | **$38.67 USD** | 🔴 **-3.31%** ($-1.33) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.002886 | $2425.59 | $2387.73 | $6.89 | 📉 -1.56% | 8h 59m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The traditional stock and ETF markets are currently closed (CERRADO), meaning active trading must focus on 24/7 open cryptocurrencies. Among crypto assets, ETH-USD is in a confirmed uptrend (above SMA20). However, ETH's 1-hour RSI is 30.7 and its 1-hour change is -0.15%, failing to meet our Reversal Confirmation Trigger (rsi_1h >= 32 and change_1h_pct > 0.0). BTC-USD and SOL-USD are currently in downtrends. We hold our current ETH-USD position as it has not triggered a stop-loss, while observing strict patience and capital preservation rules."

**Cycle Actions:**
- **[HOLD] ETH-USD** (Confidence: 80%): ETH-USD is in an uptrend but currently experiencing a minor pullback with a negative 1-hour change (-0.15%) and RSI below 32 (30.7). It has not hit our stop-loss (-1.8% to -2.0%), so we hold patiently following our equity holding patience and risk management rules.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Currently holding ETH-USD with a stop-loss at -2.0% ($2377.00) and a target take-profit at +3.5% ($2510.00). Wall Street assets are closed. Will wait for ETH-USD to show a green 1-hour candle and RSI >= 32 before considering any additional accumulation, maintaining the anti-correlation constraint of holding only one crypto asset."
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
