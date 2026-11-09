# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-09 12:40:38`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.14 USD** | **$20.68 USD** | **$38.81 USD** | 🔴 **-2.97%** ($-1.19) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $351.02 | $6.61 | 📈 +1.64% | 3d 18h |
| `MSFT` | 0.013089 | $534.82 | $541.58 | $7.09 | 📈 +1.26% | 2d 23h |
| `GLD` | 0.018501 | $378.35 | $377.30 | $6.98 | 📉 -0.28% | 1h 9m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The broader equity market is showing mixed recovery signs. Technology indexes like QQQ and major leaders like NVDA remain below their SMA20 with bearish daily trends, while selected defensive and mega-cap assets like AAPL, MSFT, and GLD are holding firm in confirmed uptrends above their SMA20. Cryptocurrencies continue to trade below their SMA20 trends, requiring patience and adherence to the anti-correlation and strict trend filter rules."

**Cycle Actions:**
- *No changes this cycle (HOLD)*

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain current winning and stable positions in AAPL, MSFT, and GLD, adhering to take-profit targets of +3.5% to +5.0% and strict stop-losses at -1.8% to -2.0%. Avoid opening new crypto or equity positions until clear confirmation triggers, uptrend alignments, and positive momentum are fully established."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **89** | 🎯 **42.7%** (38W / 36L / 15BE) | 🔴 **$-1.23 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-09 11:30` | 🟢 BUY | `GLD` | $7.00 | $378.35 | GLD is in a confirmed uptrend above its SMA20, market status is open, 1-hour momentum is s... |
| `2026-11-06 13:10` | 🟢 BUY | `MSFT` | $7.00 | $534.82 | MSFT is in a confirmed uptrend above its SMA20, market status is open, 1-hour RSI has reco... |
| `2026-11-05 17:40` | 🟢 BUY | `AAPL` | $6.50 | $345.35 | AAPL is in a confirmed uptrend above its SMA20, market status is open, and 1-hour momentum... |
| `2026-11-05 11:20` | 🔴 SELL (-0.15$) | `ETH-USD` | $6.85 | $2374.60 | 🚨 STOP-LOSS (CIRCUIT BREAKER): Loss of -2.10% hit safety limit (-2.0%). Liquidated by code... |
| `2026-11-05 01:41` | 🟢 BUY | `ETH-USD` | $7.00 | $2425.59 | ETH-USD is in a confirmed uptrend above its SMA20, market status is open 24/7, 1-hour RSI ... |

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
