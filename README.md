# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-01 22:30:46`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.23 USD** | **$6.95 USD** | **$39.17 USD** | 🔴 **-2.06%** ($-0.83) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $344.63 | $6.95 | 📉 -0.73% | 9d 8h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader equity market remains under pressure with major indices like QQQ, SPY, and MSFT trading below their SMA20 trend filters, signaling bearish conditions where catching falling knives must be strictly avoided. AAPL is the sole asset maintaining a confirmed uptrend above its SMA20, currently held in the portfolio with a modest loss of -0.73%, well within our risk parameters. Wall Street is currently closed (market status CERRADO), preventing any stock operations. In the crypto markets, assets like ETH-USD and BTC-USD show positive 1-hour changes and bouncing RSI levels, but they remain strictly in bearish trends below their respective SMA20 lines, failing our trend-following criteria."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is currently the only asset in the portfolio and the entire market maintaining a confirmed uptrend above its SMA20. Following equity holding patience and strict trend filters, we hold this position as Wall Street is closed and the current drawdown (-0.73%) is well above our -2.0% stop-loss threshold.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain the AAPL position as it is the only asset holding a confirmed uptrend above the SMA20, respecting our equity holding patience and stop-loss rules. Keep cash reserves secure ($32.23) and refrain from crypto entries until a crypto asset demonstrates a confirmed uptrend above its SMA20 accompanied by strong bounce triggers. Monitor AAPL closely for take-profit opportunities if it reaches +3.5% to +5.0% gains or stop-loss limits near -2.0% upon market re-opening."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **86** | 🎯 **44.2%** (38W / 33L / 15BE) | 🔴 **$-0.64 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-28 13:21` | 🔴 SELL (-0.02$) | `MSFT` | $6.48 | $528.16 | MSFT has shifted to a bearish trend below its SMA20 and current performance is near our st... |
| `2026-10-26 12:01` | 🟢 BUY | `MSFT` | $6.50 | $530.04 | MSFT is in a confirmed uptrend above its SMA20, and the 1-hour RSI (62.8) and 1-hour perce... |
| `2026-10-23 13:40` | 🟢 BUY | `AAPL` | $7.00 | $347.17 | AAPL is in a confirmed uptrend above its SMA20, satisfying our strict trend filter. The 1-... |
| `2026-10-22 16:00` | 🔴 SELL (-0.12$) | `MSFT` | $6.88 | $521.40 | MSFT has dropped to a PnL of -1.71%, closely approaching our mandatory stop-loss threshold... |
| `2026-10-22 14:40` | 🔴 SELL (+0.17$) | `AAPL` | $10.17 | $346.52 | AAPL rsi_1h has surpassed 72 (currently 73.4) with a positive return of +1.73%, satisfying... |

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
