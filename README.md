# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-22 09:01:02`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.20 USD** | **$17.13 USD** | **$39.33 USD** | 🔴 **-1.68%** ($-0.67) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $343.99 | $10.10 | 📈 +0.98% | 1d 20h |
| `MSFT` | 0.013196 | $530.45 | $532.95 | $7.03 | 📈 +0.47% | 20h 59m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market state shows Wall Street equities (AAPL, MSFT, SPY, QQQ, NVDA, GLD) in a CERRADO (closed) status, meaning prices are frozen and no transactions can occur on equities at this moment. In the crypto sector, assets like SOL-USD, BTC-USD, and ETH-USD are ABIERTO (24/7), but all three are currently in bearish trends below their respective SMA20 with low 1-hour RSI levels or failing to meet strict trend-following pullback criteria (avoiding falling knives). Our current equity positions in AAPL (+0.98%) and MSFT (+0.47%) are holding steady and showing patience as per rule-based guidance, while cash reserves remain healthy at $22.20."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in an uptrend above SMA20 with a positive PnL of +0.98%. Per equity holding patience rules, we do not sell flat or modest positions prematurely and let them run toward the +3.0% to +5.0% target.
- **[HOLD] MSFT** (Confidence: 85%): MSFT is in a confirmed uptrend above SMA20 with a modest positive return. Holding patiently to let the position develop toward our asymmetric risk/reward profit target.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing equity positions in AAPL and MSFT patiently as they progress toward our take-profit target of +3.0% to +5.0%, keeping a tight eye on the stop-loss threshold (-2.0%). Keep crypto sidelined because SOL, BTC, and ETH remain below their SMA20 with weak trend structures, violating our trend-following rules. Wait for market open and proper confirmation triggers before considering new allocations."
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
