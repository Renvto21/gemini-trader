# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 22:00:49`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.17 USD** | **$38.21 USD** | 🔴 **-4.47%** ($-1.79) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81427.33 | $10.03 | 📈 +0.32% | 3h 0m |
| `SOL-USD` | 0.097418 | $102.65 | $103.29 | $10.06 | 📈 +0.62% | 2h 50m |
| `ETH-USD` | 0.004193 | $2385.05 | $2402.29 | $10.07 | 📈 +0.72% | 2h 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que la operativa se concentra 100% en las criptomonedas (BTC-USD, ETH-USD y SOL-USD). Las posiciones actuales muestran ganancias ligeras entre +0.32% y +0.72%, manteniéndose estables tras casi tres horas de holding, aunque el RSI de 1H en cripto se ha contraído ligeramente sin romper soportes. El momentum de corto plazo es lateral-bajista, por lo que optamos por mantener las posiciones actuales a la espera de un nuevo impulso que active nuestros objetivos de take-profit entre +2.0% y +3.5%."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 75%): BTC-USD se mantiene estable con una pequeña ganancia del 0.32%. Mantenemos la posición mientras el precio respete el soporte actual y no se alcance el objetivo de take-profit.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra una ganancia del 0.72% con un RSI de 1H en 30.7. Mantenemos la posición buscando que el rebote continúe hacia el rango de take-profit.
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD registra un beneficio del 0.62%. Continuamos operando el rebote técnico a la espera de una aceleración en el precio o la llegada a la zona de toma de ganancias.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en BTC-USD, SOL-USD y ETH-USD. Vigilar que el RSI de 1H no rompa a la baja y aplicar stop-loss estricto si alguna posición cae al umbral de -2.0%. Mantener la orden de take-profit lista si se alcanza el rango de +2.0% a +3.5% o si el RSI de 1H supera 70. Si el mercado cripto pierde dinamismo en los próximos ciclos, rotar capital hacia oportunidades de mayor velocidad."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **67** | 🎯 **38.8%** (26W / 27L / 14BE) | 🔴 **$-1.84 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-17 19:10` | 🟢 BUY | `ETH-USD` | $10.00 | $2385.05 | ETH-USD muestra un RSI de 1H en 29.0 (sobreventa profunda) combinado con un cambio de 1h p... |
| `2026-10-17 19:10` | 🟢 BUY | `SOL-USD` | $10.00 | $102.65 | SOL-USD presenta un RSI de 1H en 31.5 saliendo de zona de sobreventa estricta y un cambio ... |
| `2026-10-17 19:00` | 🟢 BUY | `BTC-USD` | $10.00 | $81170.65 | BTC-USD muestra un RSI de 1H saliendo de niveles bajos (37.5) con un cambio positivo de 0.... |
| `2026-10-17 18:40` | 🔴 SELL (-0.22$) | `ETH-USD` | $9.78 | $2370.09 | La posición acumula una pérdida de -2.21%, excediendo el umbral de stop-loss del -2.0%. El... |
| `2026-10-17 18:40` | 🔴 SELL (-0.21$) | `SOL-USD` | $9.79 | $101.78 | La posición ha alcanzado una pérdida de -2.08%, rompiendo el límite de stop-loss estricto ... |

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
