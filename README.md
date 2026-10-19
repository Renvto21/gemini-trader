# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 19:20:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$34.76 USD** | **$38.76 USD** | 🔴 **-3.11%** ($-1.24) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 8h 40m |
| `ETH-USD` | 0.004178 | $2393.62 | $2410.80 | $10.07 | 📈 +0.72% | 6h 29m |
| `SOL-USD` | 0.096034 | $104.13 | $105.32 | $10.11 | 📈 +1.14% | 2h 39m |
| `BTC-USD` | 0.000056 | $81874.05 | $82115.33 | $4.58 | 📈 +0.29% | 2h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que el foco absoluto está en el ecosistema cripto que opera 24/7. Las posiciones actuales en ETH-USD, SOL-USD y BTC-USD muestran un comportamiento positivo con ligeras ganancias, destacando SOL-USD con un avance del 1.14% y un RSI de 1 hora recuperándose a 47.7. QQQ permanece en cartera a la espera de la apertura de Wall Street. Mantendremos el curso actual sin cerrar posiciones prematuramente, ya que el momentum alcista de corto plazo en criptomonedas aún no alcanza la zona de take-profit objetivo de +2.0% a +3.5%."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD muestra un rendimiento positivo de +1.14% con un RSI de 1h en 47.7 y cambio horario positivo (+0.68%). Se mantiene la posición para buscar el objetivo de take-profit entre +2.0% y +3.5%.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD registra una ganancia moderada de +0.72% y un RSI de 1h en 40.3. Continuamos dentro de la operación buscando la extensión del rebote técnico.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener posiciones abiertas (QQQ, ETH-USD, SOL-USD, BTC-USD). Monitorear de cerca a SOL-USD y ETH-USD para asegurar beneficios parciales o totales si alcanzan el rango de take-profit (+2.0% a +3.5%) o si el RSI de 1 hora supera 70. Establecer stop-loss estricto a -2.0% en cada posición abierta. No se realizan nuevas compras para conservar la liquidez mínima de $4.00 USD."
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
