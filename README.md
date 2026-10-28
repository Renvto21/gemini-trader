# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-28 17:20:41`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.23 USD** | **$6.93 USD** | **$39.16 USD** | 🔴 **-2.11%** ($-0.84) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $343.83 | $6.93 | 📉 -0.96% | 5d 3h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Most equities and Wall Street assets are currently in CERRADO (market closed) status, meaning their prices are frozen and no immediate execution is permitted per market hours rules. AAPL remains our sole active position, currently holding steady with a minor drawdown (-0.96%), well within our stop-loss thresholds (-1.8% to -2.0%). Cryptocurrencies are open (24/7), but all major options (BTC-USD, ETH-USD, SOL-USD) are in a BAJISTA (below SMA20) trend and currently showing negative 1-hour percentage changes, failing our strict trend and reversal confirmation filters. Therefore, no new trades are executed."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is currently in a confirmed uptrend (above SMA20) and is holding within acceptable drawdown parameters (-0.96%) far above our hard stop-loss threshold. Per equity holding patience rules, we do not exit positions prematurely due to flat or minor fluctuating prices while the market is closed.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain the AAPL position under equity holding patience, monitoring its price relative to the stop-loss level of -1.8% to -2.0% and the target profit range of +3.0% to +5.0%. Avoid all crypto assets due to ongoing bearish trends below SMA20. Wait for the equity market to reopen to look for high-quality pullbacks in confirmed uptrend assets like MSFT or SPY once reversal triggers (rsi_1h >= 32 and positive 1-hour change) are met."
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
