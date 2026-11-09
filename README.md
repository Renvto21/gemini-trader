# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-09 14:00:57`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.14 USD** | **$20.65 USD** | **$38.79 USD** | 🔴 **-3.03%** ($-1.21) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $350.30 | $6.59 | 📈 +1.43% | 3d 20h |
| `MSFT` | 0.013089 | $534.82 | $541.61 | $7.09 | 📈 +1.27% | 3d 0h |
| `GLD` | 0.018501 | $378.35 | $376.69 | $6.97 | 📉 -0.44% | 2h 30m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The portfolio currently holds AAPL, MSFT, and GLD, all of which remain above their SMA20 uptrend filter, preserving capital and remaining stable despite normal intraday noise. The crypto assets (BTC, ETH, SOL) continue to trade in a downtrend below their SMA20 and do not qualify for long entries under our strict trend rules. Other major indices like SPY and QQQ are also still below their SMA20 lines. Cash reserves stand at $18.14 USD, maintaining a healthy liquidity buffer above the $4.00 minimum requirement. Asymmetric risk-reward parameters dictate patience with existing positions while waiting for clear trend alignment and momentum triggers."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 100%): Asset is in a confirmed uptrend above SMA20, showing a positive PnL and following our equity holding patience rule.
- **[HOLD] MSFT** (Confidence: 100%): Asset is in a confirmed uptrend above SMA20, showing positive momentum and adhering to equity patience guidelines.
- **[HOLD] GLD** (Confidence: 100%): Asset remains above SMA20 in a solid uptrend; minor pullback is within normal noise boundaries, well above stop-loss thresholds.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain existing positions in AAPL, MSFT, and GLD toward our +3.5% to +5.0% take-profit targets, keeping a strict stop-loss discipline at -1.8% to -2.0%. Do not enter any new equity or crypto trades until an asset demonstrates a confirmed uptrend above its SMA20, an RSI >= 32, and positive 1-hour momentum confirmation."
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
