# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 08:50:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$11.61 USD** | **$26.88 USD** | **$38.49 USD** | 🔴 **-3.77%** ($-1.51) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 22h 0m |
| `BTC-USD` | 0.000061 | $81640.68 | $80956.41 | $4.96 | 📉 -0.84% | 11h 40m |
| `ETH-USD` | 0.002539 | $2362.71 | $2363.12 | $6.00 | 📈 +0.02% | 7h 40m |
| `SOL-USD` | 0.058789 | $102.06 | $102.30 | $6.01 | 📈 +0.24% | 5h 30m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional (acciones y ETFs) se encuentra cerrado, por lo que toda la actividad se concentra exclusivamente en las criptomonedas (BTC, ETH, SOL), que operan 24/7. Las criptomonedas muestran signos de consolidación tras caídas recientes, con SOL y ETH manteniendo ligeros beneficios o estables desde nuestras entradas recientes, mientras que BTC se mantiene estable pero con baja volatilidad a corto plazo. Mantenemos la cautela y la disciplina de gestión de riesgo, esperando señales más claras de impulso en el RSI de 1h antes de escalar posiciones, y protegiendo nuestras posiciones actuales de acuerdo con las reglas estrictas de stop-loss."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 75%): La posición se encuentra estable con una ligera ganancia del 0.02% tras su apertura reciente. El RSI de 1h se sitúa en 34.1, recuperándose de niveles de sobreventa previos. Esperamos la confirmación de un mayor impulso alcista para buscar take-profit entre +2.0% y +3.5%.
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD muestra un rendimiento positivo del 0.24% con un RSI de 1h en 37.1. Se mantiene dentro del plan táctico de rebote técnico, por lo que conservamos la posición mientras no rompa el soporte a la baja.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en ETH-USD, SOL-USD, BTC-USD y AAPL (esta última en mercado cerrado). Monitorear de cerca el RSI de 1h para ETH y SOL: si alcanzan la zona de sobrecompra (>70) o logran un rendimiento entre +2.0% y +3.5%, proceder a asegurar beneficios parciales o totales para incrementar la liquidez. Mantener el stop-loss estricto en -2.0% para todas las posiciones abiertas y preservar la liquidez mínima operativa."
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
