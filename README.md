# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-30 15:20:38`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.23 USD** | **$6.92 USD** | **$39.15 USD** | 🔴 **-2.13%** ($-0.85) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $343.29 | $6.92 | 📉 -1.12% | 7d 1h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Broader market conditions are currently weak, with major equity indices (SPY, QQQ, NVDA, MSFT) and commodities (GLD) trading below their SMA20 lines, indicating a bearish regime. Cryptocurrencies (BTC-USD, ETH-USD, SOL-USD) are also under pressure and below their SMA20 indicators, failing our strict trend-following filters. AAPL remains our sole active position, currently holding its structural uptrend above the SMA20 with a mild PnL of -1.12%, which is well within our acceptable drawdown limit before hitting the -1.8% to -2.0% stop-loss threshold."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is still in a confirmed uptrend above its SMA20. Although experiencing minor intraday weakness, equity holding patience dictates we do not exit a position prematurely for being flat or slightly negative, provided it remains well above our -1.8% stop-loss limit.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "We will continue to hold our AAPL position as long as it respects its structural uptrend above the SMA20 and stays above our strict -1.8% stop-loss level. Take-profit target remains set between +3.5% and +5.0%. No new buys will be executed until market candidates clear both the uptrend filter and positive 1-hour reversal triggers (rsi_1h >= 32 and change_1h_pct > 0.0)."
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
