# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 21:40:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$34.49 USD** | **$38.48 USD** | 🔴 **-3.80%** ($-1.52) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $709.80 | $9.87 | 📉 -1.27% | 11h 0m |
| `ETH-USD` | 0.004178 | $2393.62 | $2397.00 | $10.01 | 📈 +0.14% | 8h 49m |
| `SOL-USD` | 0.096034 | $104.13 | $104.59 | $10.04 | 📈 +0.44% | 4h 59m |
| `BTC-USD` | 0.000056 | $81874.05 | $81587.56 | $4.55 | 📉 -0.35% | 4h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado y operando de manera lateral-bajista, afectando levemente a QQQ con un PnL de -1.27%. En el sector cripto (24/7), las posiciones ETH-USD y SOL-USD se mantienen en terreno ligeramente positivo, mientras que BTC-USD muestra una ligera compresión pero sin romper soportes críticos. Mantenemos la cautela ante la falta de catalizadores macroeconómicos inmediatos."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD mantiene un rendimiento positivo leve (+0.44%) tras su rebote desde soportes diarios. El RSI de 1 hora se sitúa en 47.4, mostrando estabilidad sin alcanzar todavía el objetivo de take-profit (+2.0% a +3.5%). Se mantiene la posición.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en criptomonedas (ETH-USD, SOL-USD, BTC-USD) y QQQ a la espera de un mayor volumen de negociación en la apertura de Wall Street. Vigilar estrictamente el stop-loss en -2.0% y buscar la toma de ganancias (take-profit) entre +2.0% y +3.5% para ETH-USD y SOL-USD. No se realizarán nuevas compras en este ciclo para preservar la liquidez de $4.00 USD."
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
