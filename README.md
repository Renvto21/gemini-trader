# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 15:40:47`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.26 USD** | **$34.43 USD** | **$38.69 USD** | 🔴 **-3.28%** ($-1.31) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.38 | $9.89 | 📉 -1.09% | 1d 4h |
| `MSFT` | 0.012146 | $535.17 | $539.53 | $6.55 | 📈 +0.81% | 4h 50m |
| `QQQ` | 0.013791 | $725.09 | $724.18 | $9.99 | 📉 -0.13% | 3h 20m |
| `NVDA` | 0.036812 | $217.32 | $217.19 | $8.00 | 📉 -0.06% | 2h 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado se encuentra en un entorno mixto con presión bajista generalizada en temporalidades diarias, pero con oportunidades de rebote por sobreventa extrema en activos de tecnología como NVDA y QQQ. El efectivo disponible es limitado ($4.26 USD), cumpliendo con la reserva estricta de liquidez. Las posiciones actuales muestran un comportamiento estable: MSFT presenta ganancias moderadas (+0.81%), mientras que AAPL, QQQ y NVDA se mantienen en rangos operativos cercanos a cero o con ligeras pérdidas controladas muy por debajo de los límites de stop-loss."

**Operaciones del ciclo:**
- **[HOLD] MSFT** (Confianza: 80%): MSFT muestra un rendimiento positivo del +0.81% y tendencia alcista sobre su SMA20. Se mantiene la posición para buscar el objetivo de take-profit entre +2.0% y +3.5%.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas (AAPL, MSFT, QQQ, NVDA) respetando estrictamente el stop-loss en -2.0% y buscando un take-profit entre +2.0% y +3.5%. Dado que la liquidez está casi completamente desplegada y la reserva mínima es de $4.26 USD, el enfoque para el siguiente ciclo será buscar una toma de ganancias en MSFT o esperar la confirmación de rebote en NVDA y QQQ para liberar capital y rotar hacia criptomonedas (ETH-USD o SOL-USD) si presentan un nuevo impulso."
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
