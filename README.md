# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-04 19:20:39`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.09 USD** | **$7.14 USD** | **$39.23 USD** | 🔴 **-1.92%** ($-0.77) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012839 | $545.20 | $555.80 | $7.14 | 📈 +1.94% | 7h 49m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Wall Street markets are currently closed (CERRADO), leaving active liquidity restricted to 24/7 crypto markets. MSFT remains our only open equity holding, trading in an uptrend above its SMA20 with solid gains (+1.94%), showing an extremely high 1-hour RSI (92.2) following recent post-election rallies. In crypto, both BTC-USD and ETH-USD are in confirmed uptrends above their SMA20s, but their 1-hour RSI levels are elevated (>76), failing to meet our ideal pullback criteria (RSI between 32 and 50 with a green 1-hour candle bounce). Therefore, we maintain our current position patiently."

**Cycle Actions:**
- **[HOLD] MSFT** (Confidence: 90%): MSFT is trading in a confirmed uptrend above its SMA20 with solid positive performance (+1.94%). Following equity holding patience guidelines, we do not rotate or sell flat/winning positions prematurely unless our target (+3.0% to +5.0%) or stop-loss (-2.0%) is reached. Wall Street markets are closed.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding MSFT with a current unrealized gain of +1.94%. We will let the winner run toward our +3.0% to +5.0% target while keeping a strict eye on the -2.0% stop-loss. Wall Street assets are closed. For crypto (BTC-USD, ETH-USD), we remain disciplined: wait for 1-hour RSI to cool down closer to neutral/oversold levels before entering on a confirmed green bounce, respecting our strict anti-correlation constraint of holding at most one crypto asset at a time."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **87** | 🎯 **43.7%** (38W / 34L / 15BE) | 🔴 **$-0.77 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-04 11:30` | 🟢 BUY | `MSFT` | $7.00 | $545.20 | MSFT is currently the only asset trading above its SMA20 in a confirmed uptrend with stron... |
| `2026-11-02 11:40` | 🔴 SELL (-0.13$) | `AAPL` | $6.87 | $340.69 | AAPL has slipped further into a bearish trend below its SMA20 with a 1-hour RSI of 24.8 an... |
| `2026-10-28 13:21` | 🔴 SELL (-0.02$) | `MSFT` | $6.48 | $528.16 | MSFT has shifted to a bearish trend below its SMA20 and current performance is near our st... |
| `2026-10-26 12:01` | 🟢 BUY | `MSFT` | $6.50 | $530.04 | MSFT is in a confirmed uptrend above its SMA20, and the 1-hour RSI (62.8) and 1-hour perce... |
| `2026-10-23 13:40` | 🟢 BUY | `AAPL` | $7.00 | $347.17 | AAPL is in a confirmed uptrend above its SMA20, satisfying our strict trend filter. The 1-... |

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
