# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 17:40:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$34.63 USD** | **$38.62 USD** | 🔴 **-3.45%** ($-1.38) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 6h 59m |
| `ETH-USD` | 0.004178 | $2393.62 | $2400.28 | $10.03 | 📈 +0.28% | 4h 49m |
| `SOL-USD` | 0.096034 | $104.13 | $104.47 | $10.03 | 📈 +0.33% | 59m |
| `BTC-USD` | 0.000056 | $81874.05 | $81916.99 | $4.57 | 📈 +0.05% | 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de valores tradicional (Wall Street) se encuentra cerrado, por lo que la liquidez activa y las oportunidades de operacion se concentran exclusivamente en las criptomonedas (24/7). Las posiciones en cripto muestran ligeras recuperaciones con rendimientos positivos marginales, mientras que el mercado cripto general intenta construir un soporte tras caídas recientes."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD muestra un rendimiento positivo de +0.33% y un impulso de corto plazo favorable con RSI de 1h en 38.8. Se mantiene la posición a la espera del objetivo de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones activas en SOL-USD, ETH-USD y BTC-USD mientras muestran un comportamiento estable y buscan el objetivo de take-profit entre +2.0% y +3.5%. La posición en QQQ se mantiene congelada por el cierre de mercado. Monitorear de cerca los niveles de RSI de 1 hora y el stop-loss estricto en -2.0% para proteger el capital ante cualquier cambio drástico."
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
