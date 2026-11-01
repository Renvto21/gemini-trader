# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-01 10:50:41`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.23 USD** | **$6.95 USD** | **$39.17 USD** | 🔴 **-2.06%** ($-0.83) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $344.63 | $6.95 | 📉 -0.73% | 8d 21h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market remains largely closed with key equities and indices (SPY, QQQ, AAPL, MSFT, NVDA, GLD) showing 'CERRADO' status and currently in a general macro pullback or bearish trend below their SMA20, with the notable exception of AAPL which maintains its structural UPTREND above the SMA20. Among active 24/7 crypto markets, ETH-USD, SOL-USD, and BTC-USD remain under bearish daily trends below their SMA20, preventing any new crypto asset entries due to our strict anti-falling-knife trend filter. AAPL continues to be held patiently in accordance with equity holding rules, currently sitting at a minor -0.73% PnL well above our hard stop-loss."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): AAPL remains in a confirmed uptrend above its SMA20. Following our equity holding patience rule, we continue to hold the position as it fluctuates near our entry price (-0.73% PnL), well above our stop-loss threshold.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Continue holding AAPL under equity holding patience rules. AAPL is currently at $344.63 (-0.73% PnL), well above our stop-loss floor (~$340.00). Maintain profit target near $360.00. Cash reserves remain robust at $32.23. Refrain from opening new crypto or equity positions due to closed market hours for stocks and bearish trends below SMA20 for available cryptos. Monitor for market re-openings and incoming trend alignment signals."
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
