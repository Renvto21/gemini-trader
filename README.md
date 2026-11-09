# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-09 17:40:50`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.14 USD** | **$20.78 USD** | **$38.92 USD** | 🔴 **-2.70%** ($-1.08) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $350.75 | $6.60 | 📈 +1.56% | 4d 0h |
| `MSFT` | 0.013089 | $534.82 | $547.15 | $7.16 | 📈 +2.31% | 3d 4h |
| `GLD` | 0.018501 | $378.35 | $379.36 | $7.02 | 📈 +0.27% | 6h 9m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The current market environment shows major equity indices and crypto assets under pressure or lingering in downtrends below their SMA20, although specific high-quality equities and defensive assets like AAPL, MSFT, and GLD remain in confirmed uptrends and are performing well. Strict adherence to trend filters prevents exposure to falling knives in assets like NVDA, QQQ, and crypto tokens, while holding existing equity positions that comply with the equity holding patience rule."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL is in a confirmed uptrend above its SMA20 with a positive unrealized PnL of +1.56%. Following equity holding patience, the position is maintained to let winners run toward the +3.0% to +5.0% profit target zone.
- **[HOLD] MSFT** (Confidence: 90%): MSFT is in a confirmed uptrend above its SMA20 showing steady performance with a +2.31% PnL. Holding the position to capture full upside momentum towards the take-profit target.
- **[HOLD] GLD** (Confidence: 85%): GLD remains in an uptrend above its SMA20. The position is stable and kept open to benefit from strong defensive and gold sector trends.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing positions in AAPL, MSFT, and GLD. Monitor 1-hour RSI and price action for take-profit opportunities once RSI exceeds 72 and returns reach the +3.0% to +5.0% target band. Keep strict stop-losses active at -2.0%. Continue avoiding all crypto and assets in downtrends due to the absence of valid trend and reversal confirmation triggers."
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
