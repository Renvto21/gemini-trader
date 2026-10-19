# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 20:10:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$34.68 USD** | **$38.67 USD** | 🔴 **-3.32%** ($-1.33) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 9h 30m |
| `ETH-USD` | 0.004178 | $2393.62 | $2402.98 | $10.04 | 📈 +0.39% | 7h 19m |
| `SOL-USD` | 0.096034 | $104.13 | $104.90 | $10.07 | 📈 +0.74% | 3h 29m |
| `BTC-USD` | 0.000056 | $81874.05 | $81927.49 | $4.57 | 📈 +0.07% | 2h 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que la liquidez y operativa se concentran exclusivamente en las criptomonedas (24/7). Los criptoactivos en cartera (SOL-USD, ETH-USD, BTC-USD) muestran un comportamiento lateral con ligeras ganancias acumuladas pero sin alcanzar todavía la zona objetivo de take-profit (+2.0% a +3.5%). QQQ permanece cerrado sin cambios significativos."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): La posición en SOL-USD mantiene una ganancia leve de +0.74% tras 3.5 horas abierta. Se mantiene para permitir que el rebote continúe hacia la zona objetivo de take-profit.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD muestra estabilidad con una pequeña ganancia del +0.39%. El RSI de 1 hora se mantiene en niveles neutrales, por lo que se prefiere mantener la posición abierta.
- **[HOLD] BTC-USD** (Confianza: 80%): BTC-USD se encuentra estable cerca del precio de entrada. Se mantiene a la espera de un mayor impulso alcista.
- **[HOLD] QQQ** (Confianza: 80%): El mercado de Wall Street está cerrado y QQQ se mantiene sin cambios relevantes. Se conserva hasta la apertura del mercado bursátil.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en ETH-USD, SOL-USD, BTC-USD y QQQ mientras maduran los rebotes. Monitorear de cerca los objetivos de take-profit (+2.0% a +3.5%) o los niveles de stop-loss estricto (-2.0%) para proteger capital. Conservar la reserva mínima de efectivo de $4.00 USD. No se ejecutan nuevas operaciones en este ciclo."
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
