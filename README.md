# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-10-26 13:21:02`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$25.75 USD** | **$13.44 USD** | **$39.19 USD** | 🔴 **-2.02%** ($-0.81) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $344.38 | $6.94 | 📉 -0.80% | 2d 23h |
| `MSFT` | 0.012263 | $530.04 | $530.09 | $6.50 | 📈 +0.01% | 1h 19m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broad market shows mixed conditions with most major indices and crypto assets trading below their respective SMA20 lines, indicating a persistent bearish trend filter environment. MSFT remains in a confirmed bullish trend above the SMA20 with positive 1-hour momentum, while AAPL continues to consolidate above its SMA20 despite a slight pullback. Cryptocurrencies remain below the SMA20 trend line and are avoided in line with our strict quantitative anti-falling-knife and anti-correlation filters."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 80%): AAPL remains in a valid bullish uptrend above the SMA20. Following equity holding patience guidelines, we hold the position through minor fluctuations and monitor for take-profit targets (+3% to +5%) or stop-loss limits (-1.8%).
- **[HOLD] MSFT** (Confidence: 85%): MSFT is trading in a confirmed uptrend above the SMA20 with positive short-term momentum. Maintaining the position per equity holding patience rules while tracking profit targets.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing positions in AAPL and MSFT in accordance with equity holding patience guidelines. Do not exit AAPL or MSFT prematurely on minor fluctuations. Closely monitor the stop-loss thresholds (-1.8% to -2.0%) for both holdings and target profit taking between +3.0% and +5.0%. Avoid all crypto assets as long as they remain below the SMA20 trend line."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **85** | 🎯 **44.7%** (38W / 32L / 15BE) | 🔴 **$-0.62 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-26 12:01` | 🟢 BUY | `MSFT` | $6.50 | $530.04 | MSFT is in a confirmed uptrend above its SMA20, and the 1-hour RSI (62.8) and 1-hour perce... |
| `2026-10-23 13:40` | 🟢 BUY | `AAPL` | $7.00 | $347.17 | AAPL is in a confirmed uptrend above its SMA20, satisfying our strict trend filter. The 1-... |
| `2026-10-22 16:00` | 🔴 SELL (-0.12$) | `MSFT` | $6.88 | $521.40 | MSFT has dropped to a PnL of -1.71%, closely approaching our mandatory stop-loss threshold... |
| `2026-10-22 14:40` | 🔴 SELL (+0.17$) | `AAPL` | $10.17 | $346.52 | AAPL rsi_1h has surpassed 72 (currently 73.4) with a positive return of +1.73%, satisfying... |
| `2026-10-21 12:01` | 🟢 BUY | `MSFT` | $7.00 | $530.45 | MSFT is in a confirmed uptrend above its SMA20. The 1-hour RSI is at 36.7 (above the 32 th... |

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
