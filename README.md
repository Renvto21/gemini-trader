# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-21 07:30:50`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.89 USD** | **$39.02 USD** | 🔴 **-2.46%** ($-0.98) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $339.50 | $9.97 | 📉 -0.33% | 19h 29m |
| `ETH-USD` | 0.004058 | $2452.17 | $2446.27 | $9.93 | 📉 -0.24% | 17h 39m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Stock markets are currently closed with prices frozen, while cryptocurrency markets are open 24/7. AAPL is currently held with stable performance while its market is closed. ETH-USD is slightly down by -0.24% with a 1-hour change of -0.28%, sitting below the SMA20 trend filter. BTC-USD is in an uptrend above SMA20 but currently exhibits a slightly negative 1-hour candle (-0.17%), so we wait for a green reversal candle. Overall, adherence to risk management, equity patience, and stop-loss/take-profit levels remains paramount."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 80%): AAPL is currently held in an uptrend above SMA20. Following equity holding patience rules, stocks should not be rotated or sold solely due to being flat or mildly negative over a short timeframe while the market is closed.
- **[HOLD] ETH-USD** (Confidence: 75%): ETH-USD is currently open and held within acceptable risk parameters (-0.24% PnL), waiting to reach the asymmetric take-profit target of +3.0% to +5.0% or to respect the hard stop-loss threshold at -1.8%.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Hold AAPL in line with equity holding patience while markets remain closed. Monitor ETH-USD for either a take-profit target between +3.0% and +5.0% or a stop-loss execution if it drops past -1.8%. Watch BTC-USD for a potential pullback entry once the 1-hour price action confirms a positive reversal candle while remaining above SMA20."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **82** | 🎯 **43.9%** (36W / 31L / 15BE) | 🔴 **$-0.79 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-20 13:51` | 🟢 BUY | `ETH-USD` | $9.95 | $2452.17 | ETH-USD muestra un excelente impulso de corto plazo con change_1h_pct positivo (+0.55%) y ... |
| `2026-10-20 13:51` | 🔴 SELL (-0.05$) | `GLD` | $9.95 | $377.90 | GLD se encuentra estancado con un rendimiento ligeramente negativo (-0.47%) y un rsi_1h de... |
| `2026-10-20 12:01` | 🟢 BUY | `GLD` | $10.00 | $379.70 | GLD presenta un RSI de 1 hora en 31.4, acercándose a la zona ideal de sobreventa para acti... |
| `2026-10-20 12:01` | 🟢 BUY | `AAPL` | $10.00 | $340.64 | AAPL se encuentra en tendencia alcista diaria con un RSI de 1 hora en 33.1 (cercano a sobr... |
| `2026-10-20 11:10` | 🔴 SELL (+0.12$) | `BTC-USD` | $8.69 | $82949.93 | BTC-USD muestra un RSI de 1 hora en 72.2 (sobrecompra) y un rendimiento positivo de +1.45%... |

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
