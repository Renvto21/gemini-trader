# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 05:10:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.44 USD** | **$38.44 USD** | 🔴 **-3.91%** ($-1.56) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 18h 30m |
| `ETH-USD` | 0.004178 | $2393.62 | $2380.99 | $9.95 | 📉 -0.53% | 16h 19m |
| `SOL-USD` | 0.096034 | $104.13 | $103.94 | $9.98 | 📉 -0.18% | 12h 29m |
| `BTC-USD` | 0.000105 | $81767.70 | $81285.92 | $8.51 | 📉 -0.59% | 11h 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El portafolio se encuentra con un PnL total de -3.91% y los mercados tradicionales (QQQ, SPY, etc.) están cerrados, por lo que la liquidez activa se concentra en criptomonedas (ETH-USD, SOL-USD, BTC-USD). Las criptomonedas muestran un sesgo bajista temporal de corto plazo con pequeños retrocesos en la última hora, pero se mantienen estables dentro de los rangos de soporte sin activar el stop-loss estricto del -2.0%."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): La posición se mantiene dentro de los límites de riesgo aceptables con una pérdida menor de -0.18%. El mercado crypto opera 24/7 y esperamos un repunte del momentum tras la estabilización del RSI diario.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales (QQQ, ETH-USD, SOL-USD, BTC-USD) ya que se encuentran operando dentro de los márgenes de riesgo y ninguna ha alcanzado el stop-loss o take-profit. En el siguiente ciclo, si alguna criptomoneda rompe al alza con volumen y supera el RSI de 1 hora por encima de 60, se evaluará una toma parcial de beneficios. Si el soporte falla y se roza el -2.0% en alguna posición, se procederá a recortar pérdidas inmediatamente."
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
