# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 04:30:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$11.61 USD** | **$26.89 USD** | **$38.50 USD** | 🔴 **-3.74%** ($-1.50) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 17h 40m |
| `BTC-USD` | 0.000061 | $81640.68 | $81072.31 | $4.97 | 📉 -0.70% | 7h 20m |
| `ETH-USD` | 0.002539 | $2362.71 | $2366.08 | $6.01 | 📈 +0.14% | 3h 20m |
| `SOL-USD` | 0.058789 | $102.06 | $102.22 | $6.01 | 📈 +0.16% | 1h 10m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado bursátil de Wall Street se encuentra CERRADO, manteniendo congelados los precios de los activos tradicionales. Por lo tanto, toda la actividad táctica se concentra en las criptomonedas (SOL-USD, BTC-USD y ETH-USD) que operan 24/7. Las criptomonedas muestran ligeros intentos de recuperación en el corto plazo con cambios positivos de 1h y RSI saliendo de zonas de compresión bajista, aunque el contexto diario sigue bajo las medias móviles principales. Mantenemos una postura defensiva pero activa, protegiendo las posiciones abiertas y vigilando de cerca los niveles de take-profit y stop-loss."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra un cambio de 1h positivo del 0.51% y un RSI de 1h en 31.0 recuperándose desde niveles de sobreventa extrema. Se mantiene la posición abierta para capturar el rebote técnico hacia la zona objetivo de take-profit (+2.0% a +3.5%), sin haber alcanzado el límite de stop-loss.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en AAPL, BTC-USD, ETH-USD y SOL-USD ya que respetan los márgenes de stop-loss estricto (-2.0%). Dado que Wall Street está cerrado, la liquidez actual de $11.61 USD se mantendrá en reserva para buscar oportunidades de alto impulso en cripto si se presentan rupturas claras de resistencia o para recortar pérdidas inmediatamente si el mercado cripto revierte a la baja. Monitorear el take-profit en ETH y SOL si alcanzan ganancias entre +2.0% y +3.5%."
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
