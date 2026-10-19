# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 22:40:36`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.31 USD** | **$16.19 USD** | **$38.51 USD** | 🔴 **-3.74%** ($-1.49) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.077662 | $103.01 | $104.69 | $8.13 | 📈 +1.63% | 3h 9m |
| `ETH-USD` | 0.003330 | $2402.76 | $2421.84 | $8.06 | 📈 +0.79% | 1h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado por lo que la liquidez opera 100% en criptomonedas (ABIERTO 24/7). SOL-USD muestra un rendimiento positivo con un PnL de +1.63% acercándose a la zona de take-profit, mientras que ETH-USD se mantiene estable con +0.79%. El momentum en ambas criptomonedas se mantiene favorable con RSI de 1h saludables y recuperación desde niveles diarios sobrevendidos."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD presenta una ganancia actual de +1.63% tras 3 horas de tenencia. El RSI de 1h se sitúa en 55.2 y el cambio en la última hora es positivo (+0.51%), por lo que mantenemos la posición a la espera de que alcance el objetivo de take-profit entre +2.0% y +3.5%.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra un rendimiento de +0.79% con un RSI de 1h en 51.6 y cambio horario positivo. Mantenemos la posición abierta mientras se acerca gradualmente al rango de toma de ganancias establecido.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones abiertas de SOL-USD y ETH-USD supervisando de cerca la zona de take-profit entre +2.0% y +3.5%. Si SOL-USD alcanza dicho umbral, realizaremos una venta parcial para asegurar capital y mantener la disciplina de rotación rápida. Stop-loss estricto en -2.0% para proteger la cuenta."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **74** | 🎯 **41.9%** (31W / 29L / 14BE) | 🔴 **$-1.55 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-18 21:20` | 🟢 BUY | `ETH-USD` | $8.00 | $2402.76 | ETH-USD muestra un RSI diario fuertemente sobrevendido en 23.2 y un cambio positivo en la ... |
| `2026-10-18 21:00` | 🔴 SELL (+0.16$) | `ETH-USD` | $8.16 | $2409.06 | ETH-USD ha alcanzado una ganancia del +2.03%, cumpliendo con la regla de toma rápida de ga... |
| `2026-10-18 19:30` | 🟢 BUY | `SOL-USD` | $8.00 | $103.01 | SOL-USD presenta un RSI diario extremadamente bajo (16.5) y un RSI de 1h recuperándose has... |
| `2026-10-18 19:10` | 🔴 SELL (+0.17$) | `SOL-USD` | $8.17 | $102.92 | SOL-USD ha alcanzado un rendimiento de +2.07% cumpliendo con nuestra regla de toma rápida ... |
| `2026-10-18 18:40` | 🟢 BUY | `ETH-USD` | $8.00 | $2361.22 | ETH-USD muestra un RSI diario deprimido en 21.5 y un RSI de 1 hora que se recupera a 34.3 ... |

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
