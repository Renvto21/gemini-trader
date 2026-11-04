# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-04 14:11:05`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$32.09 USD** | **$7.14 USD** | **$39.23 USD** | 🔴 **-1.92%** ($-0.77) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012839 | $545.20 | $555.79 | $7.14 | 📈 +1.94% | 2h 40m |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "The market is experiencing a strong post-election rally following the US midterm elections, with major equity indices like SPY and key tech leaders such as MSFT and AAPL breaking out above their SMA20 trends. MSFT is currently showing solid performance with a +1.94% gain, holding an RSI_1h of 77.3. Cryptocurrencies like BTC-USD and ETH-USD are in uptrends but currently show extremely overbought 1H RSI levels (>90), precluding immediate new entries until a healthy pullback occurs."

**Cycle Actions:**
- **[HOLD] MSFT** (Confidence: 85%): MSFT is in a confirmed uptrend above its SMA20 with solid momentum and a current profit of +1.94%. Adhering to the equity holding patience rule and asymmetric risk/reward guidelines, we will let this winner run toward our +3.5% to +5.0% target while protecting capital with a strict stop-loss.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Holding MSFT position with a current profit of +1.94%. Will maintain the position and let winners run toward our +3.5% to +5.0% target, while keeping a strict stop-loss at -2.0%. Crypto assets (BTC-USD, ETH-USD) are in uptrends but currently show overbought 1H RSI levels above 90; will wait for a healthier pullback meeting our reversal confirmation trigger (1H RSI >= 32 and positive 1H change) before deploying additional capital."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **87** | 🎯 **43.7%** (38W / 34L / 15BE) | 🔴 **$-0.77 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-04 11:30` | 🟢 BUY | `MSFT` | $7.00 | $545.20 | MSFT is currently the only asset trading above its SMA20 in a confirmed uptrend with stron... |
| `2026-11-02 11:40` | 🔴 SELL (-0.13$) | `AAPL` | $6.87 | $340.69 | AAPL has slipped further into a bearish trend below its SMA20 with a 1-hour RSI of 24.8 an... |
| `2026-10-28 13:21` | 🔴 SELL (-0.02$) | `MSFT` | $6.48 | $528.16 | MSFT has shifted to a bearish trend below its SMA20 and current performance is near our st... |
| `2026-10-26 12:01` | 🟢 BUY | `MSFT` | $6.50 | $530.04 | MSFT is in a confirmed uptrend above its SMA20, and the 1-hour RSI (62.8) and 1-hour perce... |
| `2026-10-23 13:40` | 🟢 BUY | `AAPL` | $7.00 | $347.17 | AAPL is in a confirmed uptrend above its SMA20, satisfying our strict trend filter. The 1-... |

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
