# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 06:00:49`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$11.61 USD** | **$26.98 USD** | **$38.59 USD** | 🔴 **-3.52%** ($-1.41) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 19h 10m |
| `BTC-USD` | 0.000061 | $81640.68 | $81284.08 | $4.98 | 📉 -0.44% | 8h 50m |
| `ETH-USD` | 0.002539 | $2362.71 | $2372.56 | $6.03 | 📈 +0.42% | 4h 50m |
| `SOL-USD` | 0.058789 | $102.06 | $103.26 | $6.07 | 📈 +1.18% | 2h 40m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado accionario tradicional (Wall Street) se encuentra actualmente CERRADO, por lo que la operativa se concentra exclusivamente en el mercado de criptomonedas (24/7). Las criptomonedas principales como SOL-USD y ETH-USD muestran signos tempranos de estabilización tras sesiones bajistas, mientras que BTC-USD mantiene una consolidación lateral con sesgo bajista macro. El portafolio mantiene una exposición equilibrada con pequeñas ganancias en SOL y ETH, y ligeras pérdidas controladas en AAPL y BTC."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición en SOL-USD muestra un rendimiento positivo de +1.18% acercándose al objetivo de take-profit. Se mantiene la posición a la espera de que el RSI de 1h se acerque a zonas de sobrecompra para asegurar beneficios.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear de cerca el comportamiento de SOL-USD y ETH-USD para asegurar ganancias parciales o totales si alcanzan el rango objetivo de +2.0% a +3.5%. Vigilar el estricto stop-loss en -2.0% para AAPL y BTC-USD. Mantener la reserva mínima de efectivo de $4.00 y esperar la apertura de Wall Street para reevaluar posiciones en renta variable si el momentum técnico mejora."
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
