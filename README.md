# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 04:00:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.59 USD** | **$38.59 USD** | 🔴 **-3.54%** ($-1.41) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 17h 20m |
| `ETH-USD` | 0.004178 | $2393.62 | $2393.79 | $10.00 | 📈 +0.01% | 15h 9m |
| `SOL-USD` | 0.096034 | $104.13 | $104.51 | $10.04 | 📈 +0.36% | 11h 20m |
| `BTC-USD` | 0.000105 | $81767.70 | $81681.95 | $8.56 | 📉 -0.10% | 10h 49m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado y los activos tecnológicos como QQQ muestran estancamiento bajo la SMA20. En cuanto a las criptomonedas, operan 24/7 pero se encuentran con un impulso lateral a bajista en el corto plazo (cambios de 1 hora cercanos a cero o ligeramente negativos). Las posiciones actuales se mantienen estables pero sin alcanzar todavía el take-profit objetivo de +2.0% o un RSI de 1 hora superior a 70. Mantendremos la disciplina y el monitoreo estricto de los soportes."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD muestra una pequeña ganancia del 0.36% y se mantiene operando 24/7. El RSI de 1 hora está en 58.6, acercándose a niveles óptimos para evaluar un take-profit parcial si supera los 70 puntos. Mantenemos la posición por ahora.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales (QQQ, ETH-USD, SOL-USD, BTC-USD) ya que ninguna ha alcanzado el stop-loss estricto de -2.0% ni el take-profit de +2.0%. Estar atento al mercado de criptomonedas para asegurar ganancias si SOL-USD o ETH-USD disparan su RSI por encima de 70, o bien rotar capital si alguna posición muestra debilidad prolongada."
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
