# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 21:30:49`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$34.45 USD** | **$38.44 USD** | 🔴 **-3.89%** ($-1.56) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $709.80 | $9.87 | 📉 -1.27% | 10h 50m |
| `ETH-USD` | 0.004178 | $2393.62 | $2394.90 | $10.01 | 📈 +0.05% | 8h 39m |
| `SOL-USD` | 0.096034 | $104.13 | $104.36 | $10.02 | 📈 +0.22% | 4h 50m |
| `BTC-USD` | 0.000056 | $81874.05 | $81474.44 | $4.55 | 📉 -0.49% | 4h 20m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado accionario tradicional (QQQ, SPY, NVDA, MSFT, AAPL, GLD) se encuentra cerrado, por lo que toda la atención táctica se centra en los mercados de criptomonedas (24/7). Las criptomonedas principales (SOL-USD, ETH-USD, BTC-USD) muestran ligeros retrocesos en la última hora y una tendencia general bajista en marcos diarios, pero se mantienen estables dentro de los rangos de acumulación tras los rebotes previos. No se observan señales de pánico ni rupturas de soporte mayores a -2.0%, por lo que la postura se mantiene defensiva y de vigilancia."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición se mantiene estable con una ganancia marginal del +0.22%. El precio está respetando el soporte tras el rebote y no ha activado ninguna condición de salida o stop-loss. Mantenemos la posición buscando alcanzar el objetivo de take-profit entre +2.0% y +3.5%.
- **[HOLD] ETH-USD** (Confianza: 75%): La posición se encuentra neutral (+0.05%) operando cerca del precio de entrada. Mantiene su vigencia operativa ya que no muestra debilidad estructural que amerite cortar la posición antes del stop-loss.
- **[HOLD] BTC-USD** (Confianza: 70%): Presenta una ligera pérdida no realizada de -0.49%, manteniéndose holgadamente por encima del límite de stop-loss estricto de -2.0%. Esperamos confirmación de volumen alcista en el próximo ciclo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en criptomonedas (SOL-USD, ETH-USD, BTC-USD) y QQQ a pesar de la consolidación de corto plazo. Vigilar estrictamente los stop-loss en -2.0% y mantener la expectativa de toma de ganancias (take-profit) entre +2.0% y +3.5%. Dado que el mercado tradicional está cerrado y las criptomonedas muestran un momentum moderado, se prioriza preservar la liquidez actual de $4.00 USD y no realizar nuevas entradas hasta ver una confirmación de volumen y un RSI de 1 hora saliendo de zonas de compresión."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **77** | 🎯 **42.9%** (33W / 29L / 15BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-19 17:10` | 🟢 BUY | `BTC-USD` | $4.57 | $81874.05 | BTC-USD muestra señales de rebote técnico con un RSI de 1 hora en 31.1 recuperándose y un ... |
| `2026-10-19 16:40` | 🟢 BUY | `SOL-USD` | $10.00 | $104.13 | SOL-USD presenta un RSI diario extremo de 19.7, indicando condiciones de sobreventa profun... |
| `2026-10-19 12:51` | 🟢 BUY | `ETH-USD` | $10.00 | $2393.62 | ETH-USD presenta un RSI de 1 hora en 34.6, entrando en zona de sobreventa de corto plazo, ... |
| `2026-10-19 10:40` | 🟢 BUY | `QQQ` | $10.00 | $718.92 | QQQ muestra un fuerte momentum intradiario con un cambio de 1h del +1.28%, liderando el re... |
| `2026-10-19 01:50` | 🔴 SELL (+0.09$) | `ETH-USD` | $8.09 | $2428.97 | ETH-USD registra una ganancia acumulada y su RSI de 1 hora ha alcanzado 68.3, acercándose ... |

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
