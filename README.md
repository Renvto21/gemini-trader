# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-26 16:20:42`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.75 USD** | **$13.45 USD** | **$39.20 USD** | 🔴 **-1.99%** ($-0.80) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $343.86 | $6.93 | 📉 -0.95% | 3d 2h |
| `MSFT` | 0.012263 | $530.04 | $531.81 | $6.52 | 📈 +0.33% | 4h 19m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The market shows mixed conditions with major equity indices like SPY, QQQ, and NVDA trading below their SMA20 despite positive 24-hour momentum, precluding new long entries per our strict trend filter. Crypto assets remain in downtrends. Among our current holdings, MSFT is up +0.33% with a 1-hour RSI at 80.9, nearing our +3.0% to +5.0% take-profit zone. AAPL is experiencing a mild pullback (-0.95%) while holding above its SMA20 in a confirmed uptrend."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 80%): AAPL is in a confirmed uptrend above its SMA20. Although down -0.95%, equity holding patience dictates we maintain positions through minor fluctuations unless stop-loss limits (-1.8% to -2.0%) are breached.
- **[HOLD] MSFT** (Confidence: 85%): MSFT is in a confirmed uptrend above its SMA20 and is currently in positive territory (+0.33%). With a 1-hour RSI above 80, we hold to capture further upside toward our +3.0% to +5.0% take-profit target.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain holding on AAPL and MSFT according to equity holding patience. Monitor MSFT closely for profit-taking if it reaches the +3.0% to +5.0% target window, and keep AAPL until it recovers or hits the -1.8% to -2.0% stop-loss threshold. Cash reserves remain secure at $25.75."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **85** | 🎯 **44.7%** (38W / 32L / 15BE) | 🔴 **$-0.62 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-26 12:01` | 🟢 BUY | `MSFT` | $6.50 | $530.04 | MSFT is in a confirmed uptrend above its SMA20, and the 1-hour RSI (62.8) and 1-hour perce... |
| `2026-10-23 13:40` | 🟢 BUY | `AAPL` | $7.00 | $347.17 | AAPL is in a confirmed uptrend above its SMA20, satisfying our strict trend filter. The 1-... |
| `2026-10-22 16:00` | 🔴 SELL (-0.12$) | `MSFT` | $6.88 | $521.40 | MSFT has dropped to a PnL of -1.71%, closely approaching our mandatory stop-loss threshold... |
| `2026-10-22 14:40` | 🔴 SELL (+0.17$) | `AAPL` | $10.17 | $346.52 | AAPL rsi_1h has surpassed 72 (currently 73.4) with a positive return of +1.73%, satisfying... |
| `2026-10-21 12:01` | 🟢 BUY | `MSFT` | $7.00 | $530.45 | MSFT is in a confirmed uptrend above its SMA20. The 1-hour RSI is at 36.7 (above the 32 th... |

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
