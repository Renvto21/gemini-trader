# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-29 10:10:54`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.23 USD** | **$6.93 USD** | **$39.16 USD** | 🔴 **-2.11%** ($-0.84) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $343.83 | $6.93 | 📉 -0.96% | 5d 20h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Wall Street markets remain closed (CERRADO), meaning traditional equities and ETFs such as AAPL and MSFT are currently frozen. Cryptocurrencies are trading actively (ABIERTO 24/7), but all major crypto assets (BTC-USD, ETH-USD, SOL-USD) remain in a clear bearish trend below their SMA20 with weak 24-hour performance, keeping them excluded per our strict trend filter. Our single open equity position in AAPL is experiencing minor unrealized losses (-0.96%), well within our stop-loss tolerance of -1.8% to -2.0%. Following equity holding patience rules, we will maintain AAPL through the weekend closure, awaiting Wall Street's reopening for potential directional confirmation."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL remains in a confirmed uptrend above its SMA20. Although currently experiencing a minor pullback (-0.96%), it is well above our hard stop-loss threshold (-1.8% to -2.0%). Adhering to our equity holding patience rule and market hours constraint, we will hold the position steady through the weekend.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Continue holding AAPL through the market closure. Monitor its stop-loss threshold at approximately $340.91 (-1.8% to -2.0% risk limit) and target a profit objective around $357.00 to $360.00 (+3% to +5%). Keep all crypto assets excluded due to persistent bearish macro trends under the SMA20. Once Wall Street reopens, evaluate uptrend equities for potential new entries or exits depending on price action."
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
