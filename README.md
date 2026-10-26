# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-26 03:20:42`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.25 USD** | **$7.01 USD** | **$39.26 USD** | 🔴 **-1.85%** ($-0.74) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $347.73 | $7.01 | 📈 +0.16% | 2d 13h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Wall Street markets remain closed (CERRADO) with prices frozen, meaning active liquidity and trade management must strictly defer equity actions until market hours resume. AAPL is currently being held in a confirmed uptrend above its SMA20 with a modest PnL of +0.16% and a 1h RSI of 66.0, approaching our take-profit target zone of +3.0% to +5.0%. Crypto assets (SOL-USD, BTC-USD, ETH-USD) are open 24/7 but are currently in a BAJISTA (below SMA20) trend state with negative 24h changes. Given our strict trend-following pullback rules and anti-correlation constraints, no crypto buys are justified right now since prices are not in a confirmed uptrend bounce with positive momentum candles meeting all reversal criteria."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): AAPL is in an active equity position adhering to the equity holding patience rule. Wall Street is closed, and the stock is showing steady performance in an uptrend above SMA20 with an unrealized profit of +0.16%. No action required until take-profit or stop-loss parameters are reached.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Continue holding AAPL through the weekend as Wall Street is closed, giving the stock time to develop toward our +3.0% to +5.0% take-profit target while maintaining our strict -1.8% stop-loss level. Avoid opening any crypto positions since all major coins are trading below their SMA20 trends. Monitor crypto and equity markets for upcoming trend reversals and look for proper confirmation triggers before deploying additional capital."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **85** | 🎯 **44.7%** (38W / 32L / 15BE) | 🔴 **$-0.62 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-23 13:40` | 🟢 BUY | `AAPL` | $7.00 | $347.17 | AAPL is in a confirmed uptrend above its SMA20, satisfying our strict trend filter. The 1-... |
| `2026-10-22 16:00` | 🔴 SELL (-0.12$) | `MSFT` | $6.88 | $521.40 | MSFT has dropped to a PnL of -1.71%, closely approaching our mandatory stop-loss threshold... |
| `2026-10-22 14:40` | 🔴 SELL (+0.17$) | `AAPL` | $10.17 | $346.52 | AAPL rsi_1h has surpassed 72 (currently 73.4) with a positive return of +1.73%, satisfying... |
| `2026-10-21 12:01` | 🟢 BUY | `MSFT` | $7.00 | $530.45 | MSFT is in a confirmed uptrend above its SMA20. The 1-hour RSI is at 36.7 (above the 32 th... |
| `2026-10-21 10:10` | 🔴 SELL (+0.12$) | `ETH-USD` | $10.07 | $2481.87 | ETH-USD rsi_1h has surpassed 72 (currently 73.7) with a positive return of +1.21%, satisfy... |

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
