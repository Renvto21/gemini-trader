# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 08:30:50`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.47 USD** | **$38.47 USD** | 🔴 **-3.82%** ($-1.53) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 21h 50m |
| `ETH-USD` | 0.004178 | $2393.62 | $2383.60 | $9.96 | 📉 -0.42% | 19h 39m |
| `SOL-USD` | 0.096034 | $104.13 | $104.08 | $10.00 | 📉 -0.05% | 15h 50m |
| `BTC-USD` | 0.000105 | $81767.70 | $81403.76 | $8.53 | 📉 -0.45% | 15h 20m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional (Wall Street) se encuentra cerrado, por lo que toda la actividad se concentra exclusivamente en el mercado de criptomonedas, que opera 24/7. Las criptomonedas principales (SOL-USD, ETH-USD, BTC-USD) muestran un comportamiento lateral con sesgo ligeramente bajista en el corto plazo, manteniendo RSI de 1 hora en niveles neutrales o de ligera compresión (entre 34 y 41), mientras que sus RSI diarios permanecen en zonas de sobreventa profunda, lo que respalda mantener la tesis de rebote técnico a mediano plazo. Las posiciones actuales se encuentran estables dentro de los márgenes de tolerancia de riesgo sin activar los stop-loss."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición se mantiene estable con una pérdida marginal del -0.05%. El RSI diario en 21.2 sugiere un soporte macro sólido y potencial de rebote en cuanto el volumen acompañe, por lo que se decide mantener sin realizar cambios.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra un RSI diario de 24.1 indicando sobreventa profunda. La posición registra una pérdida menor del -0.42%, manteniéndose holgadamente por encima del umbral de stop-loss.
- **[HOLD] BTC-USD** (Confianza: 75%): Bitcoin se mantiene consolidando cerca de su soporte local con un RSI de 1 hora en 34.4. La pérdida actual es de -0.45%, manteniendo la vigencia de la estrategia de acumulación para el rebote.
- **[HOLD] QQQ** (Confianza: 70%): El mercado de valores se encuentra cerrado y la posición en QQQ muestra una variación casi nula (-0.08%). Se mantendrá en cartera hasta la apertura de Wall Street para evaluar su desempeño.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas actuales (QQQ, ETH-USD, SOL-USD, BTC-USD) ya que ninguna ha alcanzado el stop-loss estricto del -2.0% ni el objetivo de take-profit del +2.0%. Dado que el efectivo disponible es de 0.0 USD, no se pueden realizar nuevas compras en este ciclo. Monitorear de cerca el impulso de las criptomonedas y esperar a que alcancen zonas de take-profit o que el mercado tradicional abra para evaluar posibles rotaciones de capital."
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
