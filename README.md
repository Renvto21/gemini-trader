# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 04:20:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$11.61 USD** | **$26.86 USD** | **$38.47 USD** | 🔴 **-3.82%** ($-1.53) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 17h 30m |
| `BTC-USD` | 0.000061 | $81640.68 | $80909.75 | $4.96 | 📉 -0.90% | 7h 10m |
| `ETH-USD` | 0.002539 | $2362.71 | $2360.68 | $5.99 | 📉 -0.09% | 3h 10m |
| `SOL-USD` | 0.058789 | $102.06 | $102.09 | $6.00 | 📈 +0.03% | 1h 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que toda la actividad se concentra exclusivamente en las criptomonedas que operan 24/7. Las cripto principales (ETH, SOL, BTC) muestran un sesgo bajista en el gráfico diario, pero se detectan ligeros intentos de estabilización en el corto plazo con variaciones horarias levemente positivas, aunque sin un momentum claro de rebote explosivo en este ciclo."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 60%): ETH-USD se mantiene estable con una pérdida marginal de -0.09%. A pesar de tener un RSI diario bajo, el RSI de 1h muestra sobreventa pero el precio aún no genera el impulso alcista esperado. Mantenemos la posición esperando un rebote hacia la zona de take-profit.
- **[HOLD] SOL-USD** (Confianza: 60%): SOL-USD opera practicamente plano con un cambio de 1h positivo pero moderado. Se mantiene dentro del plan táctico a la espera de confirmación de volumen comprador para asegurar ganancias rápidas.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales en AAPL, BTC-USD, ETH-USD y SOL-USD ya que ninguna ha alcanzado el stop-loss estricto del -2.0% y se encuentran en rangos de consolidación estrechos. Monitorearemos de cerca el comportamiento de ETH-USD y SOL-USD para capturar ganancias si se produce un repunte del +2.0% al +3.5%, o para recortar pérdidas inmediatamente si rompen soportes a la baja. La liquidez de efectivo se mantiene conservadora a la espera de un catalizador de mayor fuerza en la próxima sesión."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **54** | 🎯 **40.7%** (22W / 18L / 14BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-15 03:20` | 🟢 BUY | `SOL-USD` | $6.00 | $102.06 | SOL-USD muestra un RSI de 1h en 33.3 saliendo de zonas de compresión bajista, acompañado d... |
| `2026-10-15 01:10` | 🟢 BUY | `ETH-USD` | $6.00 | $2362.71 | ETH-USD presenta un RSI de 1h extremadamente bajo en 23.5 saliendo de sobreventa y un camb... |
| `2026-10-14 23:30` | 🔴 SELL (-0.30$) | `SOL-USD` | $9.70 | $101.32 | La posición en SOL-USD acumula una pérdida de -2.95%, acercándose al límite crítico y sin ... |
| `2026-10-14 23:30` | 🔴 SELL (-0.32$) | `ETH-USD` | $9.68 | $2340.86 | 🚨 STOP-LOSS AUTOMÁTICO (CIRCUIT BREAKER): Pérdida de -3.20% superó el límite de seguridad ... |
| `2026-10-14 21:10` | 🟢 BUY | `BTC-USD` | $5.00 | $81640.68 | BTC-USD presenta un RSI de 1h en 24.9 (sobreventa extrema) y liquidez disponible suficient... |

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
