# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 17:50:35`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.48 USD** | **$19.99 USD** | **$38.47 USD** | 🔴 **-3.83%** ($-1.53) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096209 | $103.94 | $104.06 | $10.01 | 📈 +0.12% | 7h 29m |
| `ETH-USD` | 0.004126 | $2423.75 | $2418.66 | $9.98 | 📉 -0.21% | 5h 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se mantiene abierto y operando en un rango lateral con sesgo bajista y bajo dinamismo en las últimas horas (cambios de 1h cercanos a cero). Los mercados tradicionales (Wall Street) se encuentran cerrados por el fin de semana, por lo que toda la liquidez y atención táctica se concentra exclusivamente en los activos digitales 24/7. Las posiciones actuales de SOL-USD y ETH-USD muestran un estancamiento prolongado de aproximadamente 6 a 7 horas sin lograr el impulso alcista esperado tras sus condiciones de sobreventa diaria."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 60%): SOL-USD se mantiene cerca del precio de entrada con una ganancia marginal del 0.12%. Aunque el dinamismo es bajo, el RSI diario en 22.6 sugiere que el fondo macro podría sostener un rebote si el volumen aumenta, por lo que se decide mantener la posición temporalmente.
- **[HOLD] ETH-USD** (Confianza: 60%): ETH-USD registra una ligera pérdida de -0.21% tras casi 6 horas de tenencia. Dado que el mercado está cerrado para activos tradicionales y el RSI diario permanece en sobreventa profunda (28.4), se le otorga un ciclo más para mostrar impulso antes de considerar una rotación de capital.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Las posiciones de SOL-USD y ETH-USD llevan varias horas abiertas sin mostrar el rebote de momentum esperado, manteniéndose planas. Mantendremos las posiciones vigentes durante este ciclo evaluando una posible rotación de capital si el RSI de 1 hora no supera la zona de 50 en las próximas horas. El objetivo de take-profit se mantiene entre +2.0% y +3.5%, y los stop-loss se activarán estrictamente si la pérdida alcanza el -2.0% para proteger el capital."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **65** | 🎯 **40.0%** (26W / 25L / 14BE) | 🔴 **$-1.41 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-17 11:50` | 🟢 BUY | `ETH-USD` | $10.00 | $2423.75 | ETH-USD presenta un RSI diario en niveles de sobreventa profunda (28.9) y un cambio positi... |
| `2026-10-17 10:20` | 🟢 BUY | `SOL-USD` | $10.00 | $103.94 | SOL-USD presenta un RSI diario en niveles de sobreventa extrema (22.5) y un cambio positiv... |
| `2026-10-17 04:30` | 🔴 SELL (+0.12$) | `SOL-USD` | $10.12 | $104.94 | SOL-USD ha alcanzado un RSI de 1 hora de 70.4, entrando en zona de sobrecompra, y acumula ... |
| `2026-10-17 04:00` | 🔴 SELL (+0.07$) | `ETH-USD` | $10.07 | $2429.64 | ETH-USD ha alcanzado un RSI de 1 hora de 73.3, entrando en zona de sobrecompra. Siguiendo ... |
| `2026-10-16 16:30` | 🟢 BUY | `ETH-USD` | $10.00 | $2412.98 | ETH-USD muestra un RSI diario en niveles de sobreventa extrema (30.3) y un cambio positivo... |

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
