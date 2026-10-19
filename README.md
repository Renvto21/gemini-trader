# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 13:20:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.57 USD** | **$20.08 USD** | **$38.64 USD** | 🔴 **-3.40%** ($-1.36) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $721.95 | $10.04 | 📈 +0.42% | 2h 40m |
| `ETH-USD` | 0.004178 | $2393.62 | $2401.77 | $10.03 | 📈 +0.34% | 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sentimiento mixto con ligera tendencia bajista en gráficos diarios, pero con algunos activos tecnológicos y criptomonedas intentando consolidar rebotes de corto plazo. QQQ y ETH-USD se mantienen en nuestras posiciones con ganancias marginales (+0.42% y +0.34% respectivamente), operando aún por debajo de nuestras metas de take-profit entre +2.0% y +3.5%. Mantenemos la cautela y la liquidez disponible para reaccionar ante cualquier cambio abrupto en el momentum."

**Operaciones del ciclo:**
- **[HOLD] QQQ** (Confianza: 70%): La posición en QQQ lleva poco tiempo abierta (2h 39m) y muestra una ganancia leve del +0.42%. El RSI de 1 hora se encuentra neutral en 48.9 y el activo sigue buscando consolidar su rebote. Mantenemos la posición a la espera del objetivo de take-profit.
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD presenta una ganancia del +0.34% tras un breve periodo en cartera (29m). Su RSI de 1 hora ha subido a 39.0 desde la zona de sobreventa, indicando que el rebote técnico sigue su curso previsto. Mantenemos la posición para buscar el objetivo de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales en QQQ y ETH-USD esperando que alcancen el objetivo de take-profit en el rango de +2.0% a +3.5%. Establecemos stop-loss estricto si alguna posición cae por debajo de -2.0%. En el próximo ciclo evaluaremos la rotación de capital si el momentum intradiario se desacelera o si surge una oportunidad más clara en activos con mayor fuerza relativa."
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
