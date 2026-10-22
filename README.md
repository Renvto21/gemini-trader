# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-22 14:01:09`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.20 USD** | **$17.08 USD** | **$39.28 USD** | 🔴 **-1.80%** ($-0.72) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $345.81 | $10.15 | 📈 +1.52% | 2d 1h |
| `MSFT` | 0.013196 | $530.45 | $525.23 | $6.93 | 📉 -0.98% | 1d 1h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broad market is exhibiting generalized weakness with major indices and assets such as QQQ, SPY, NVDA, and crypto pairs trading below their respective SMA20 trend filters, signaling a defensive environment. AAPL remains a standout holding in a confirmed uptrend above its SMA20 with solid momentum (rsi_1h at 65.6 and up +1.52%). MSFT has slipped slightly below its SMA20 amid broader market pullbacks, recording a -0.98% unrealized loss, but remains well above the strict stop-loss threshold of -1.8% to -2.0%. Crypto markets are showing downward pressure with negative 24-hour changes and low hourly RSI levels. Given strict quantitative trend filters requiring assets to be above the SMA20 and displaying positive 1-hour reversal momentum (change_1h_pct > 0.0), no new buy opportunities meet our criteria at this moment."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL is in a confirmed uptrend above its SMA20 with solid gains (+1.52%). Following equity holding patience rules, we let winners run towards our +3.0% to +5.0% profit targets.
- **[HOLD] MSFT** (Confidence: 80%): MSFT is currently experiencing a minor pullback down -0.98%, which is well within our acceptable drawdown range before hitting the strict -1.8% to -2.0% stop-loss threshold. Equity patience applies.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Continue to hold AAPL and monitor for profit-taking targets (+3.0% to +5.0% gain, or rsi_1h > 72 with profit >= +2.5%). Hold MSFT patiently despite its temporary dip below SMA20, maintaining strict discipline against the -1.8% to -2.0% stop-loss threshold. Keep cash reserves safely above $4.00 USD ($22.20 currently) and wait for assets to clear both the SMA20 uptrend requirement and the 1-hour reversal trigger (rsi_1h >= 32 and change_1h_pct > 0.0) before deploying new capital."
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
