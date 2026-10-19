# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 13:30:54`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.57 USD** | **$20.04 USD** | **$38.60 USD** | 🔴 **-3.49%** ($-1.40) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $720.84 | $10.03 | 📈 +0.27% | 2h 50m |
| `ETH-USD` | 0.004178 | $2393.62 | $2396.37 | $10.01 | 📈 +0.11% | 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado se encuentra en una fase de consolidación de corto plazo con sesgo bajista general bajo la SMA20 en la mayoría de los activos de referencia. Las criptomonedas muestran ligeros intentos de estabilización tras haber tocado niveles de soporte diario, mientras que los índices tradicionales operan con un momentum intradiario plano a ligeramente negativo."

**Operaciones del ciclo:**
- **[HOLD] QQQ** (Confianza: 65%): La posición en QQQ lleva menos de 3 horas abierta y muestra una ganancia marginal del +0.27%. El momentum intradiario se ha desacelerado ligeramente, pero se mantiene por encima del precio de entrada, por lo que es prudente mantener y esperar el objetivo de take-profit.
- **[HOLD] ETH-USD** (Confianza: 65%): ETH-USD muestra un leve rebote intradiario tras salir de la zona de sobreventa, cotizando con una ganancia del +0.11%. Mantenemos la posición activa buscando un mayor impulso que permita alcanzar la zona de toma de beneficios.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantenemos las posiciones actuales en QQQ y ETH-USD mientras se desarrollan dentro de un rango estrecho sin alcanzar todavía el objetivo de take-profit (+2.0% a +3.5%) ni activar el stop-loss estricto (-2.0%). Monitorearemos de cerca el RSI de 1 hora de ETH-USD y QQQ para asegurar beneficios rápidamente si se produce un repunte o para cortar pérdidas si el soporte cede."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **77** | 🎯 **42.9%** (33W / 29L / 15BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-19 12:51` | 🟢 BUY | `ETH-USD` | $10.00 | $2393.62 | ETH-USD presenta un RSI de 1 hora en 34.6, entrando en zona de sobreventa de corto plazo, ... |
| `2026-10-19 10:40` | 🟢 BUY | `QQQ` | $10.00 | $718.92 | QQQ muestra un fuerte momentum intradiario con un cambio de 1h del +1.28%, liderando el re... |
| `2026-10-19 01:50` | 🔴 SELL (+0.09$) | `ETH-USD` | $8.09 | $2428.97 | ETH-USD registra una ganancia acumulada y su RSI de 1 hora ha alcanzado 68.3, acercándose ... |
| `2026-10-19 01:00` | 🔴 SELL (-0.00$) | `SOL-USD` | $8.00 | $105.08 | SOL-USD ha entrado en sobrecompra con un RSI de 1 hora en 72.7, cumpliendo estrictamente c... |
| `2026-10-18 23:20` | 🟢 BUY | `SOL-USD` | $8.00 | $105.11 | SOL-USD presenta un RSI diario en 21.8 (sobreventa extrema) y un momentum de 24 horas alci... |

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
