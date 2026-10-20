# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 23:30:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.58 USD** | **$38.58 USD** | 🔴 **-3.56%** ($-1.42) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 12h 49m |
| `ETH-USD` | 0.004178 | $2393.62 | $2392.65 | $10.00 | 📉 -0.04% | 10h 39m |
| `SOL-USD` | 0.096034 | $104.13 | $104.60 | $10.05 | 📈 +0.45% | 6h 49m |
| `BTC-USD` | 0.000105 | $81767.70 | $81567.92 | $8.54 | 📉 -0.24% | 6h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general de criptomonedas se encuentra operando en un rango lateral con sesgo bajista de corto plazo, manteniendo los mercados tradicionales cerrados. BTC-USD muestra un RSI de 1 hora en 26.6, reflejando condiciones de sobreventa extrema donde podría buscarse un rebote inminente, mientras que SOL-USD muestra resiliencia con una ligera ganancia porcentual y ETH-USD se mantiene estable en soportes."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición se mantiene con una ganancia actual de +0.45%. No se vende aún ya que buscamos alcanzar el objetivo de take-profit entre +2.0% y +3.5% aprovechando el rebote desde la sobreventa diaria.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas actuales ya que ninguna ha alcanzado el stop-loss estricto de -2.0% y la liquidez en efectivo es cero. Monitorear de cerca el RSI de 1 hora de BTC-USD para evaluar una posible expansión del rebote técnico y preparar la toma de ganancias en SOL-USD si alcanza el objetivo de +2.0% a +3.5%."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **77** | 🎯 **42.9%** (33W / 29L / 15BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-19 23:00` | 🟢 BUY | `BTC-USD` | $4.00 | $81646.39 | BTC-USD presenta un RSI de 1 hora en 27.7, nivel de sobreventa profunda ideal para un rebo... |
| `2026-10-19 17:10` | 🟢 BUY | `BTC-USD` | $4.57 | $81874.05 | BTC-USD muestra señales de rebote técnico con un RSI de 1 hora en 31.1 recuperándose y un ... |
| `2026-10-19 16:40` | 🟢 BUY | `SOL-USD` | $10.00 | $104.13 | SOL-USD presenta un RSI diario extremo de 19.7, indicando condiciones de sobreventa profun... |
| `2026-10-19 12:51` | 🟢 BUY | `ETH-USD` | $10.00 | $2393.62 | ETH-USD presenta un RSI de 1 hora en 34.6, entrando en zona de sobreventa de corto plazo, ... |
| `2026-10-19 10:40` | 🟢 BUY | `QQQ` | $10.00 | $718.92 | QQQ muestra un fuerte momentum intradiario con un cambio de 1h del +1.28%, liderando el re... |

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
