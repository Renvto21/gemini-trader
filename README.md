# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 22:00:48`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$34.48 USD** | **$38.48 USD** | 🔴 **-3.81%** ($-1.52) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $709.80 | $9.87 | 📉 -1.27% | 11h 20m |
| `ETH-USD` | 0.004178 | $2393.62 | $2397.00 | $10.01 | 📈 +0.14% | 9h 9m |
| `SOL-USD` | 0.096034 | $104.13 | $104.55 | $10.04 | 📈 +0.40% | 5h 20m |
| `BTC-USD` | 0.000056 | $81874.05 | $81597.70 | $4.55 | 📉 -0.34% | 4h 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de Wall Street se encuentra cerrado, manteniendo los precios de los activos tradicionales congelados con sesgo bajista (QQQ y SPY bajo la SMA20). En contraste, el mercado de criptomonedas opera 24/7, mostrando una consolidación lateral leve tras las caídas recientes. Los activos en cartera (ETH-USD, SOL-USD, BTC-USD) se mantienen estables pero sin la fuerza necesaria para alcanzar la zona de take-profit (+2.0% a +3.5%), mientras que QQQ sufre una leve presión bajista pero se mantiene por encima del stop-loss estricto de -2.0%. Mantendremos la postura actual a la espera de un catalizador de volumen en cripto."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 70%): La posición se encuentra estable con una ligera ganancia del 0.14%. Aún no alcanza el objetivo de take-profit del 2% al 3.5%, y el mercado cripto está operando en rango sin invalidar la tesis del rebote técnico diario.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener posiciones actuales (QQQ, ETH-USD, SOL-USD, BTC-USD) sin cambios en este ciclo ya que ninguna ha alcanzado el take-profit (+2% a +3.5%) ni ha perforado el stop-loss estricto (-2.0%). QQQ está con -1.27% y se vigilará de cerca en la apertura del siguiente ciclo de Wall Street. En cripto, monitorear si SOL-USD o ETH-USD generan un impulso de volumen que permita asegurar beneficios rápidos o si se requiere rotación de capital."
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
