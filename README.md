# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 09:40:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.54 USD** | **$38.54 USD** | 🔴 **-3.66%** ($-1.46) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 23h 0m |
| `ETH-USD` | 0.004178 | $2393.62 | $2391.60 | $9.99 | 📉 -0.08% | 20h 49m |
| `SOL-USD` | 0.096034 | $104.13 | $104.31 | $10.02 | 📈 +0.17% | 16h 59m |
| `BTC-USD` | 0.000105 | $81767.70 | $81476.16 | $8.53 | 📉 -0.36% | 16h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra CERRADO, por lo que la liquidez activa se concentra en el mercado de criptomonedas (ABIERTO 24/7). Las criptomonedas principales muestran leves señales de recuperación en el corto plazo (cambios de 1 hora positivos y RSI de 1 hora saliendo de zonas de sobreventa profunda), aunque se mantienen en una tendencia general bajista en marco diario. Mantenemos la cautela y vigilamos de cerca los niveles de take-profit y stop-loss."

**Operaciones del ciclo:**
- *Sin cambios en este ciclo (HOLD)*

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear el comportamiento de SOL-USD, ETH-USD y BTC-USD en busca de un incremento en el RSI de 1 hora por encima de 50 para asegurar ganancias en el rango del +2% al +3.5%. Vigilar estrictamente que ninguna posición rompa el soporte del -2% de pérdida para evitar activar cortes de pérdida manuales antes del circuit breaker. Mantener QQQ en cartera a la espera de la apertura del mercado tradicional."
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
