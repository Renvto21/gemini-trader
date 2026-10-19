# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 21:40:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.31 USD** | **$16.09 USD** | **$38.40 USD** | 🔴 **-4.00%** ($-1.60) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.077662 | $103.01 | $104.00 | $8.08 | 📈 +0.96% | 2h 9m |
| `ETH-USD` | 0.003330 | $2402.76 | $2406.16 | $8.01 | 📈 +0.14% | 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que toda la atención y liquidez se centran exclusivamente en el mercado de criptomonedas (abierto 24/7). Observamos un impulso positivo moderado en los activos principales como SOL-USD y ETH-USD, los cuales muestran un rebote técnico favorable desde niveles diarios muy sobrevendidos con un cambio de 1h positivo, aunque todavía sin alcanzar el objetivo de take-profit óptimo."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD muestra un rendimiento positivo constante (+0.96%) con un RSI de 1h saludable en 50.9. Mantenemos la posición a la espera de que el impulso alcista continúe hacia el rango de take-profit.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD mantiene una ganancia leve y positiva tras su reciente recompra, con un RSI de 1h en 45.4 y cambio horario favorable (+0.77%). Esperamos el desarrollo del rebote técnico diario.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantenemos las posiciones abiertas en SOL-USD y ETH-USD mientras monitoreamos de cerca su evolución hacia el objetivo de take-profit entre +2.0% y +3.5% o hasta que el RSI de 1h alcance la zona de sobrecompra (>70). El stop-loss se mantiene estricto en -2.0% para proteger el capital ante cualquier giro repentino. Tenemos suficiente liquidez disponible pero preferimos consolidar estas posiciones actuales antes de expandirnos."
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
