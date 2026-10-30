# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-30 15:10:43`

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

> "The broader market remains largely under pressure, with major indices (SPY, QQQ, NVDA) trading in bearish territory below their SMA20 lines alongside heavy downside momentum. AAPL remains our sole equity holding, currently showing a modest loss of -1.12%, which is comfortably above our strict -1.8% to -2.0% stop-loss threshold. Although AAPL's 1-hour change is currently negative (-0.94%), it maintains its structural uptrend above the SMA20, adhering to our equity holding patience rule. All potential crypto and alternative equity candidates fail either the trend filter or lack the required positive 1-hour reversal confirmation."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL remains in a confirmed uptrend above its SMA20. Although experiencing a short-term dip, the current PnL of -1.12% is well above our stop-loss trigger of -1.8% to -2.0%. Complying with equity holding patience rules, we hold the position to let it play out towards our take-profit target of +3.5% to +5.0%.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "We will maintain our AAPL position as long as it holds its structural uptrend above the SMA20 and stays above our -1.8% to -2.0% stop-loss limit. We continue to target a take-profit between +3.5% and +5.0%. No new entries will be made until candidates satisfy both the strict uptrend filter and positive 1-hour reversal triggers."
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
