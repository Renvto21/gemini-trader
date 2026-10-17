# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 20:20:37`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.09 USD** | **$38.13 USD** | 🔴 **-4.67%** ($-1.87) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81230.04 | $10.01 | 📈 +0.07% | 1h 19m |
| `SOL-USD` | 0.097418 | $102.65 | $103.13 | $10.05 | 📈 +0.47% | 1h 9m |
| `ETH-USD` | 0.004193 | $2385.05 | $2392.76 | $10.03 | 📈 +0.32% | 1h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se mantiene abierto operando 24/7, mostrando una consolidación ligera tras los recientes intentos de rebote en BTC-USD, SOL-USD y ETH-USD. Las posiciones actuales se encuentran en terreno ligeramente positivo con holding times de poco más de una hora, sin alcanzar aún los objetivos de take-profit (>70 RSI o +2.0%) ni activar los stop-loss. Los mercados tradicionales (Wall Street) se encuentran cerrados, por lo que la liquidez y la atención táctica se concentran exclusivamente en los activos digitales."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): La posición en BTC-USD lleva poco más de una hora abierta y se encuentra estable con una ligera ganancia. Mantenemos el activo esperando mayor impulso hacia la zona de sobrecompra para buscar take-profit.
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD mantiene un rendimiento positivo de +0.47% y un RSI de 1H en 37.7. Continuamos en la posición para aprovechar la continuación del rebote técnico.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD muestra un comportamiento resiliente con ganancias del +0.32% tras su entrada en sobreventa profunda. Mantenemos la posición a la espera de acercarnos a niveles de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas de BTC-USD, SOL-USD y ETH-USD mientras evolucionan hacia la zona de sobrecompra en el RSI de 1H para ejecutar take-profit parciales o totales al alcanzar ganancias del +2.0% al +3.5%. Vigilar rigurosamente el stop-loss en -2.0% para cada posición y no abrir nuevas operaciones hasta liberar efectivo o identificar un momentum más claro en los criptoactivos."
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
