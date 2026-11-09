# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-09 17:00:52`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.14 USD** | **$20.79 USD** | **$38.92 USD** | 🔴 **-2.69%** ($-1.08) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.018821 | $345.35 | $351.39 | $6.61 | 📈 +1.75% | 3d 23h |
| `MSFT` | 0.013089 | $534.82 | $546.93 | $7.16 | 📈 +2.26% | 3d 3h |
| `GLD` | 0.018501 | $378.35 | $379.18 | $7.02 | 📈 +0.22% | 5h 30m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The portfolio holds three solid positions (AAPL, MSFT, and GLD) that are maintaining structural uptrends above their SMA20. MSFT and AAPL are showing healthy gains, approaching or nearing take-profit territory as momentum builds. GLD is steady with positive 1H momentum. The broader market shows multiple assets still trading below their SMA20, meaning strict trend filters must be applied and crypto avoided due to lack of a confirmed healthy uptrend structure. Overall sentiment is cautiously optimistic as equities recover, and our risk management parameters remain fully active."

**Cycle Actions:**
- **[HOLD] MSFT** (Confidence: 90%): MSFT is in a confirmed uptrend above its SMA20 with a solid profit of +2.26%. Holding per equity holding patience rule until take-profit target (+3% to +5%) or RSI > 72 is reached.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintain current positions in AAPL, MSFT, and GLD. Monitor 1-hour RSI for MSFT and AAPL closely to take profits if RSI exceeds 72 or gains reach the +3.0% to +5.0% target. Adhere strictly to the -2.0% stop-loss threshold. Continue avoiding crypto and below-SMA20 assets until proper confirmation triggers are met."
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
