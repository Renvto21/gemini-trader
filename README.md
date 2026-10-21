# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-21 05:40:39`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.91 USD** | **$39.03 USD** | 🔴 **-2.42%** ($-0.97) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $339.50 | $9.97 | 📉 -0.33% | 17h 39m |
| `ETH-USD` | 0.004058 | $2452.17 | $2449.49 | $9.94 | 📉 -0.11% | 15h 49m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The current equity markets (AAPL, MSFT, SPY, QQQ, NVDA, GLD) are closed, showing frozen prices. AAPL remains held patiently according to equity holding patience guidelines, hovering near our entry with a minor -0.33% PnL. In the crypto sector, which is trading 24/7, ETH-USD is currently held but its 1-hour change has turned slightly negative (-0.15%), while its trend remains bearish below the SMA20. However, patience is required as it hasn't hit stop-loss limits (-1.8%) or profit targets (+3.0%). Other crypto assets like BTC-USD and SOL-USD are also in downtrends below their SMA20, precluding any new purchases under strict trend-following rules."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): Holding AAPL in adherence to equity holding patience guidelines. The position is stable with minor fluctuation and market hours are closed.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain AAPL and ETH-USD positions. Monitor ETH-USD for profit target execution between +3.0% and +5.0%, or strict stop-loss protection near -1.8%. Respect the single crypto holding constraint and avoid opening any new positions while current assets develop. Keep sufficient cash reserve ($19.12) intact."
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
