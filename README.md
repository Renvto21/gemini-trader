# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 04:30:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.21 USD** | **$38.26 USD** | 🔴 **-4.36%** ($-1.74) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81608.06 | $10.05 | 📈 +0.54% | 9h 29m |
| `SOL-USD` | 0.097418 | $102.65 | $103.34 | $10.07 | 📈 +0.67% | 9h 19m |
| `ETH-USD` | 0.004193 | $2385.05 | $2406.61 | $10.09 | 📈 +0.90% | 9h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se mantiene abierto y operando en un rango de consolidación alcista tras el rebote inicial. BTC-USD, SOL-USD y ETH-USD muestran ganancias moderadas (entre +0.5% y +0.9%), acercándose a la zona media de sus rangos de 1 hora sin alcanzar todavía los objetivos agresivos de take-profit (+2.0% a +3.5%) ni la sobrecompra extrema (>70). Los mercados tradicionales (QQQ, SPY, NVDA, AAPL, MSFT, GLD) se encuentran cerrados, por lo que toda la atención y liquidez táctica se concentra en mantener las posiciones en cripto y proteger el capital con los stop-loss definidos."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): BTC-USD mantiene una ganancia del 0.54% con un RSI de 1H en 59.4, evolucionando favorablemente hacia el objetivo de take-profit. Se mantiene la posición sin cambios.
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD registra un PnL positivo de +0.67% y un RSI de 1H en 50.0. La posición sigue activa buscando alcanzar el objetivo de take-profit del 2.0% o superior.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD lidera el portafolio con un PnL de +0.9% y un RSI de 1H en 49.0. Se mantiene la posición activa respetando el plan táctico de momentum.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en BTC-USD, SOL-USD y ETH-USD dado que continúan con rendimientos positivos y un holding time de aproximadamente 9.5 horas. El plan táctico es vigilar de cerca la evolución del RSI de 1 hora hacia el objetivo de take-profit de +2.0% a +3.5% o salida por sobrecompra (>70). El stop-loss estricto a -2.0% sigue operando como salvaguarda. La liquidez en efectivo se mantiene en reserva mínima ($8.05 USD), por lo que no se abrirán nuevas posiciones en este ciclo hasta realizar tomas de beneficios o detectar una señal de alta convicción."
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
