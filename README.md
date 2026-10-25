# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-25 04:40:37`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.25 USD** | **$7.01 USD** | **$39.26 USD** | 🔴 **-1.85%** ($-0.74) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $347.73 | $7.01 | 📈 +0.16% | 1d 14h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market condition remains cautious, with all traditional Wall Street equities (AAPL, MSFT, NVDA, QQQ, SPY, GLD) currently showing a 'CERRADO' market status, meaning prices are frozen and no trades can be executed on equities at this time. AAPL remains our sole open position, demonstrating modest resilience and holding steady in an uptrend above its SMA20 with a current PnL of +0.16%. In the crypto sector (ABIERTO 24/7), assets like BTC-USD, ETH-USD, and SOL-USD show positive 1-hour changes and rebounding 1H RSI levels, but all remain structurally in a BAJISTA (bajo SMA20) downtrend. Per our strict quantitative rules, we refuse to catch falling knives or buy crypto assets trading below their SMA20."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): AAPL is currently in a closed market state, preserving our position. It remains in an uptrend above the SMA20 with a solid PnL of +0.16%. Adhering to our equity holding patience rule, we maintain the position while awaiting our take-profit threshold (+3.0% to +5.0%) or 1H RSI > 72 with a gain >= +2.5%.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL position (entry $347.17, current $347.73, PnL +0.16%). Practicing equity holding patience, allowing AAPL time to reach our take-profit target zone of +3.0% to +5.0% ($357.58 to $364.53) or exit if 1H RSI exceeds 72 with a gain >= +2.5%. Hard stop-loss remains strictly enforced at -1.8% to -2.0% ($340.22 to $340.92). Crypto markets remain locked in a downtrend below the SMA20, so we maintain our cash reserves and sideline stance on BTC, ETH, and SOL until a confirmed trend reversal occurs."
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
