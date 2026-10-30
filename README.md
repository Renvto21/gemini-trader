# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-30 15:30:46`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.23 USD** | **$6.92 USD** | **$39.15 USD** | 🔴 **-2.13%** ($-0.85) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $343.43 | $6.92 | 📉 -1.08% | 7d 1h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market is currently experiencing a strong risk-off pullback, with nearly all tracked assets (GLD, MSFT, NVDA, QQQ, SPY, and major cryptocurrencies) trading below their respective SMA20 trends and showing negative 24-hour and 7-day performances. AAPL remains the sole asset holding a confirmed bullish trend above its SMA20 despite a mild intraday pullback (-0.9% 1h change, rsi_1h at 46.7). Because the 1-hour change is currently negative, our reversal confirmation trigger is not met for new entries. AAPL's PnL is at -1.08%, well within our acceptable holding threshold, and following our equity holding patience rule, we will continue to hold it as long as it respects the strict -1.8% to -2.0% stop-loss boundary."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL remains in a confirmed structural uptrend above its SMA20. Although experiencing a minor 1-hour pullback (-0.9%), it is well above our strict -1.8% stop-loss limit (-1.08% current PnL). Following our equity holding patience and trend-following rules, we maintain our position and wait for a green 1-hour candle before considering adding or taking profit.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "We are continuing to hold our AAPL position. We will monitor AAPL closely; if it hits our stop-loss threshold near -1.8% to -2.0% (~$340.40), we will exit immediately. Take-profit target remains set between +3.5% and +5.0% gain. No new buy orders will be placed until market conditions improve and potential candidates satisfy both the uptrend filter and positive 1-hour reversal triggers (rsi_1h >= 32 and change_1h_pct > 0.0)."
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
