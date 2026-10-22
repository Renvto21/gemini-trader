# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-22 10:50:57`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.20 USD** | **$17.07 USD** | **$39.27 USD** | 🔴 **-1.83%** ($-0.73) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $345.40 | $10.14 | 📈 +1.40% | 1d 22h |
| `MSFT` | 0.013196 | $530.45 | $525.35 | $6.93 | 📉 -0.96% | 22h 49m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market is currently experiencing a widespread pullback, with most equities and crypto assets trading below their SMA20 lines in a bearish short-term trend. AAPL remains a notable exception, maintaining a confirmed bullish trend above its SMA20 with positive hourly and daily momentum (rsi_1h at 61.3, change_1h_pct at +0.39%), currently showing a profit of +1.4%. MSFT has dipped slightly below its SMA20 (-0.96% PnL), but per equity holding patience rules, it will not be sold prematurely as it has only been held for under 24 hours and has not triggered the strict -2.0% stop-loss threshold. No crypto assets currently satisfy both the confirmed uptrend filter and the reversal triggers."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in a confirmed uptrend above its SMA20 with strong momentum. It is being held patiently as it approaches the +3.0% to +5.0% profit target zone, adhering to equity holding guidelines.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Continue holding AAPL as it approaches the +3.0% to +5.0% profit target zone; exit if RSI surpasses 72 or the target is reached. Maintain MSFT position under equity patience rules unless the hard stop-loss at -2.0% is triggered. Keep cash reserves safe above $22.00 USD and avoid opening new positions until market-wide trends stabilize above SMA20."
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
