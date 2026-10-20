# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 13:01:20`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.98 USD** | **$39.10 USD** | 🔴 **-2.24%** ($-0.90) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $341.00 | $10.01 | 📈 +0.11% | 59m |
| `GLD` | 0.026337 | $379.70 | $378.61 | $9.97 | 📉 -0.29% | 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un comportamiento mixto con un sesgo ligeramente defensivo. Las posiciones actuales en AAPL y GLD se mantienen estables con ligeras variaciones, mientras que los activos cripto muestran un impulso moderado pero sin la fuerza necesaria para forzar una rotación inmediata en este ciclo. Continuamos operando bajo la disciplina de mantener reservas mínimas y proteger el capital."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 80%): AAPL mantiene una tendencia diaria alcista sobre la SMA20 y un RSI de 1 hora en recuperacion (35.7). El PnL es ligeramente positivo (+0.11%) y lleva poco tiempo en cartera, por lo que esperamos el desarrollo del rebote técnico.
- **[HOLD] GLD** (Confianza: 80%): GLD se encuentra en una zona de sobreventa de corto plazo con un RSI de 1 hora en 30.9. Aunque registra una pequeña perdida de -0.29%, el nivel respeta la estrategia de mean reversion y esperamos que busque el objetivo de ganancia en los siguientes ciclos.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones en AAPL y GLD durante este ciclo ya que el holding time es bajo (59 minutos) y no han tocado ningún stop-loss ni take-profit objetivo. Seguiremos vigilando el rsi_1h de GLD (actualmente en 30.9) esperando el rebote técnico hacia la zona de take-profit de +2.0% a +3.5%. Si alguna posición perfora el soporte o cae más de -2.0%, ejecutaremos la venta inmediata."
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
