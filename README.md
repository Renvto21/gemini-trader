# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 12:21:02`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$28.57 USD** | **$10.05 USD** | **$38.62 USD** | 🔴 **-3.46%** ($-1.38) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $722.69 | $10.05 | 📈 +0.52% | 1h 40m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado se encuentra en una fase de consolidación de corto plazo con la mayoría de los activos tecnológicos y criptomonedas operando en tendencias bajistas generales bajo sus medias móviles de 20 periodos, aunque muestran ligeros intentos de estabilización intradiaria. QQQ se mantiene en cartera con una ganancia marginal, pero su momentum se ha ralentizado (RSI 1h en 47.6). No hay señales de sobrecompra para tomar take-profit ni tampoco condiciones de ruptura de stop-loss, por lo que optamos por la paciencia táctica manteniendo la posición actual."

**Operaciones del ciclo:**
- **[HOLD] QQQ** (Confianza: 70%): La posición en QQQ registra una ganancia moderada del +0.52% tras 1h 40m. No ha alcanzado el objetivo de take-profit (+2.0% a +3.5%) ni ha activado el stop-loss (-2.0%). Mantenemos la operación abierta para permitir que el rebote intradiario continúe desarrollándose sin realizar movimientos prematuros.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos la posición abierta en QQQ, vigilando de cerca si logra retomar fuerza alcista o si se estanca. El take-profit sigue fijado entre +2.0% y +3.5%, y el stop-loss estricto en -2.0%. Mantendremos la liquidez en reserva para buscar nuevas oportunidades de rebote en criptoactivos (como ETH-USD o SOL-USD) o en tecnológicas de alto beta si el RSI de 1 hora desciende a zonas de sobreventa extrema (< 35) en los próximos ciclos."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **77** | 🎯 **42.9%** (33W / 29L / 15BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-19 10:40` | 🟢 BUY | `QQQ` | $10.00 | $718.92 | QQQ muestra un fuerte momentum intradiario con un cambio de 1h del +1.28%, liderando el re... |
| `2026-10-19 01:50` | 🔴 SELL (+0.09$) | `ETH-USD` | $8.09 | $2428.97 | ETH-USD registra una ganancia acumulada y su RSI de 1 hora ha alcanzado 68.3, acercándose ... |
| `2026-10-19 01:00` | 🔴 SELL (-0.00$) | `SOL-USD` | $8.00 | $105.08 | SOL-USD ha entrado en sobrecompra con un RSI de 1 hora en 72.7, cumpliendo estrictamente c... |
| `2026-10-18 23:20` | 🟢 BUY | `SOL-USD` | $8.00 | $105.11 | SOL-USD presenta un RSI diario en 21.8 (sobreventa extrema) y un momentum de 24 horas alci... |
| `2026-10-18 23:10` | 🔴 SELL (+0.17$) | `SOL-USD` | $8.17 | $105.19 | SOL-USD acumula una ganancia del +2.12%, cumpliendo con la regla de toma rápida de gananci... |

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
