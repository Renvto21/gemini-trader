# 🤖 Gemini Autonomous Trader

> **Status:** 🟢 Cloud Active | **Last Updated:** `2026-11-04 09:10:47`

---

### 📊 Portfolio Summary

| Initial Capital | Free Cash | Assets Value | Total Balance | Net Return |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$39.09 USD** | **$0.00 USD** | **$39.09 USD** | 🔴 **-2.26%** ($-0.91) |

---

### 💼 Current Positions

| Asset | Shares | Buy Price | Current Price | Total Value | PnL % | Holding Time |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| *(No open positions - 100% in cash)* | - | - | - | - | - | - |

---

### 🧠 Latest Gemini Market Analysis (Current Cycle)

> "All monitored assets, including equities and cryptocurrencies, are currently trading in a bearish trend below their respective SMA20 lines. Wall Street markets are closed (CERRADO), leaving active liquidity restricted to cryptocurrencies (SOL-USD, ETH-USD, BTC-USD). Although crypto assets show occasional bounce attempts, none satisfy our strict Reversal Confirmation Trigger (rsi_1h >= 32 and change_1h_pct > 0.0 simultaneously while above the SMA20 trend line). Therefore, capital preservation remains paramount."

**Cycle Actions:**
- **[HOLD] SOL-USD** (Confidence: 100%): Asset is currently in a bearish trend below the SMA20 with a negative 1-hour change (-0.6%), failing our strict trend and momentum confirmation rules.

---

### 📝 Operational Memory & Journal (Next Cycles)

> "Maintained defensive cash posture with zero open positions. All assets remain under their SMA20 trend filter, failing the rule of gold. Will continue to monitor crypto assets 24/7 for a verified reversal setup combining a positive 1-hour percentage change and RSI recovery above 32 once the broader trend reclaims the SMA20 line."
---

### 📈 Quantitative Performance & Historical Stats

| Closed Trades | Win Rate | Realized PnL | Best Trade | Worst Trade |
| :---: | :---: | :---: | :---: | :---: |
| **87** | 🎯 **43.7%** (38W / 34L / 15BE) | 🔴 **$-0.77 USD** | 🏆 `+$0.56 (+2.8%) on SOL-USD` | 🛡️ `$-0.97 (-2.5%) on SOL-USD` |
---

### 📜 Recent Trades

| Date | Action | Asset | Amount | Price | Reasoning |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-11-02 11:40` | 🔴 SELL (-0.13$) | `AAPL` | $6.87 | $340.69 | AAPL has slipped further into a bearish trend below its SMA20 with a 1-hour RSI of 24.8 an... |
| `2026-10-28 13:21` | 🔴 SELL (-0.02$) | `MSFT` | $6.48 | $528.16 | MSFT has shifted to a bearish trend below its SMA20 and current performance is near our st... |
| `2026-10-26 12:01` | 🟢 BUY | `MSFT` | $6.50 | $530.04 | MSFT is in a confirmed uptrend above its SMA20, and the 1-hour RSI (62.8) and 1-hour perce... |
| `2026-10-23 13:40` | 🟢 BUY | `AAPL` | $7.00 | $347.17 | AAPL is in a confirmed uptrend above its SMA20, satisfying our strict trend filter. The 1-... |
| `2026-10-22 16:00` | 🔴 SELL (-0.12$) | `MSFT` | $6.88 | $521.40 | MSFT has dropped to a PnL of -1.71%, closely approaching our mandatory stop-loss threshold... |

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
