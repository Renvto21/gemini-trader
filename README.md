# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 01:10:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$30.48 USD** | **$8.06 USD** | **$38.54 USD** | 🔴 **-3.65%** ($-1.46) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.003330 | $2402.76 | $2421.26 | $8.06 | 📈 +0.77% | 3h 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado durante el fin de semana, por lo que toda la actividad se concentra en el mercado de criptomonedas (24/7). Los principales activos cripto (ETH-USD, SOL-USD, BTC-USD) muestran un rebote interesante pero se acercan o ya superan zonas de sobrecompra en el RSI de 1 hora (ETH-USD en 66.5, SOL-USD en 73.2 y BTC-USD en 76.8). Esto indica que estamos cerca de la zona objetivo para asegurar beneficios parciales o totales de nuestras posiciones abiertas."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD se encuentra actualmente con una ganancia del +0.77% y un RSI de 1 hora en 66.5. Todavía no alcanza el umbral de take-profit del +2.0% ni la zona extrema de sobrecompra >70, por lo que mantenemos la posición esperando capturar un poco más de impulso alcista antes de la toma de beneficios.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos ETH-USD abierta pero vigilaremos de cerca el RSI de 1 hora. Si cruza por completo los 70 puntos o alcanza una ganancia del +2.0% al +3.5%, procederemos a vender para asegurar capital en efectivo. Dejaremos una reserva de liquidez adecuada y buscaremos posibles retrocesos en SOL-USD o BTC-USD para reentrar tras una corrección a corto plazo."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **76** | 🎯 **42.1%** (32W / 29L / 15BE) | 🔴 **$-1.38 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-19 01:00` | 🔴 SELL (-0.00$) | `SOL-USD` | $8.00 | $105.08 | SOL-USD ha entrado en sobrecompra con un RSI de 1 hora en 72.7, cumpliendo estrictamente c... |
| `2026-10-18 23:20` | 🟢 BUY | `SOL-USD` | $8.00 | $105.11 | SOL-USD presenta un RSI diario en 21.8 (sobreventa extrema) y un momentum de 24 horas alci... |
| `2026-10-18 23:10` | 🔴 SELL (+0.17$) | `SOL-USD` | $8.17 | $105.19 | SOL-USD acumula una ganancia del +2.12%, cumpliendo con la regla de toma rápida de gananci... |
| `2026-10-18 21:20` | 🟢 BUY | `ETH-USD` | $8.00 | $2402.76 | ETH-USD muestra un RSI diario fuertemente sobrevendido en 23.2 y un cambio positivo en la ... |
| `2026-10-18 21:00` | 🔴 SELL (+0.16$) | `ETH-USD` | $8.16 | $2409.06 | ETH-USD ha alcanzado una ganancia del +2.03%, cumpliendo con la regla de toma rápida de ga... |

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
