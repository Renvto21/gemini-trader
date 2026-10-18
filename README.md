# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 23:00:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.21 USD** | **$38.26 USD** | 🔴 **-4.35%** ($-1.74) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81566.11 | $10.05 | 📈 +0.49% | 3h 59m |
| `SOL-USD` | 0.097418 | $102.65 | $103.47 | $10.08 | 📈 +0.80% | 3h 50m |
| `ETH-USD` | 0.004193 | $2385.05 | $2405.58 | $10.09 | 📈 +0.86% | 3h 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene operando 24/7 con un sesgo lateral a bajista en el corto plazo, mientras que los mercados tradicionales permanecen cerrados. Las posiciones actuales en BTC-USD, SOL-USD y ETH-USD muestran ganancias moderadas entre +0.49% y +0.86%, manteniéndose estables tras casi 4 horas de holding, pero sin alcanzar aún el objetivo de take-profit óptimo (+2.0% a +3.5%)."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): BTC-USD se encuentra en terreno positivo con una ganancia de +0.49% y un RSI de 1h en 51.8. Se mantiene la posición buscando el objetivo de take-profit entre +2.0% y +3.5%.
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD presenta una ganancia del +0.80% y un comportamiento estable tras casi 4 horas. Continuamos manteniendo la posición esperando un mayor impulso alcista.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD lidera las ganancias del portafolio con +0.86%. Se mantiene la posición activa para capturar el rebote técnico completo hacia el rango objetivo de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas actuales (BTC-USD, SOL-USD, ETH-USD) ya que se encuentran en terreno positivo y el impulso de corto plazo persiste. Monitorear de cerca los niveles de RSI de 1 hora para asegurar beneficios parciales o totales tan pronto como toquen el objetivo de take-profit de +2.0% a +3.5% o crucen a sobrecompra (>70). El stop-loss estricto se mantiene firmemente en -2.0% para proteger el capital. No realizar nuevas compras en este ciclo para preservar la liquidez mínima requerida."
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
