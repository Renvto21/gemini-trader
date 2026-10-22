# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-22 14:11:03`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.20 USD** | **$17.06 USD** | **$39.26 USD** | 🔴 **-1.85%** ($-0.74) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $345.75 | $10.15 | 📈 +1.50% | 2d 2h |
| `MSFT` | 0.013196 | $530.45 | $523.99 | $6.91 | 📉 -1.22% | 1d 2h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market is currently experiencing a strong pullback or short-term correction, with major indices and equities like MSFT, QQQ, SPY, NVDA, and crypto assets trading below their SMA20 trends. AAPL remains resilient as the sole asset holding an uptrend above its SMA20 with a positive 24h change (+0.51%) and a 1h RSI of 65.3. Most other assets show negative 1h price momentum (change_1h_pct < 0.0), failing our reversal confirmation trigger. Cash reserves are currently healthy at $22.20 USD."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 85%): AAPL remains in a confirmed uptrend above its SMA20 with a solid PnL of +1.5%. Adhering to equity holding patience and asymmetric reward targets (+3.0% to +5.0%), we hold position.
- **[HOLD] MSFT** (Confidence: 80%): MSFT is currently experiencing a temporary pullback below its SMA20 with a PnL of -1.22%. Since it has not hit the hard stop-loss threshold (-1.8% to -2.0%), we maintain our position and wait for trend recovery.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Continue to hold AAPL patiently as it approaches our target take-profit zone of +3.0% to +5.0% (currently at +1.5%). Hold MSFT despite its dip, strictly respecting the -1.8% to -2.0% stop-loss threshold while monitoring for a bounce above SMA20. Do not deploy capital into any crypto or equities until both the uptrend requirement and the 1-hour reversal confirmation (rsi_1h >= 32 and change_1h_pct > 0.0) are fully satisfied."
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
