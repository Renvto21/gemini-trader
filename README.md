# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-28 11:21:15`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.75 USD** | **$13.45 USD** | **$39.20 USD** | 🔴 **-2.01%** ($-0.80) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $344.86 | $6.95 | 📉 -0.67% | 4d 21h |
| `MSFT` | 0.012263 | $530.04 | $529.54 | $6.49 | 📉 -0.09% | 1d 23h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market presents a mixed backdrop with major equity indices showing slight movements. SPY is in an uptrend above its SMA20 with positive 1-hour momentum, while others like NVDA, QQQ, and MSFT are currently trading below their SMA20 lines. Crypto assets remain in downtrends and do not satisfy the strict trend filter or reversal triggers. Our active positions in AAPL and MSFT require careful monitoring. AAPL remains in a confirmed uptrend and is currently holding steady despite a minor intraday dip, while MSFT has dipped below the SMA20 trendline and shows a slight negative 1-hour change, but remains well within risk parameters above our hard stop-loss threshold."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in a confirmed uptrend above its SMA20. Following equity holding patience rules, we maintain the position as it fluctuates near breakeven, waiting for higher targets.
- **[HOLD] MSFT** (Confidence: 80%): MSFT is currently experiencing a minor pullback below its SMA20, but PnL is at -0.09%, far above our strict stop-loss limit of -1.8%. We maintain the position per equity holding patience rules.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Hold current positions in AAPL and MSFT respecting equity holding patience rules. AAPL is above SMA20 and we await a recovery toward the +3.0% to +5.0% take-profit target. MSFT has slipped below the SMA20; monitor it closely for potential bounce confirmation or strict stop-loss execution if it approaches -1.8%. No new positions will be opened until clear trend alignment and 1-hour reversal triggers are met."
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
