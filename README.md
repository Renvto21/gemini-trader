# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-10 20:00:46`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.01 USD** | **$13.54 USD** | **$38.55 USD** | 🔴 **-3.63%** ($-1.45) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $348.51 | $6.56 | 📈 +0.92% | 5d 2h |
| `MSFT` | 0.013089 | $534.82 | $533.16 | $6.98 | 📉 -0.31% | 4d 6h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The traditional stock market is currently closed ('CERRADO'), with prices frozen across all equity assets and ETFs (AAPL, MSFT, NVDA, SPY, QQQ). Cryptocurrencies remain open (24/7) but are locked in a heavy downtrend following recent hot inflation data and broad macroeconomic weakness, with ETH, SOL, and BTC trading below their respective SMA20 lines and negative 24-hour momentum. Our equity positions in AAPL and MSFT remain stable; AAPL is showing positive returns (+0.92%) while MSFT is slightly negative (-0.31%), both well within acceptable tolerance thresholds and safely above the strict -1.8% to -2.0% stop-loss limits. No stocks or crypto assets currently fulfill both the structural uptrend filter (above SMA20) and the mandatory reversal confirmation trigger (positive 1-hour candle and RSI >= 32)."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): AAPL is in a confirmed uptrend above its SMA20 and is currently profitable (+0.92%). Market is closed (CERRADO) and equity holding patience dictates letting the position run toward the +3% to +5% profit target without premature rotation.
- **[HOLD] MSFT** (Confidence: 100%): MSFT is in a confirmed uptrend above its SMA20 with minor drawdown (-0.31%), well above the -1.8% stop-loss threshold. Market is closed (CERRADO) and equity holding patience applies.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing holdings in AAPL and MSFT as per the equity holding patience rule since markets are closed and positions are not hitting stop-loss thresholds. Keep crypto exposure at zero due to persistent bearish trends below SMA20 and lack of confirmed upward reversal triggers. Monitor equity markets upon reopening for potential profit-taking targets (+3% to +5%) or stop-loss limits (-1.8% to -2.0%)."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **90** | 🎯 **42.2%** (38W / 37L / 15BE) | 🔴 **$-1.35 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-10 11:31` | 🔴 SELL (-0.12$) | `GLD` | $6.87 | $371.60 | GLD has fallen below its SMA20 trend line and its current PnL is approaching the strict st... |
| `2026-11-09 11:30` | 🟢 BUY | `GLD` | $7.00 | $378.35 | GLD is in a confirmed uptrend above its SMA20, market status is open, 1-hour momentum is s... |
| `2026-11-06 13:10` | 🟢 BUY | `MSFT` | $7.00 | $534.82 | MSFT is in a confirmed uptrend above its SMA20, market status is open, 1-hour RSI has reco... |
| `2026-11-05 17:40` | 🟢 BUY | `AAPL` | $6.50 | $345.35 | AAPL is in a confirmed uptrend above its SMA20, market status is open, and 1-hour momentum... |
| `2026-11-05 11:20` | 🔴 SELL (-0.15$) | `ETH-USD` | $6.85 | $2374.60 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -2.10% hit safety limit (-2.0%). Liquidated by code... |

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
