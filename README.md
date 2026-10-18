# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 07:00:50`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.35 USD** | **$38.40 USD** | 🔴 **-4.00%** ($-1.60) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $82012.28 | $10.10 | 📈 +1.04% | 12h 0m |
| `SOL-USD` | 0.097418 | $102.65 | $103.71 | $10.10 | 📈 +1.03% | 11h 50m |
| `ETH-USD` | 0.004193 | $2385.05 | $2420.23 | $10.15 | 📈 +1.48% | 11h 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de Wall Street se encuentra cerrado, por lo que la liquidez y operativa se concentran exclusivamente en el mercado de criptomonedas (ABIERTO 24/7). Las posiciones actuales en BTC-USD, SOL-USD y ETH-USD muestran ganancias moderadas entre 1.03% y 1.48%, acercándose al rango objetivo de take-profit sin alcanzar todavía la zona de sobrecompra estricta en RSI de 1H (>70). Se mantiene la disciplina operativa a la espera de mayores impulsos."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): La posición muestra un rendimiento positivo de +1.04% tras 12 horas abierto. El RSI de 1H se sitúa en 61.6, manteniéndose en una trayectoria saludable hacia el objetivo de take-profit (+2.0% a +3.5%) sin señales de reversión bajista inmediata.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD registra una ganancia actual de +1.48%, liderando el portafolio en este ciclo. El precio se mantiene firme y el RSI de 1H se encuentra en 50.7, por lo que se mantiene la posición buscando el objetivo de take-profit.
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD presenta un rendimiento positivo de +1.03% tras casi 12 horas de retención. Mantiene estructura técnica estable y se espera que continúe su avance hacia la zona de recogida de beneficios.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear de cerca las posiciones abiertas en BTC-USD, SOL-USD y ETH-USD para asegurar beneficios en cuanto alcancen una rentabilidad entre +2.0% y +3.5% o crucen un RSI de 1H superior a 70. Mantener el stop-loss estricto en -2.0% y la reserva mínima de efectivo de $4.05 USD. No realizar nuevas compras este ciclo dado que la liquidez restante está por debajo del tamaño operativo mínimo y las posiciones actuales están consolidando sus rebotes."
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
