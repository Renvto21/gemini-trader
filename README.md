# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-01 15:40:45`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.23 USD** | **$6.95 USD** | **$39.17 USD** | 🔴 **-2.06%** ($-0.83) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.020163 | $347.17 | $344.63 | $6.95 | 📉 -0.73% | 9d 1h |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "Wall Street markets are currently closed (CERRADO), meaning equity prices are frozen and no trade execution is permitted for assets like AAPL, MSFT, QQQ, SPY, GLD, or NVDA. Among cryptocurrencies (ABIERTO 24/7), SOL-USD, ETH-USD, and BTC-USD are all currently trading below their respective SMA20 trends (bearish trend classification), failing our strict trend-following pullback criteria. Specifically, SOL-USD shows a negative 1-hour percentage change and low RSI, while ETH-USD and BTC-USD do not present a verified bullish breakout or pullback setup above the SMA20. Our single open equity position in AAPL is currently sitting at a minor drawdown of -0.73% while remaining comfortably above its SMA20 trend line. In accordance with equity holding patience rules, we maintain our position, respecting the profit target range of +3.0% to +5.0% and the strict stop-loss threshold at -1.8%."

**Cycle Actions:**
- **[HOLD] AAPL** (Confidence: 90%): AAPL remains in a confirmed uptrend above its SMA20 line despite a minor -0.73% drawdown. Adhering strictly to equity holding patience rules, we do not rotate or sell flat positions prematurely. The stop-loss is set at -1.8% and take-profit target at +3.0% to +5.0%.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding AAPL under equity holding patience rules with a current PnL of -0.73%. Wall Street is closed, so no stock actions can be taken. Crypto markets do not present any valid setups as all major coins (SOL, ETH, BTC) remain in downtrends below their SMA20 lines. We will continue holding AAPL, monitor its performance upon market reopening, and maintain cash reserves while waiting for confirmed bullish pullbacks above the SMA20."
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
