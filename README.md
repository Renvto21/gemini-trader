# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-28 16:00:54`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.23 USD** | **$6.94 USD** | **$39.17 USD** | 🔴 **-2.08%** ($-0.83) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $344.40 | $6.94 | 📉 -0.80% | 5d 2h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The market shows mixed conditions with several major equities and crypto assets trading below their SMA20 trend filters, signaling caution. AAPL remains our sole open position in a confirmed uptrend above its SMA20, currently experiencing a minor pullback with a -0.8% PnL, which respects our equity holding patience rule. SPY is also above its SMA20 but has a high 1-hour RSI near 79.8 and negative 1-hour momentum, while other candidates like MSFT, NVDA, GLD, QQQ, and crypto assets fail to meet the strict pullback confirmation criteria (either below SMA20 or lacking positive 1-hour percentage change). Cash reserves remain healthy at $32.23 USD."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in a confirmed uptrend above its SMA20 and currently shows a minor unrealized loss of -0.8%. In accordance with equity holding patience rules for equities, we will hold the position and allow it time to recover toward our profit target without prematurely cutting it, while maintaining vigilance over our stop-loss parameters.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain the current AAPL position under equity holding patience guidelines, tracking toward the profit target of +3.0% to +5.0% while monitoring the hard stop-loss at -1.8% to -2.0%. Keep cash reserves secure above the $4.00 minimum threshold and wait for assets above their SMA20 to exhibit positive 1-hour percentage changes (change_1h_pct > 0.0) alongside 1-hour RSI >= 32 before entering new positions."
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
