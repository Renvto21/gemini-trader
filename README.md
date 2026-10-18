# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 02:00:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.28 USD** | **$38.32 USD** | 🔴 **-4.20%** ($-1.68) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81681.98 | $10.06 | 📈 +0.63% | 6h 59m |
| `SOL-USD` | 0.097418 | $102.65 | $103.66 | $10.10 | 📈 +0.98% | 6h 50m |
| `ETH-USD` | 0.004193 | $2385.05 | $2412.15 | $10.11 | 📈 +1.14% | 6h 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que toda la actividad se concentra en el sector de criptomonedas que opera 24/7. Las posiciones actuales en BTC-USD, SOL-USD y ETH-USD muestran ganancias moderadas pero el momentum de 1 hora se está estabilizando o desacelerando ligeramente (con RSI 1H alrededor de 51-61), acercándose a los objetivos de take-profit sin alcanzarlos plenamente. Mantenemos la vigilancia estricta ante posibles reversiones."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 75%): La posición en BTC-USD registra una ganancia del 0.63% tras casi 7 horas. El RSI 1H se encuentra en 61.4 y el precio se mantiene estable. Mantenemos la posición a la espera de alcanzar el objetivo de take-profit de +2.0% a +3.5%.
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD muestra una ganancia del 0.98% con un RSI 1H en 51.3. El rebote técnico sigue su curso de manera controlada, por lo que conservamos la posición para buscar una mayor valorización antes de tomar beneficios.
- **[HOLD] ETH-USD** (Confianza: 78%): ETH-USD lidera las ganancias con un 1.14% y un RSI 1H en 52.0. Continuamos dentro de la operación protegiendo la ganancia y listos para ejecutar venta total o parcial si el precio acelera hacia el rango de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales (BTC-USD, SOL-USD, ETH-USD) buscando alcanzar la zona objetivo de take-profit entre +2.0% y +3.5%. Si el RSI 1H supera los 70 o las ganancias alcanzan el objetivo, procederemos a vender para asegurar liquidez. Los stop-loss se mantienen estrictos por debajo de -2.0% para proteger el capital."
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
