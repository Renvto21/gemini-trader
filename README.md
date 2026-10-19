# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 13:10:51`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.57 USD** | **$20.07 USD** | **$38.63 USD** | 🔴 **-3.42%** ($-1.37) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $722.38 | $10.05 | 📈 +0.48% | 2h 30m |
| `ETH-USD` | 0.004178 | $2393.62 | $2398.25 | $10.02 | 📈 +0.19% | 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un comportamiento mixto con un sesgo lateral a bajista en temporalidades diarias, aunque persisten oportunidades de rebote de muy corto plazo en algunos activos tecnológicos y criptomonedas. Los índices principales como QQQ y SPY se mantienen operando bajo sus medias móviles de 20 periodos, mientras que en el mercado cripto (ETH-USD, SOL-USD) observamos intentos incipientes de estabilización tras caídas semanales, manteniendo los mercados abiertos operando con normalidad."

**Operaciones del ciclo:**
- **[HOLD] QQQ** (Confianza: 75%): La posición en QQQ presenta una ganancia marginal del +0.48% tras 2.3 horas abierta. El momentum se ha estabilizado con un RSI de 1 hora en 49.4. Mantenemos la posición a la espera de que alcance el objetivo de take-profit del +2.0% al +3.5% o active una señal de salida técnica.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra un comportamiento estable con una ganancia del +0.19% y un RSI de 1 hora en 36.8, recuperándose desde la zona de sobreventa reciente. Conservamos la posición para capturar el rebote técnico esperado hacia los niveles de take-profit establecidos.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales en QQQ y ETH-USD mientras monitoreamos de cerca los niveles de take-profit entre +2.0% y +3.5%. Establecemos un stop-loss estricto si alguna de las posiciones rompe a la baja perdiendo más del -2.0%. En el siguiente ciclo evaluaremos la rotación de capital si QQQ o ETH-USD alcanzan sus objetivos o si el momentum intradiario decae."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **77** | 🎯 **42.9%** (33W / 29L / 15BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-19 12:51` | 🟢 BUY | `ETH-USD` | $10.00 | $2393.62 | ETH-USD presenta un RSI de 1 hora en 34.6, entrando en zona de sobreventa de corto plazo, ... |
| `2026-10-19 10:40` | 🟢 BUY | `QQQ` | $10.00 | $718.92 | QQQ muestra un fuerte momentum intradiario con un cambio de 1h del +1.28%, liderando el re... |
| `2026-10-19 01:50` | 🔴 SELL (+0.09$) | `ETH-USD` | $8.09 | $2428.97 | ETH-USD registra una ganancia acumulada y su RSI de 1 hora ha alcanzado 68.3, acercándose ... |
| `2026-10-19 01:00` | 🔴 SELL (-0.00$) | `SOL-USD` | $8.00 | $105.08 | SOL-USD ha entrado en sobrecompra con un RSI de 1 hora en 72.7, cumpliendo estrictamente c... |
| `2026-10-18 23:20` | 🟢 BUY | `SOL-USD` | $8.00 | $105.11 | SOL-USD presenta un RSI diario en 21.8 (sobreventa extrema) y un momentum de 24 horas alci... |

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
