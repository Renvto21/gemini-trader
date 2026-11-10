# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-10 02:40:43`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.14 USD** | **$20.76 USD** | **$38.89 USD** | 🔴 **-2.76%** ($-1.11) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $350.69 | $6.60 | 📈 +1.55% | 4d 8h |
| `MSFT` | 0.013089 | $534.82 | $545.18 | $7.14 | 📈 +1.94% | 3d 13h |
| `GLD` | 0.018501 | $378.35 | $379.53 | $7.02 | 📈 +0.31% | 15h 9m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Wall Street markets are currently closed ('CERRADO'), with prices frozen. Our active positions in AAPL, MSFT, and GLD are safely positioned in confirmed uptrends above their SMA20, showing modest positive returns. Cryptocurrencies are open (24/7), but both BTC-USD, ETH-USD, and SOL-USD remain strictly in bear trends (below SMA20) with daily RSIs indicating weakness and failure to meet trend-following criteria. Consequently, no new crypto entries are warranted under quantitative risk rules."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): Asset is in a confirmed uptrend above SMA20, markets are closed, and the position is profitable. Patiently holding per equity holding guidelines.
- **[HOLD] MSFT** (Confidence: 100%): Asset remains stable in an uptrend above SMA20 during market closure. Holding to let winners run.
- **[HOLD] GLD** (Confidence: 100%): Market is closed and GLD is above SMA20. Maintaining position per capital preservation rules.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain current equity and commodity positions (AAPL, MSFT, GLD) as equity markets are closed and positions remain stable above SMA20. Monitor stop-loss thresholds (-2.0%) and target profits (+3.0% to +5.0%). Keep crypto sidelined until a confirmed daily trend reversal above the SMA20 occurs."
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
