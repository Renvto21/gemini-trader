# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-04 12:51:07`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.09 USD** | **$7.09 USD** | **$39.19 USD** | 🔴 **-2.04%** ($-0.81) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012839 | $545.20 | $552.31 | $7.09 | 📈 +1.30% | 1h 20m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader equity market is showing post-election volatility following the Democratic sweep in Congress, with Nasdaq and select tech bellwethers reaching new highs. MSFT is currently holding steady above its SMA20 with solid daily gains, though its 1-hour RSI is elevated at 72.4. Cryptocurrencies are experiencing strong upward momentum, with BTC-USD and ETH-USD trading firmly above their SMA20 lines, though their 1-hour RSI levels are also extended (above 75), requiring caution against chasing immediate breakouts without proper pullbacks."

**Cycle Actions:**
- **[HOLD] MSFT** (Confidence: 85%): MSFT remains in a confirmed uptrend above its SMA20 with positive PnL (+1.3%). Following equity holding patience rules, we do not rotate or sell prematurely and allow the trend to run towards our target.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain MSFT position in line with equity holding patience rules, keeping stop-loss strict around -1.8% to -2.0% and aiming for a take-profit target of +3.5% to +5.0%. For crypto assets (BTC-USD, ETH-USD), monitor for a healthy pullback to cool down 1-hour RSI levels before considering entries under the anti-correlation rule (maximum 1 crypto position)."
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
