# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-28 15:01:24`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.23 USD** | **$6.97 USD** | **$39.19 USD** | 🔴 **-2.02%** ($-0.81) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $345.52 | $6.97 | 📉 -0.48% | 5d 1h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market exhibits mixed conditions. Major indices like QQQ, MSFT, and NVDA remain in a downtrend below their SMA20, while SPY and AAPL retain their bullish status above the SMA20. AAPL is holding relatively stable with a minor negative daily return but remains in an uptrend, fulfilling our equity holding patience policy. Crypto assets (BTC-USD, ETH-USD, SOL-USD) are currently under their respective SMA20 lines, failing our strict trend filter criteria, thus no crypto allocations are made. SPY is showing a high 1-hour RSI above 72 but lacks a clear pullback opportunity right now."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is currently in a confirmed uptrend above its SMA20 and is experiencing normal short-term consolidation. In accordance with equity holding patience guidelines, we maintain our position without panic, allowing it time to reach our profit target (+3.0% to +5.0%) while protecting downside via our strict stop-loss rules.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain our current AAPL holding in accordance with equity holding patience guidelines as it trades above its SMA20. Watch AAPL closely for a push toward our profit target (+3.0% to +5.0%) or maintain the stop-loss limit discipline at -1.8% to -2.0%. Ensure cash reserves stay safely above the $4.00 USD minimum threshold. Continue monitoring SPY and other potential candidates for valid pullbacks above SMA20 with RSI >= 32 and positive 1-hour percentage change before considering any new allocations."
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
