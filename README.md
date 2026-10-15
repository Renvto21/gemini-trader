# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 13:20:49`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.26 USD** | **$34.44 USD** | **$38.70 USD** | 🔴 **-3.26%** ($-1.30) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $343.55 | $9.92 | 📉 -0.75% | 1d 2h |
| `MSFT` | 0.012146 | $535.17 | $539.71 | $6.56 | 📈 +0.85% | 2h 30m |
| `QQQ` | 0.013791 | $725.09 | $723.69 | $9.98 | 📉 -0.19% | 1h 0m |
| `NVDA` | 0.036812 | $217.32 | $216.65 | $7.98 | 📉 -0.31% | 30m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sentimiento mixto con sesgo bajista en varios índices y acciones tecnológicas de gran capitalización bajo sus SMA20, aunque se aprecian condiciones severas de sobreventa intradiaria en activos clave como QQQ (rsi_1h en 21.0) y NVDA (rsi_1h en 18.7). La liquidez disponible es baja ($4.26 USD), lo que limita la capacidad de apertura de nuevas posiciones sin realizar rotaciones previas. Las criptomonedas se mantienen operativas 24/7 con movimientos moderados."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 60%): AAPL se mantiene dentro de un rango operativo aceptable pero sin momentum claro. Dado el tiempo abierto prolongado, se mantiene temporalmente en cartera a la espera de un repunte, preparando su posible venta para rotación si persiste estancada.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener la vigilancia estricta sobre las posiciones actuales. AAPL lleva más de 1 día abierta con un rendimiento lateral leve (-0.75%), por lo que se evaluará su rotación en el siguiente ciclo si no muestra tracción alcista para liberar capital hacia rebotes más agresivos. Monitorear MSFT para asegurar ganancias si se acerca al objetivo de +2.0%. Controlar estrictamente el stop-loss en -2.0% para proteger el capital."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **57** | 🎯 **42.1%** (24W / 19L / 14BE) | 🔴 **$-1.12 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-15 12:50` | 🟢 BUY | `NVDA` | $8.00 | $217.32 | NVDA presenta un RSI de 1h en sobreventa extrema (21.5) con un inicio de recuperación en s... |
| `2026-10-15 12:20` | 🟢 BUY | `QQQ` | $10.00 | $725.09 | QQQ muestra un RSI de 1h en sobreventa extrema (28.7) cruzando al alza con un cambio posit... |
| `2026-10-15 12:10` | 🔴 SELL (+0.14$) | `ETH-USD` | $6.14 | $2417.73 | ETH-USD ha alcanzado un rendimiento del +2.33%, cumpliendo con el rango establecido para l... |
| `2026-10-15 11:50` | 🔴 SELL (+0.13$) | `SOL-USD` | $6.13 | $104.21 | SOL-USD ha alcanzado un rendimiento de +2.11%, cumpliendo con la regla de toma rápida de g... |
| `2026-10-15 10:50` | 🟢 BUY | `MSFT` | $6.50 | $535.17 | MSFT presenta un RSI de 1h ultra comprimido en sobreventa extrema (14.7) con un cambio pos... |

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
