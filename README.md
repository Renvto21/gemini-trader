# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 06:30:49`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.45 USD** | **$38.45 USD** | 🔴 **-3.89%** ($-1.55) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 19h 50m |
| `ETH-USD` | 0.004178 | $2393.62 | $2381.52 | $9.95 | 📉 -0.51% | 17h 39m |
| `SOL-USD` | 0.096034 | $104.13 | $103.96 | $9.98 | 📉 -0.16% | 13h 50m |
| `BTC-USD` | 0.000105 | $81767.70 | $81336.11 | $8.52 | 📉 -0.53% | 13h 20m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general muestra un sentimiento mixto a bajista con la mayoría de los activos tradicionales (QQQ, SPY, GLD, MSFT, AAPL, NVDA) en mercados cerrados. Por otro lado, las criptomonedas (SOL-USD, ETH-USD, BTC-USD) se mantienen operando 24/7 en una fase de consolidación con sesgo lateral/bajista de corto plazo, donde los RSI de 1 hora se mantienen neutrales (entre 39 y 51) sin mostrar aún el impulso de ruptura alcista necesario para detonar un rebote agresivo, pero manteniéndose alejados de los niveles de stop-loss estricto."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 70%): La posición lleva cerca de 14 horas abierta con una pérdida marginal del -0.16%. El RSI de 1 hora se encuentra en 51.4 y el mercado opera sin catalizadores fuertes de corto plazo. Mantenemos la posición a la espera de un impulso alcista que permita asegurar ganancias.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales (QQQ, ETH-USD, SOL-USD y BTC-USD) ya que ninguna ha alcanzado el límite de stop-loss de -2.0% ni los objetivos de take-profit de +2.5% a +3.5%. Monitorearemos de cerca el comportamiento de SOL-USD y ETH-USD en los siguientes ciclos en busca de una aceleración en el RSI de 1 hora por encima de 65-70 para realizar tomas parciales de ganancias. Si alguna posición rompe a la baja superando el umbral de pérdida del -2.0%, procederemos a la venta inmediata para proteger el capital."
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
