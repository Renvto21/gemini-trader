# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 02:10:51`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$17.61 USD** | **$20.90 USD** | **$38.51 USD** | 🔴 **-3.73%** ($-1.49) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 15h 20m |
| `BTC-USD` | 0.000061 | $81640.68 | $81238.83 | $4.98 | 📉 -0.49% | 5h 0m |
| `ETH-USD` | 0.002539 | $2362.71 | $2367.86 | $6.01 | 📈 +0.22% | 1h 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se mantiene abierto operando en un entorno de cautela con tendencia bajista general, mientras que los mercados tradicionales (Wall Street) permanecen cerrados. ETH-USD muestra ligeras señales de consolidación tras el rebote reciente, pero su RSI de 1h se encuentra en 31.0, cerca de la zona de sobreventa, manteniendo una perspectiva frágil. AAPL y BTC-USD muestran variaciones mínimas con pérdidas no realizadas controladas dentro de los rangos permitidos."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 60%): ETH-USD mantiene una pequeña ganancia del +0.22% tras la entrada reciente por rebote. El RSI de 1h está en 31.0 y el cambio de 1h es ligeramente negativo (-0.54%). Mantendremos la posición esperando un impulso mayor hacia el rango objetivo de take-profit del +2.0% al +3.5%, vigilando que no rompa soportes a la baja.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en AAPL, BTC-USD y ETH-USD mientras el mercado tradicional esté cerrado. Vigilar estrictamente ETH-USD para asegurar ganancias si alcanza el objetivo de +2.0% a +3.5% o si el RSI de 1h supera 70. Mantener el stop-loss estricto en -2.0% para AAPL y BTC-USD. No abrir nuevas posiciones en cripto hasta ver una confirmación alcista más clara con un RSI de 1h saliendo firmemente de la zona baja."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **54** | 🎯 **40.7%** (22W / 18L / 14BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-15 01:10` | 🟢 BUY | `ETH-USD` | $6.00 | $2362.71 | ETH-USD presenta un RSI de 1h extremadamente bajo en 23.5 saliendo de sobreventa y un camb... |
| `2026-10-14 23:30` | 🔴 SELL (-0.30$) | `SOL-USD` | $9.70 | $101.32 | La posición en SOL-USD acumula una pérdida de -2.95%, acercándose al límite crítico y sin ... |
| `2026-10-14 23:30` | 🔴 SELL (-0.32$) | `ETH-USD` | $9.68 | $2340.86 | 🚨 STOP-LOSS AUTOMÁTICO (CIRCUIT BREAKER): Pérdida de -3.20% superó el límite de seguridad ... |
| `2026-10-14 21:10` | 🟢 BUY | `BTC-USD` | $5.00 | $81640.68 | BTC-USD presenta un RSI de 1h en 24.9 (sobreventa extrema) y liquidez disponible suficient... |
| `2026-10-14 19:00` | 🟢 BUY | `ETH-USD` | $10.00 | $2418.34 | ETH-USD presenta un RSI de 1h en 22.0 (sobreventa extrema) y un cambio de 1h que comienza ... |

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
