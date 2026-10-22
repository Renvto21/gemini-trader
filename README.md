# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-22 11:50:48`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.20 USD** | **$17.00 USD** | **$39.20 USD** | 🔴 **-2.00%** ($-0.80) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $343.48 | $10.08 | 📈 +0.83% | 1d 23h |
| `MSFT` | 0.013196 | $530.45 | $524.40 | $6.92 | 📉 -1.14% | 23h 49m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market remains mostly under pressure with major indices and stocks trading below their SMA20, signaling a cautious environment. AAPL continues to hold firm in an uptrend above its SMA20 with solid momentum (+0.83% PnL), whereas MSFT has dipped slightly below its SMA20 (-1.14% PnL) but remains well within acceptable risk limits before any stop-loss triggers. Cryptocurrencies are displaying corrective behavior with RSI levels recovering from extreme lows, but strict trend rules prevent new entries as they remain below their SMA20."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in a confirmed uptrend above SMA20 with positive PnL (+0.83%). Following equity holding patience rules, we let winners run toward the +3% to +5% target.
- **[HOLD] MSFT** (Confidence: 80%): MSFT is experiencing a minor pullback (-1.14%) but has not breached the strict -1.8% to -2.0% stop-loss threshold. Patience is maintained for equities per portfolio rules.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain patience with equity holdings AAPL and MSFT. AAPL remains in a strong uptrend above SMA20; hold for target gains (+3% to +5%). MSFT is slightly below SMA20 (-1.14%); monitor closely for a recovery or a hard stop-loss trigger at -1.8% to -2.0%. Keep crypto exposure flat until a confirmed uptrend and valid reversal trigger appear."
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
