# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-22 14:20:48`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.20 USD** | **$17.08 USD** | **$39.28 USD** | 🔴 **-1.81%** ($-0.72) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $346.29 | $10.17 | 📈 +1.66% | 2d 2h |
| `MSFT` | 0.013196 | $530.45 | $523.97 | $6.91 | 📉 -1.22% | 1d 2h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market is experiencing a broad pullback, with major indices and equities trading below their SMA20 trend lines in bearish daily structures. AAPL remains the sole asset showing a confirmed bullish trend above its SMA20 with solid momentum and an RSI approaching the take-profit threshold. MSFT has dipped slightly to -1.22%, currently holding well above our strict stop-loss limit of -1.8% to -2.0%. Cryptocurrencies and other major equities are currently in downtrends or lacking clean reversal triggers, prompting a patient, defensive posture."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is in a confirmed uptrend above SMA20 with a positive PnL of +1.66%. Sticking to the equity holding patience rule while approaching our +3.0% to +5.0% profit target.
- **[HOLD] MSFT** (Confidence: 85%): MSFT is currently experiencing a minor pullback at -1.22%, well within our acceptable risk boundary and far above the strict -1.8% to -2.0% stop-loss threshold.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Continue to hold AAPL patiently, targeting a take-profit gain of +3.0% to +5.0% or selling if rsi_1h exceeds 72 with profit >= +2.5%. Hold MSFT while strictly monitoring the -1.8% to -2.0% stop-loss threshold. Do not enter any new long positions until assets fulfill both the uptrend condition (above SMA20) and the 1-hour reversal trigger (rsi_1h >= 32 and change_1h_pct > 0.0)."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **83** | 🎯 **44.6%** (37W / 31L / 15BE) | 🔴 **$-0.67 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-21 12:01` | 🟢 BUY | `MSFT` | $7.00 | $530.45 | MSFT is in a confirmed uptrend above its SMA20. The 1-hour RSI is at 36.7 (above the 32 th... |
| `2026-10-21 10:10` | 🔴 SELL (+0.12$) | `ETH-USD` | $10.07 | $2481.87 | ETH-USD rsi_1h has surpassed 72 (currently 73.7) with a positive return of +1.21%, satisfy... |
| `2026-10-20 13:51` | 🟢 BUY | `ETH-USD` | $9.95 | $2452.17 | ETH-USD muestra un excelente impulso de corto plazo con change_1h_pct positivo (+0.55%) y ... |
| `2026-10-20 13:51` | 🔴 SELL (-0.05$) | `GLD` | $9.95 | $377.90 | GLD se encuentra estancado con un rendimiento ligeramente negativo (-0.47%) y un rsi_1h de... |
| `2026-10-20 12:01` | 🟢 BUY | `GLD` | $10.00 | $379.70 | GLD presenta un RSI de 1 hora en 31.4, acercándose a la zona ideal de sobreventa para acti... |

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
