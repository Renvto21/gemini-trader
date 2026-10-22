# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-22 14:50:55`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.37 USD** | **$6.91 USD** | **$39.28 USD** | 🔴 **-1.79%** ($-0.72) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.013196 | $530.45 | $523.96 | $6.91 | 📉 -1.22% | 1d 2h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader market is currently experiencing a pullback or corrective phase, with most major assets (MSFT, SPY, QQQ, NVDA, crypto) trading below their SMA20 trend lines. Only AAPL remains above the SMA20 trend line, but its 1-hour RSI is elevated near 70 without showing a fresh green reversal candle at this exact moment. Our open position in MSFT is down by -1.22%, which is within normal holding tolerance and above our -1.8% to -2.0% stop-loss threshold. Following equity holding patience guidelines, we will maintain our MSFT position and avoid premature rotation while waiting for broader market stabilization and confirmed uptrend reversals."

**Cycle Actions:**
- **[HOLD] MSFT** (Confidence: 85%): MSFT is currently down -1.22%, holding well above our -1.8% to -2.0% stop-loss threshold. Following the Equity Holding Patience rule, stocks require time to play out and should not be sold for being flat or slightly negative over 24-48 hours unless the stop-loss is triggered.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding MSFT with a current unrealized loss of -1.22%. Strict stop-loss is placed at -1.8% to -2.0%. AAPL is the only asset above SMA20, but lacks a valid entry trigger at present. No new positions will be opened until assets cross back above their SMA20 with positive 1-hour momentum and RSI >= 32. Maintain cash reserves above $4.00 USD."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **84** | 🎯 **45.2%** (38W / 31L / 15BE) | 🔴 **$-0.50 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-22 14:40` | 🔴 SELL (+0.17$) | `AAPL` | $10.17 | $346.52 | AAPL rsi_1h has surpassed 72 (currently 73.4) with a positive return of +1.73%, satisfying... |
| `2026-10-21 12:01` | 🟢 BUY | `MSFT` | $7.00 | $530.45 | MSFT is in a confirmed uptrend above its SMA20. The 1-hour RSI is at 36.7 (above the 32 th... |
| `2026-10-21 10:10` | 🔴 SELL (+0.12$) | `ETH-USD` | $10.07 | $2481.87 | ETH-USD rsi_1h has surpassed 72 (currently 73.7) with a positive return of +1.21%, satisfy... |
| `2026-10-20 13:51` | 🟢 BUY | `ETH-USD` | $9.95 | $2452.17 | ETH-USD muestra un excelente impulso de corto plazo con change_1h_pct positivo (+0.55%) y ... |
| `2026-10-20 13:51` | 🔴 SELL (-0.05$) | `GLD` | $9.95 | $377.90 | GLD se encuentra estancado con un rendimiento ligeramente negativo (-0.47%) y un rsi_1h de... |

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
