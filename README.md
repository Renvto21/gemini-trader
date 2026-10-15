# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 10:20:49`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$11.61 USD** | **$26.74 USD** | **$38.35 USD** | 🔴 **-4.12%** ($-1.65) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 23h 30m |
| `BTC-USD` | 0.000061 | $81640.68 | $80315.00 | $4.92 | 📉 -1.62% | 13h 10m |
| `ETH-USD` | 0.002539 | $2362.71 | $2342.29 | $5.95 | 📉 -0.86% | 9h 10m |
| `SOL-USD` | 0.058789 | $102.06 | $101.46 | $5.96 | 📉 -0.59% | 7h 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado accionario se encuentra cerrado con precios congelados, mientras que el mercado de criptomonedas opera 24/7 en una tendencia general bajista bajo la SMA20. Las posiciones actuales se mantienen estables pero con ligeras pérdidas latentes, sin que ninguna haya alcanzado aún el límite crítico de stop-loss estricto de -2.0% o un take-profit positivo, operando en un entorno de cautela en cripto."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 70%): La posición en BTC-USD muestra una pérdida menor (-1.62%) dentro del rango de tolerancia, sin disparar el stop-loss. Se mantiene en espera de un cambio de impulso horario positivo para incrementar o mantener la exposición.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear estrictamente las posiciones abiertas (AAPL, BTC-USD, ETH-USD, SOL-USD). Mantener stop-loss estricto en -2.0% para cortar pérdidas rápidamente si el mercado de criptomonedas profundiza su tendencia bajista. Esperar la apertura de Wall Street para buscar oportunidades de rebote técnico en sobreventa en activos tecnológicos y del S&P 500, rotando capital si es necesario."
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
