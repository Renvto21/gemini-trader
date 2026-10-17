# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 11:40:35`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$28.48 USD** | **$10.02 USD** | **$38.50 USD** | 🔴 **-3.76%** ($-1.50) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096209 | $103.94 | $104.16 | $10.02 | 📈 +0.21% | 1h 20m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado por lo que la liquidez activa se concentra en las criptomonedas. SOL-USD mantiene una posición abierta con un beneficio marginal del 0.21% tras su reciente entrada en soporte diario, mientras que ETH-USD muestra un RSI diario de 29.0 y un cambio de 1h positivo, indicando potencial de rebote técnico."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición en SOL-USD lleva poco más de una hora abierta, mostrando una ligera ganancia (0.21%) y un RSI de 1h neutral en 48.8. Dado que el activo opera 24/7 y mantiene su soporte diario, se mantiene la posición para buscar el objetivo de take-profit sin apresurar una salida.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos SOL-USD buscando alcanzar el objetivo de take-profit entre +2.0% y +3.5% o hasta que el RSI de 1 hora supere los 70 puntos. El stop-loss estricto para SOL-USD se mantiene en -2.0%. Estaremos atentos a la evolución del momentum de ETH-USD para evaluar una posible entrada si consolida su tendencia de recuperación intradiaria."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **65** | 🎯 **40.0%** (26W / 25L / 14BE) | 🔴 **$-1.41 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-17 10:20` | 🟢 BUY | `SOL-USD` | $10.00 | $103.94 | SOL-USD presenta un RSI diario en niveles de sobreventa extrema (22.5) y un cambio positiv... |
| `2026-10-17 04:30` | 🔴 SELL (+0.12$) | `SOL-USD` | $10.12 | $104.94 | SOL-USD ha alcanzado un RSI de 1 hora de 70.4, entrando en zona de sobrecompra, y acumula ... |
| `2026-10-17 04:00` | 🔴 SELL (+0.07$) | `ETH-USD` | $10.07 | $2429.64 | ETH-USD ha alcanzado un RSI de 1 hora de 73.3, entrando en zona de sobrecompra. Siguiendo ... |
| `2026-10-16 16:30` | 🟢 BUY | `ETH-USD` | $10.00 | $2412.98 | ETH-USD muestra un RSI diario en niveles de sobreventa extrema (30.3) y un cambio positivo... |
| `2026-10-16 16:30` | 🔴 SELL (-0.11$) | `MSFT` | $6.39 | $526.18 | MSFT lleva más de 1 día y 5 horas abierto mostrando debilidad persistente y un rendimiento... |

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
