# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 13:31:13`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.96 USD** | **$39.08 USD** | 🔴 **-2.30%** ($-0.92) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $340.70 | $10.00 | 📈 +0.02% | 1h 29m |
| `GLD` | 0.026337 | $379.70 | $378.01 | $9.96 | 📉 -0.45% | 1h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un comportamiento lateral con sesgo bajista en la mayoría de los índices principales, mientras que los activos de criptomonedas y materias primas mantienen una consolidación tranquila. AAPL se mantiene estable sobre su tendencia alcista diaria, mientras que GLD registra un RSI de 1 hora extremadamente bajo (30.5), bordeando la zona crítica de soporte donde esperamos el rebote técnico."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 70%): La posición lleva poco más de una hora abierta con una ganancia marginal del +0.02%. Mantiene una tendencia diaria alcista sólida y un RSI de 1 hora neutral en 39.3, por lo que esperamos que desarrolle mayor impulso sin necesidad de rotar el capital todavía.
- **[HOLD] GLD** (Confianza: 75%): GLD presenta un RSI de 1 hora en 30.5, muy cerca del nivel de sobreventa extrema que buscamos para cazar rebotes de reversión a la media. Mantendremos la posición para permitir que el precio reaccione al soporte actual, vigilando estrictamente el stop-loss en caso de caída.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos nuestras posiciones abiertas en AAPL y GLD ya que ninguna ha alcanzado los umbrales de stop-loss (-2.0%) o take-profit (+2.0% a +3.5%). El RSI de GLD en 30.5 sugiere que la presión vendedora podría estar agotándose; vigilaremos de cerca la siguiente hora para confirmar el rebote o proceder al cierre si perfora soportes."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **81** | 🎯 **44.4%** (36W / 30L / 15BE) | 🔴 **$-0.74 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-20 12:01` | 🟢 BUY | `GLD` | $10.00 | $379.70 | GLD presenta un RSI de 1 hora en 31.4, acercándose a la zona ideal de sobreventa para acti... |
| `2026-10-20 12:01` | 🟢 BUY | `AAPL` | $10.00 | $340.64 | AAPL se encuentra en tendencia alcista diaria con un RSI de 1 hora en 33.1 (cercano a sobr... |
| `2026-10-20 11:10` | 🔴 SELL (+0.12$) | `BTC-USD` | $8.69 | $82949.93 | BTC-USD muestra un RSI de 1 hora en 72.2 (sobrecompra) y un rendimiento positivo de +1.45%... |
| `2026-10-20 11:10` | 🔴 SELL (+0.28$) | `SOL-USD` | $10.28 | $107.08 | SOL-USD registra un excelente rendimiento de +2.83% con un RSI de 1 hora en sobrecompra (7... |
| `2026-10-20 11:10` | 🔴 SELL (+0.23$) | `ETH-USD` | $10.23 | $2449.11 | ETH-USD ha alcanzado un PnL de +2.32% y su RSI de 1 hora ha tocado el nivel de sobrecompra... |

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
