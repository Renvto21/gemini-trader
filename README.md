# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 14:30:56`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.31 USD** | **$19.91 USD** | **$39.22 USD** | 🔴 **-1.95%** ($-0.78) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.31 | $9.89 | 📉 -1.11% | 3h 40m |
| `SOL-USD` | 0.095511 | $104.70 | $104.96 | $10.02 | 📈 +0.25% | 2h 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general se encuentra bajo presión bajista con la mayoría de los activos cotizando por debajo de su SMA20, aunque se observan niveles de sobreventa extrema en marcos temporales de 1 hora en varios índices y criptomonedas. Las posiciones actuales se mantienen estables pero sin un momentum agresivo claro; AAPL muestra un leve retroceso (-1.11%) pero mantiene su tendencia alcista diaria, mientras que SOL-USD se mantiene lateral con un mínimo beneficio (+0.25%)."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 75%): AAPL lleva abierto menos de 4 horas con una pérdida leve de -1.11%, manteniéndose dentro del rango operativo normal y por encima de su soporte diario. Se mantiene la posición vigilando el stop-loss.
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD muestra un comportamiento neutral-positivo con un PnL de +0.25% y un RSI de 1h en 30.7. Se mantiene a la espera de que el momentum alcista se consolide para buscar el objetivo de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear de cerca AAPL y SOL-USD. Mantener stop-loss estricto a -2.0% y take-profit entre +2.0% y +3.5%. Para el siguiente ciclo, esperar a que ETH-USD o BTC-USD muestren un cruce de RSI de 1h por encima de 35 con cambio porcentual positivo para buscar una nueva oportunidad de rebote, manteniendo la liquidez de efectivo protegida."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **51** | 🎯 **43.1%** (22W / 15L / 14BE) | 🔴 **$-0.59 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-14 12:30` | 🟢 BUY | `SOL-USD` | $10.00 | $104.70 | SOL-USD presenta un RSI de 1h en 29.2 saliendo de sobreventa extrema y un cambio de 1h pos... |
| `2026-10-14 11:20` | 🔴 SELL (-0.09$) | `BTC-USD` | $5.89 | $81874.95 | BTC-USD lleva más de 14 horas abierto con un PnL negativo persistente (-1.51%) y un RSI de... |
| `2026-10-14 10:50` | 🟢 BUY | `AAPL` | $10.00 | $346.15 | AAPL se encuentra con un excelente momentum alcista intradiario, un incremento de 1.4% en ... |
| `2026-10-14 10:10` | 🔴 SELL (-0.11$) | `SOL-USD` | $5.89 | $105.41 | La posición en SOL-USD acumula una pérdida cercana al -1.9%, rozando nuestro stop-loss est... |
| `2026-10-14 02:50` | 🔴 SELL (-0.01$) | `ETH-USD` | $4.99 | $2502.14 | ETH-USD lleva más de 9 horas de holding con PnL plano (-0.25%) y un RSI de 1H en 42.3 sin ... |

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
