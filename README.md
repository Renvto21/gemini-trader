# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-05 12:41:14`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$38.64 USD** | **$0.00 USD** | **$38.64 USD** | 🔴 **-3.41%** ($-1.36) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| *(No open positions - 100% in cash)* | - | - | - | - | - | - |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market remains under pressure with major indices and equities such as NVDA, QQQ, SPY, and crypto assets (ETH-USD, BTC-USD, SOL-USD) sitting below their SMA20 in clear downtrends. Assets in confirmed uptrends above their SMA20 include MSFT, AAPL, and GLD. However, short-term pullbacks lack the required reversal confirmation triggers (rsi_1h >= 32 and change_1h_pct > 0). Specifically, MSFT's 1-hour change is negative (-0.1%), and AAPL's 1-hour change is negative (-0.27%) alongside an overbought 1h RSI. GLD has an extremely high 1h RSI of 90.6, failing the healthy pullback entry criteria. Maintaining capital preservation discipline and holding cash until clear setups emerge."

**Cycle Actions:**
- **[HOLD] MSFT** (Confidence: 0%): Asset is in an uptrend above SMA20, but current 1-hour momentum shows a slight negative change (-0.1%) and does not yet meet the strict reversal confirmation trigger (change_1h_pct > 0.0). Holding cash until a valid pullback setup occurs.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Preserving capital with $38.64 USD in cash. MSFT and AAPL remain in solid uptrends above the SMA20, but current short-term momentum lacks the proper pullback setup (RSI_1h >= 32 and change_1h_pct > 0). Will continue to patiently monitor MSFT and AAPL for a healthy dip to key support levels accompanied by a confirmed green 1-hour candle before executing any new long entries."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **89** | 🎯 **42.7%** (38W / 36L / 15BE) | 🔴 **$-1.23 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-05 11:20` | 🔴 SELL (-0.15$) | `ETH-USD` | $6.85 | $2374.60 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -2.10% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-05 01:41` | 🟢 BUY | `ETH-USD` | $7.00 | $2425.59 | ETH-USD is in a confirmed uptrend above its SMA20, market status is open 24/7, 1-hour RSI ... |
| `2026-11-04 22:00` | 🔴 SELL (-0.31$) | `MSFT` | $6.69 | $520.99 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -4.44% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-04 11:30` | 🟢 BUY | `MSFT` | $7.00 | $545.20 | MSFT is currently the only asset trading above its SMA20 in a confirmed uptrend with stron... |
| `2026-11-02 11:40` | 🔴 SELL (-0.13$) | `AAPL` | $6.87 | $340.69 | AAPL has slipped further into a bearish trend below its SMA20 with a 1-hour RSI of 24.8 an... |

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
