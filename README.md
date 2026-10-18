# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 04:10:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.26 USD** | **$38.30 USD** | 🔴 **-4.24%** ($-1.70) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81651.25 | $10.06 | 📈 +0.59% | 9h 9m |
| `SOL-USD` | 0.097418 | $102.65 | $103.60 | $10.09 | 📈 +0.93% | 9h 0m |
| `ETH-USD` | 0.004193 | $2385.05 | $2409.92 | $10.10 | 📈 +1.04% | 9h 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado por lo que la operativa se concentra exclusivamente en el mercado de criptomonedas abierto 24/7. Las posiciones actuales en BTC-USD, SOL-USD y ETH-USD muestran ligeras ganancias acumuladas tras casi 9 horas abiertas, situándose en rangos de +0.59% a +1.04%. Los indicadores de 1 hora se mantienen estables pero sin alcanzar aún la zona de sobrecompra (>70) óptima para una toma de beneficios completa según la estrategia de take-profit establecida entre +2.0% y +3.5%."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 75%): La posición acumula una ganancia moderada de +0.59% tras 9 horas. El RSI de 1H está en 60.4, acercándose gradualmente a la zona de sobrecompra sin señales de debilidad. Mantenemos la posición a la espera del objetivo de take-profit entre +2.0% y +3.5%.
- **[HOLD] SOL-USD** (Confianza: 75%): La posición muestra un rendimiento positivo de +0.93%. El RSI de 1H se sitúa en 52.3 con un comportamiento técnico estable. Se mantiene para buscar la expansión del movimiento alcista hacia el objetivo de take-profit.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD lidera las ganancias actuales con un +1.04%. El RSI de 1H se ubica en 50.5 y el precio se mantiene firme sobre los niveles de entrada. Continuamos reteniendo la posición para asegurar beneficios en el rango óptimo establecido.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en BTC-USD, SOL-USD y ETH-USD mientras continúan su camino hacia el objetivo de take-profit entre +2.0% y +3.5% o hasta que el RSI de 1 hora alcance la zona de sobrecompra (>70). El stop-loss estricto a -2.0% se mantiene activo para proteger la cuenta. No se realizarán nuevas compras en este ciclo para preservar la liquidez actual y permitir que el capital desplegado madure."
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
