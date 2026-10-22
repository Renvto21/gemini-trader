# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-22 13:52:11`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.20 USD** | **$17.05 USD** | **$39.25 USD** | 🔴 **-1.89%** ($-0.75) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $345.25 | $10.14 | 📈 +1.35% | 2d 1h |
| `MSFT` | 0.013196 | $530.45 | $523.99 | $6.91 | 📉 -1.22% | 1d 1h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market is experiencing a broad pullback, with most tracked assets trading below their respective SMA20 and displaying bearish short-term momentum. AAPL remains the standout performer, holding strong in an uptrend above its SMA20 with solid daily and hourly RSI levels, yielding a positive return (+1.35%). MSFT has slipped slightly below its entry price to -1.22%, but per equity holding patience rules, it should be given time unless the hard stop-loss of -1.8% to -2.0% is breached. No new buy signals are triggered across the wider market because other assets fail either the trend filter (below SMA20) or lack a confirmed 1-hour positive reversal candle."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is in a confirmed uptrend above its SMA20, showing steady performance with a +1.35% return. Sticking to equity holding patience rules to let the winner run toward the +3.0% to +5.0% profit target.
- **[HOLD] MSFT** (Confidence: 85%): MSFT is currently down -1.22%, which is within normal equity fluctuation bounds and above the strict -1.8% to -2.0% stop-loss circuit breaker. Allowing equities adequate time to play out per core trading discipline.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Continue to hold AAPL and monitor for profit-taking targets (+3.0% to +5.0% gain, or rsi_1h > 72 with profit >= +2.5%). Hold MSFT patiently while closely monitoring its price against the -1.8% to -2.0% strict stop-loss threshold. Maintain strong cash reserves above $4.00 USD and wait for new assets to clear both the SMA20 trend filter and the 1-hour reversal trigger (rsi_1h >= 32 and change_1h_pct > 0.0) before deploying additional capital."
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
