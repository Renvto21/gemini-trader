# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 07:20:38`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.39 USD** | **$38.43 USD** | 🔴 **-3.92%** ($-1.57) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $82060.38 | $10.11 | 📈 +1.10% | 12h 19m |
| `SOL-USD` | 0.097418 | $102.65 | $104.02 | $10.13 | 📈 +1.33% | 12h 9m |
| `ETH-USD` | 0.004193 | $2385.05 | $2419.36 | $10.14 | 📈 +1.44% | 12h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se mantiene abierto y operando con estabilidad moderada. Las posiciones actuales en BTC-USD, SOL-USD y ETH-USD muestran rendimientos positivos acumulados entre +1.1% y +1.44%, acercándose de manera gradual a la zona objetivo de take-profit (+2.0% a +3.5%). Los activos tradicionales como acciones y ETFs se encuentran cerrados por el fin de semana, por lo que toda la atención táctica se concentra en la gestión del riesgo y la captura de beneficios en los criptoactivos."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): BTC-USD presenta una ganancia actual de +1.1% tras 12 horas de retención. El RSI de 1H se sitúa en 62.7 y el precio muestra estabilidad. Se mantiene la posición a la espera de alcanzar el rango de take-profit (+2.0% a +3.5%).
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD registra un rendimiento positivo de +1.33% con un holding time de más de 12 horas. El movimiento alcista continúa su curso hacia la meta de beneficios establecida sin tocar los niveles de stop-loss.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD lidera el portafolio con una ganancia de +1.44%. El comportamiento del precio sigue la tesis de rebote técnico inicial, por lo que se mantiene la posición para capturar la totalidad del movimiento esperado.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Las posiciones abiertas en BTC-USD, SOL-USD y ETH-USD están madurando adecuadamente. Mantendré las posiciones vigentes hasta que alcancen la zona de take-profit entre +2.0% y +3.5%, o hasta que el indicador RSI de 1H muestre signos claros de sobrecompra (>70). Monitorearé la evolución del precio para asegurar utilidades y mantener el efectivo disponible por encima de la reserva mínima."
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
