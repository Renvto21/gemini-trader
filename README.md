# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 21:20:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.31 USD** | **$16.06 USD** | **$38.37 USD** | 🔴 **-4.08%** ($-1.63) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.077662 | $103.01 | $103.76 | $8.06 | 📈 +0.73% | 1h 49m |
| `ETH-USD` | 0.003330 | $2402.76 | $2402.76 | $8.00 | 📈 +0.00% | 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de valores tradicional se encuentra cerrado y con precios congelados, por lo que toda la actividad se concentra en los criptoactivos (24/7). SOL-USD muestra un comportamiento estable con una ganancia actual de +0.73% y un RSI de 1h en recuperación (49.2), mientras que ETH-USD presenta un RSI diario muy deprimido (23.2) y un cambio de 1h positivo (+0.63%), lo que representa una excelente oportunidad táctica de rebote por sobreventa (mean reversion)."

**Operaciones del ciclo:**
- **[BUY] ETH-USD** (Confianza: 85%): ETH-USD muestra un RSI diario fuertemente sobrevendido en 23.2 y un cambio positivo en la última hora del 0.63%, cumpliendo perfectamente con nuestra estrategia de cazar rebotes técnicos en criptomonedas con alta convicción.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Bitácora de ciclo: Mantenemos SOL-USD buscando alcanzar el objetivo de take-profit entre +2.0% y +3.5%, o la zona de sobrecompra en el RSI de 1h (> 70). Abrimos una nueva posición en ETH-USD para aprovechar su RSI diario extremadamente bajo (23.2) y el impulso alcista de corto plazo. Establecemos un stop-loss estricto en -2.0% para ambas posiciones y mantendremos la disciplina de rotación de capital."
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
