# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 00:50:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.44 USD** | **$38.48 USD** | 🔴 **-3.79%** ($-1.52) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81893.65 | $10.09 | 📈 +0.89% | 5h 49m |
| `SOL-USD` | 0.097418 | $102.65 | $104.56 | $10.19 | 📈 +1.86% | 5h 39m |
| `ETH-USD` | 0.004193 | $2385.05 | $2423.48 | $10.16 | 📈 +1.61% | 5h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se mantiene abierto 24/7 y muestra un rebote moderado tras las caídas semanales previas. Las posiciones actuales en BTC-USD, SOL-USD y ETH-USD muestran rendimientos positivos de +0.89%, +1.86% y +1.61% respectivamente, acercándose a la zona objetivo de take-profit. Los mercados tradicionales están cerrados, por lo que toda la atención se centra en la gestión de estas criptomonedas."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD se encuentra con un rendimiento positivo de +1.86% y un RSI de 1H en 55.1, muy cerca de la zona de take-profit (+2.0% a +3.5%). Se mantiene la posición a la espera de que el impulso continúe para asegurar ganancias óptimas.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD registra una ganancia del +1.61% con un RSI de 1H en 51.2. El rebote técnico se está desarrollando según lo planeado, por lo que se mantiene la posición para buscar el objetivo de ganancia en el próximo ciclo.
- **[HOLD] BTC-USD** (Confianza: 75%): BTC-USD muestra una ganancia de +0.89% con un RSI de 1H en 61.9. Aunque va más retrasado que las altcoins en este tramo, el momentum sigue siendo favorable y se mantiene para permitir que alcance el objetivo de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener posiciones activas en BTC-USD, SOL-USD y ETH-USD ya que se encuentran cerca de la zona de toma de beneficios (+2.0% a +3.5%). Monitorear de cerca el RSI de 1H y el porcentaje de ganancia en el siguiente ciclo para ejecutar un SELL parcial o total si alcanzan el umbral de take-profit, liberando liquidez hacia efectivo."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **67** | 🎯 **38.8%** (26W / 27L / 14BE) | 🔴 **$-1.84 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-17 19:10` | 🟢 BUY | `ETH-USD` | $10.00 | $2385.05 | ETH-USD muestra un RSI de 1H en 29.0 (sobreventa profunda) combinado con un cambio de 1h p... |
| `2026-10-17 19:10` | 🟢 BUY | `SOL-USD` | $10.00 | $102.65 | SOL-USD presenta un RSI de 1H en 31.5 saliendo de zona de sobreventa estricta y un cambio ... |
| `2026-10-17 19:00` | 🟢 BUY | `BTC-USD` | $10.00 | $81170.65 | BTC-USD muestra un RSI de 1H saliendo de niveles bajos (37.5) con un cambio positivo de 0.... |
| `2026-10-17 18:40` | 🔴 SELL (-0.22$) | `ETH-USD` | $9.78 | $2370.09 | La posición acumula una pérdida de -2.21%, excediendo el umbral de stop-loss del -2.0%. El... |
| `2026-10-17 18:40` | 🔴 SELL (-0.21$) | `SOL-USD` | $9.79 | $101.78 | La posición ha alcanzado una pérdida de -2.08%, rompiendo el límite de stop-loss estricto ... |

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
