# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 01:30:49`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$14.17 USD** | **$24.59 USD** | **$38.76 USD** | 🔴 **-3.11%** ($-1.24) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $539.44 | $6.55 | 📈 +0.80% | 14h 40m |
| `QQQ` | 0.013791 | $725.09 | $728.00 | $10.04 | 📈 +0.40% | 13h 10m |
| `NVDA` | 0.036812 | $217.32 | $217.23 | $8.00 | 📉 -0.04% | 12h 40m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de Wall Street se encuentra cerrado actualmente con precios congelados, por lo que las acciones tecnológicas en cartera (MSFT, QQQ, NVDA) no operan en este ciclo. En el frente cripto, que opera 24/7, ETH-USD muestra un RSI diario de sobreventa profunda (29.4) y un RSI de 1h elevado (68.4), mientras que SOL-USD mantiene un RSI diario de 26.9. Dado que la liquidez está mayormente comprometida en posiciones accionarias en espera de apertura y contamos con $14.17 en efectivo, mantendremos la disciplina y el monitoreo de los activos abiertos sin forzar entradas en cripto hasta ver una corrección más nítida."

**Operaciones del ciclo:**
- **[HOLD] MSFT** (Confianza: 80%): La posición en MSFT muestra un rendimiento positivo de +0.8% pero el mercado está cerrado. Se mantiene para buscar el objetivo de take-profit entre +2.0% y +3.5% en la próxima sesión.
- **[HOLD] QQQ** (Confianza: 80%): QQQ se encuentra con mercado cerrado y un PnL de +0.4%. Esperamos la apertura para evaluar la continuación del rebote técnico y asegurar ganancias si alcanza el rango objetivo.
- **[HOLD] NVDA** (Confianza: 75%): NVDA está prácticamente plano (-0.04%) con mercado cerrado. Mantenemos la posición vigilando el stop-loss estricto del -2.0% y esperando la apertura para evaluar su momentum.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener posiciones actuales en MSFT, QQQ y NVDA hasta la apertura del mercado bursátil para buscar take-profit rápido en el rango de +2.0% a +3.5%. Conservar la liquidez actual de $14.17 USD en efectivo. Vigilar de cerca ETH-USD y SOL-USD para una corrección intradiaria con RSI de 1h por debajo de 35 que permita una entrada táctica de alta convicción."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **58** | 🎯 **41.4%** (24W / 20L / 14BE) | 🔴 **$-1.22 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-15 16:20` | 🔴 SELL (-0.10$) | `AAPL` | $9.90 | $342.86 | AAPL lleva más de un día abierta (1d 5h) sin mostrar un momentum significativo ni alcanzar... |
| `2026-10-15 12:50` | 🟢 BUY | `NVDA` | $8.00 | $217.32 | NVDA presenta un RSI de 1h en sobreventa extrema (21.5) con un inicio de recuperación en s... |
| `2026-10-15 12:20` | 🟢 BUY | `QQQ` | $10.00 | $725.09 | QQQ muestra un RSI de 1h en sobreventa extrema (28.7) cruzando al alza con un cambio posit... |
| `2026-10-15 12:10` | 🔴 SELL (+0.14$) | `ETH-USD` | $6.14 | $2417.73 | ETH-USD ha alcanzado un rendimiento del +2.33%, cumpliendo con el rango establecido para l... |
| `2026-10-15 11:50` | 🔴 SELL (+0.13$) | `SOL-USD` | $6.13 | $104.21 | SOL-USD ha alcanzado un rendimiento de +2.11%, cumpliendo con la regla de toma rápida de g... |

---

<details>
<summary>⚙️ Ver configuración técnica y comandos locales</summary>

### Comandos disponibles
* **Ver estado actual:** `python main.py --status`
* **Ejecutar 1 ciclo de prueba:** `python main.py --run-once`
* **Ejecutar en bucle local:** `python main.py --loop --interval 300`

### Módulos del sistema
* `main.py`: Orquestador principal del bot.
* `dashboard.py`: Generador del panel dinámico en README.
* `agent.py`: Conexión con Gemini Flash y reglas de riesgo.
* `portfolio.py`: Registro de operaciones, cálculo de saldo y PnL.
* `market_data.py`: Descarga y cálculo técnico con yfinance.
* `portfolio.json`: Base de datos de posiciones.
</details>
