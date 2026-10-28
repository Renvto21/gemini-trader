# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-28 16:10:49`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.23 USD** | **$6.95 USD** | **$39.17 USD** | 🔴 **-2.07%** ($-0.83) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $344.52 | $6.95 | 📉 -0.76% | 5d 2h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market is experiencing a cautious phase, with most major assets currently trading below their SMA20 trend filters, signaling a broader bearish or consolidating state. AAPL remains our sole active equity position, continuing to trade above its SMA20 in an uptrend despite minor intraday pullbacks (-0.04% 1h change), well within the equity holding patience guidelines as it has not breached our hard stop-loss of -1.8% to -2.0%. Other prominent tickers and cryptocurrencies are either in downtrends below the SMA20 or failing to exhibit the necessary bullish 1-hour confirmation triggers (change_1h_pct > 0.0), keeping us strictly sidelined from opening new risk exposures in accordance with our strict trend-following and anti-correlation constraints."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): AAPL is maintaining its uptrend above its SMA20. In accordance with equity holding patience guidelines, we hold the position as it remains far above the hard stop-loss threshold (-1.8% to -2.0%) and awaits its target profit margin without succumbing to short-term noise.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain the current AAPL position under equity holding patience, monitoring the price relative to our stop-loss at -1.8% to -2.0% and profit targets at +3.0% to +5.0%. Cash reserves remain robust at $32.23. Wait for assets to reclaim positions above their SMA20 with validated 1-hour bullish confirmation (rsi_1h >= 32 and change_1h_pct > 0.0) before executing any new BUY orders."
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
