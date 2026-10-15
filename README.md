# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 13:30:47`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.26 USD** | **$34.41 USD** | **$38.67 USD** | 🔴 **-3.32%** ($-1.33) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $343.97 | $9.94 | 📉 -0.63% | 1d 2h |
| `MSFT` | 0.012146 | $535.17 | $539.62 | $6.55 | 📈 +0.83% | 2h 40m |
| `QQQ` | 0.013791 | $725.09 | $722.65 | $9.97 | 📉 -0.34% | 1h 10m |
| `NVDA` | 0.036812 | $217.32 | $216.08 | $7.95 | 📉 -0.57% | 40m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado se encuentra mixto con sesgo bajista en varios índices y acciones tecnológicas importantes, aunque existen claras señales de sobreventa extrema en activos clave como QQQ (rsi_1h en 21.4) y NVDA (rsi_1h en 18.1), lo cual representa oportunidades tácticas de rebote a corto plazo (mean reversion). Las criptomonedas se mantienen estables pero sin el impulso suficiente en este ciclo específico para desviar la atención de las oportunidades en renta variable que siguen abiertas."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 70%): La posición muestra un rendimiento lateral leve (-0.63%) tras más de un día abierta. Se mantiene en cartera a la espera de un impulso alcista que confirme su tendencia macro o para evaluar rotación si no muestra dinamismo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener la vigilancia sobre MSFT que se acerca al objetivo de toma de ganancias (+0.83% actual). Monitorear de cerca AAPL, QQQ y NVDA para cortar cualquier pérdida si se acercan al umbral estricto del -2.0% o asegurar ganancias rápidas si el RSI de 1 hora rebota hacia la zona de sobrecompra (>70). La liquidez en efectivo se mantiene en niveles mínimos para maximizar la exposición al crecimiento acelerado."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **57** | 🎯 **42.1%** (24W / 19L / 14BE) | 🔴 **$-1.12 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-15 12:50` | 🟢 BUY | `NVDA` | $8.00 | $217.32 | NVDA presenta un RSI de 1h en sobreventa extrema (21.5) con un inicio de recuperación en s... |
| `2026-10-15 12:20` | 🟢 BUY | `QQQ` | $10.00 | $725.09 | QQQ muestra un RSI de 1h en sobreventa extrema (28.7) cruzando al alza con un cambio posit... |
| `2026-10-15 12:10` | 🔴 SELL (+0.14$) | `ETH-USD` | $6.14 | $2417.73 | ETH-USD ha alcanzado un rendimiento del +2.33%, cumpliendo con el rango establecido para l... |
| `2026-10-15 11:50` | 🔴 SELL (+0.13$) | `SOL-USD` | $6.13 | $104.21 | SOL-USD ha alcanzado un rendimiento de +2.11%, cumpliendo con la regla de toma rápida de g... |
| `2026-10-15 10:50` | 🟢 BUY | `MSFT` | $6.50 | $535.17 | MSFT presenta un RSI de 1h ultra comprimido en sobreventa extrema (14.7) con un cambio pos... |

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
