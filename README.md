# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-27 09:50:51`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.75 USD** | **$13.47 USD** | **$39.21 USD** | 🔴 **-1.96%** ($-0.79) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $343.91 | $6.93 | 📉 -0.94% | 3d 20h |
| `MSFT` | 0.012263 | $530.04 | $532.60 | $6.53 | 📈 +0.48% | 21h 49m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Wall Street equities (AAPL, MSFT, SPY, QQQ, NVDA, GLD) are currently closed, with prices frozen. Among equities, MSFT remains in an uptrend above its SMA20 with a strong 1-hour RSI of 80.0 and positive PnL (+0.48%), while AAPL is also in an uptrend above its SMA20 with a slight pullback (PnL -0.94%). Crypto markets are open 24/7, but all major cryptos (ETH-USD, SOL-USD, BTC-USD) are currently trading below their SMA20 (bearish trend), meaning our strict trend filter prevents any crypto entries. Following equity holding rules, we maintain patience with AAPL and MSFT during market closure, awaiting optimal take-profit targets (+3.0% to +5.0%) or stop-loss limits (-1.8% to -2.0%)."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is an equity holding currently under market closure. It remains in a confirmed uptrend above its SMA20, and equity holding rules require patience and avoiding premature rotation unless stop-loss limits are breached.
- **[HOLD] MSFT** (Confidence: 90%): MSFT is in a confirmed uptrend above its SMA20 and is currently profitable (+0.48%). With markets closed, we hold to approach our target profit range of +3.0% to +5.0%.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain positions in AAPL and MSFT during market closure. Monitor MSFT for profit-taking when markets reopen, aiming for +3.0% to +5.0% gains. Keep AAPL open as equity patience rules dictate giving stocks time to play out despite minor fluctuations, keeping strict stop-losses at -1.8% to -2.0%. Keep crypto exposure at zero due to persistent bearish trends below SMA20 across all digital assets."
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
