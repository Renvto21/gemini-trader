# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-04 17:40:41`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.09 USD** | **$7.16 USD** | **$39.26 USD** | 🔴 **-1.86%** ($-0.74) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012839 | $545.20 | $557.92 | $7.16 | 📈 +2.33% | 6h 9m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The post-election equity rally continues to support selected large-cap tech leaders trading in a confirmed uptrend above their SMA20. MSFT and AAPL show strong positive 24-hour momentum and remain above their SMA20, whereas indices like SPY and QQQ are consolidating below their short-term moving average. MSFT is currently holding a solid profit with an extremely high 1-hour RSI near 95, approaching our take-profit threshold. Meanwhile, crypto assets like ETH-USD are trading above their SMA20 but their 1-hour change is currently slightly negative or consolidating, though ETH-USD shows an uptrend. We adhere strictly to holding our winning equity position patiently and avoiding premature exits."

**Cycle Actions:**
- **[HOLD] MSFT** (Confidence: 90%): MSFT is in a confirmed uptrend above its SMA20 with a strong 24h gain of 7.09% and a current unrealized profit of +2.33%. Following the equity holding patience rule and asymmetric risk/reward guidelines, we let this winner run towards our +3.0% to +5.0% target window without premature selling.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding MSFT with a +2.33% gain. The 1-hour RSI is at 95.3, nearing our profit target window (+3.0% to +5.0%). We will let the winner run and lock in profits once target prices ($570.00+) are reached, or maintain patience according to equity holding rules. Stop-loss remains protected at -2.0% ($534.30). Cash reserves are healthy at $32.09. We will wait for a proper pullback confirmation before deploying additional cash."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **87** | 🎯 **43.7%** (38W / 34L / 15BE) | 🔴 **$-0.77 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-04 11:30` | 🟢 BUY | `MSFT` | $7.00 | $545.20 | MSFT is currently the only asset trading above its SMA20 in a confirmed uptrend with stron... |
| `2026-11-02 11:40` | 🔴 SELL (-0.13$) | `AAPL` | $6.87 | $340.69 | AAPL has slipped further into a bearish trend below its SMA20 with a 1-hour RSI of 24.8 an... |
| `2026-10-28 13:21` | 🔴 SELL (-0.02$) | `MSFT` | $6.48 | $528.16 | MSFT has shifted to a bearish trend below its SMA20 and current performance is near our st... |
| `2026-10-26 12:01` | 🟢 BUY | `MSFT` | $6.50 | $530.04 | MSFT is in a confirmed uptrend above its SMA20, and the 1-hour RSI (62.8) and 1-hour perce... |
| `2026-10-23 13:40` | 🟢 BUY | `AAPL` | $7.00 | $347.17 | AAPL is in a confirmed uptrend above its SMA20, satisfying our strict trend filter. The 1-... |

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
