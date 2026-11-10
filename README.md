# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-10 07:50:44`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.14 USD** | **$20.76 USD** | **$38.89 USD** | 🔴 **-2.76%** ($-1.11) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $350.69 | $6.60 | 📈 +1.55% | 4d 14h |
| `MSFT` | 0.013089 | $534.82 | $545.18 | $7.14 | 📈 +1.94% | 3d 18h |
| `GLD` | 0.018501 | $378.35 | $379.53 | $7.02 | 📈 +0.31% | 20h 19m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The overall market shows Wall Street equities closed for the weekend/pre-market with major indices like QQQ, SPY, and NVDA currently in bearish daily trends below their SMA20. However, our existing equity holdings (AAPL, MSFT, GLD) remain strong in confirmed uptrends above their SMA20 and are exhibiting resilient price action, holding modest unrealized gains. Crypto markets are open 24/7, but BTC-USD, ETH-USD, and SOL-USD remain deep in bearish trends with negative 24-hour momentum and failing 1-hour reversal triggers (RSI well below 32 and negative hourly returns), meaning we must strictly avoid buying crypto to prevent catching falling knives."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): Asset is in a confirmed uptrend above SMA20 with positive unrealized gains (+1.55%). Following equity holding patience guidelines to let the winning trade run toward our take-profit target.
- **[HOLD] MSFT** (Confidence: 90%): Asset is in a confirmed uptrend above SMA20 with solid unrealized gains (+1.94%). Maintaining position to capture further upside toward the +3% to +5% target.
- **[HOLD] GLD** (Confidence: 85%): Gold ETF remains in an uptrend above SMA20. Holding steady while it consolidates recent gains.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain current equity positions (AAPL, MSFT, GLD) as they display stability in confirmed uptrends. Patiently hold through minor hourly fluctuations while monitoring for our take-profit targets (+3% to +5%) or circuit-breaker stop-losses (-2%). Avoid all crypto assets due to ongoing bearish trends and lack of confirmed 1-hour reversal triggers. Preserve cash reserves above $4.00 USD."
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
