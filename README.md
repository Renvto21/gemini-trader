# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 13:20:54`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.95 USD** | **$39.07 USD** | 🔴 **-2.32%** ($-0.93) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $340.54 | $10.00 | 📉 -0.03% | 1h 19m |
| `GLD` | 0.026337 | $379.70 | $377.90 | $9.95 | 📉 -0.47% | 1h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado se encuentra mixto con sesgo bajista general en temporalidades diarias, aunque algunos activos muestran oportunidades de rebote por sobreventa en corto plazo. GLD ha profundizado su caída con un RSI de 1 hora en 28.5, cumpliendo nuestra zona de entrada para rebote técnico, mientras que AAPL se mantiene estable con un ligero incremento en su RSI de 1 hora a 33.7."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 75%): La posición en AAPL tiene un holding time de poco más de una hora y una pérdida marginal de -0.03%. Mantiene tendencia alcista diaria y un RSI de 1 hora en 33.7, por lo que esperamos que desarrolle el rebote hacia nuestro objetivo de take-profit.
- **[HOLD] GLD** (Confianza: 75%): GLD registra un RSI de 1 hora en 28.5 (sobreventa extrema) y una pérdida no realizada de -0.47%. Dado que aún no activa el stop-loss estricto de -2.0%, mantendremos la posición para capturar el esperado rebote técnico de reversión a la media.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos AAPL y GLD por el momento, ya que el holding time sigue siendo corto (poco más de una hora) y no han alcanzado nuestro stop-loss de -2.0% ni el take-profit del +2.0% al +3.5%. Estaremos vigilando de cerca el RSI de GLD para asegurar ganancias rápidas si rebota, o cortar pérdidas estrictamente si perfora el soporte."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **81** | 🎯 **44.4%** (36W / 30L / 15BE) | 🔴 **$-0.74 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-20 12:01` | 🟢 BUY | `GLD` | $10.00 | $379.70 | GLD presenta un RSI de 1 hora en 31.4, acercándose a la zona ideal de sobreventa para acti... |
| `2026-10-20 12:01` | 🟢 BUY | `AAPL` | $10.00 | $340.64 | AAPL se encuentra en tendencia alcista diaria con un RSI de 1 hora en 33.1 (cercano a sobr... |
| `2026-10-20 11:10` | 🔴 SELL (+0.12$) | `BTC-USD` | $8.69 | $82949.93 | BTC-USD muestra un RSI de 1 hora en 72.2 (sobrecompra) y un rendimiento positivo de +1.45%... |
| `2026-10-20 11:10` | 🔴 SELL (+0.28$) | `SOL-USD` | $10.28 | $107.08 | SOL-USD registra un excelente rendimiento de +2.83% con un RSI de 1 hora en sobrecompra (7... |
| `2026-10-20 11:10` | 🔴 SELL (+0.23$) | `ETH-USD` | $10.23 | $2449.11 | ETH-USD ha alcanzado un PnL de +2.32% y su RSI de 1 hora ha tocado el nivel de sobrecompra... |

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
