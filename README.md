# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 03:20:35`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.22 USD** | **$38.27 USD** | 🔴 **-4.33%** ($-1.73) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81592.40 | $10.05 | 📈 +0.52% | 8h 19m |
| `SOL-USD` | 0.097418 | $102.65 | $103.41 | $10.07 | 📈 +0.74% | 8h 9m |
| `ETH-USD` | 0.004193 | $2385.05 | $2407.66 | $10.09 | 📈 +0.95% | 8h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que la actividad se concentra 100% en las criptomonedas (BTC-USD, SOL-USD y ETH-USD). Las posiciones actuales muestran ganancias moderadas (entre +0.52% y +0.95%), acercándose gradualmente a la zona objetivo pero sin alcanzar aún el take-profit óptimo del +2.0% al +3.5%. Los indicadores de 1 hora se mantienen estables y sin señales inmediatas de reversión bajista o sobrecompra extrema (RSI 1H entre 52 y 61)."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): La posición en BTC-USD muestra un rendimiento positivo de +0.52% tras más de 8 horas de holding. El RSI de 1H en 61.4 indica que el precio mantiene estabilidad sin señales de sobrecompra ni pérdida de impulso que justifiquen una salida anticipada. Se mantiene el plan de retención buscando el objetivo de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en BTC-USD, SOL-USD y ETH-USD durante este ciclo ya que se encuentran en terreno positivo y operando dentro de los márgenes normales de riesgo. Monitorear de cerca el RSI de 1 hora y el avance de precios: si alguno de los activos alcanza el objetivo de ganancia de +2.0% a +3.5% o cruza a sobrecompra (>70), ejecutaré la venta inmediata para asegurar liquidez. El efectivo disponible se mantendrá reservado a la espera de una mayor divergencia o volatilidad que active nuevas entradas agresivas."
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
