# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 20:30:51`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$34.69 USD** | **$38.68 USD** | 🔴 **-3.29%** ($-1.32) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 9h 50m |
| `ETH-USD` | 0.004178 | $2393.62 | $2404.75 | $10.05 | 📈 +0.46% | 7h 39m |
| `SOL-USD` | 0.096034 | $104.13 | $104.94 | $10.08 | 📈 +0.78% | 3h 50m |
| `BTC-USD` | 0.000056 | $81874.05 | $81916.14 | $4.57 | 📈 +0.05% | 3h 20m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general se encuentra mayormente consolidando en una tendencia bajista de corto plazo por debajo de la SMA20. Los activos de renta variable tradicional (QQQ, SPY, NVDA, etc.) se encuentran cerrados, por lo que el foco está 100% en el mercado de criptomonedas (ABIERTO 24/7). Las posiciones en SOL-USD, ETH-USD y BTC-USD muestran ligeras ganancias pero carecen de un impulso fuerte de continuación, manteniendo un comportamiento de rebote técnico débil. Mantendremos las posiciones vigentes mientras operamos de forma táctica."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 70%): SOL-USD se mantiene con una ganancia moderada de +0.78%. Aunque el RSI diario sigue en zona profunda de sobreventa (22.0), el impulso de 1 hora se ha desacelerado ligeramente. Mantenemos la posición a la espera de un acercamiento al objetivo de take-profit.
- **[HOLD] ETH-USD** (Confianza: 65%): ETH-USD registra una ganancia del +0.46%. El precio se sostiene por encima del precio de entrada tras varias horas de tenencia. Mantenemos la posición vigilando el soporte y buscando una aceleración del RSI de 1 hora.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en SOL-USD, ETH-USD, BTC-USD y QQQ vigilando de cerca los niveles de take-profit entre +2.0% y +3.5% o el stop-loss estricto en -2.0%. Si las criptomonedas continúan estancadas sin superar los umbrales de momentum en las próximas horas, rotaremos el capital hacia oportunidades con mayor volatilidad en el próximo ciclo."
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
