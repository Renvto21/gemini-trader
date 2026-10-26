# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-26 14:50:58`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.75 USD** | **$13.41 USD** | **$39.16 USD** | 🔴 **-2.10%** ($-0.84) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $342.78 | $6.91 | 📉 -1.26% | 3d 1h |
| `MSFT` | 0.012263 | $530.04 | $530.17 | $6.50 | 📈 +0.02% | 2h 49m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The market shows mixed conditions with most major indices and crypto assets trading below their respective SMA20 lines, indicating prevailing bearish or consolidating trends. MSFT and AAPL remain in confirmed uptrends above their SMA20. MSFT shows a high 1h RSI of 72.3, nearing take-profit territory, while AAPL experiences a minor pullback with an RSI of 36.1 and a slightly negative 1h change, not yet satisfying the positive 1h bounce confirmation trigger for additional buying."

**Cycle Actions:**
- **[HOLD] MSFT** (Confidence: 85%): MSFT is in a confirmed uptrend above its SMA20 with solid performance. RSI(1h) is at 72.3, approaching take-profit targets (+3% to +5%), but holding per equity patience rules as it continues to perform well without hitting stop-losses.
- **[HOLD] AAPL** (Confidence: 80%): AAPL remains above its SMA20 trendline. Although experiencing a minor pullback (pnl -1.26%), equity holding patience rules dictate we do not panic-sell flat or slightly down positions unless the hard stop-loss of -1.8% to -2.0% is triggered.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain current equity positions in MSFT and AAPL. Monitor MSFT for potential take-profit if gains reach +3.0% to +5.0% or momentum peaks. Keep AAPL open as equity holdings require patience, honoring the stop-loss limit near -1.8% to -2.0%. Avoid all crypto and downtrending assets due to strict trend filtering."
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
