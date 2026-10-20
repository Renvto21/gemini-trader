# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 13:11:01`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.96 USD** | **$39.09 USD** | 🔴 **-2.28%** ($-0.91) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $340.61 | $10.00 | 📉 -0.01% | 1h 9m |
| `GLD` | 0.026337 | $379.70 | $378.38 | $9.97 | 📉 -0.35% | 1h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado se encuentra mixto con Wall Street abierto. Las posiciones abiertas en AAPL y GLD muestran un comportamiento lateral con ligeras fluctuaciones tras 1 hora de tenencia. GLD mantiene un RSI de 1 hora en 30.1, cerca de la zona de sobreventa extrema, esperando el rebote técnico. AAPL muestra un RSI de 1 hora en 34.0 con un cambio positivo de 0.07%, manteniendo la estructura alcista en temporalidad diaria."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 70%): AAPL mantiene una tendencia alcista diaria sobre su SMA20 y un RSI de 1 hora en 34.0 con un ligero cambio positivo de 0.07%. Mantenemos la posición para permitir que desarrolle el rebote técnico esperado.
- **[HOLD] GLD** (Confianza: 70%): GLD presenta un RSI de 1 hora en 30.1, encontrándose en el umbral ideal de sobreventa. Mantenemos la posición a la espera de que se active el rebote técnico hacia la zona objetivo de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones en AAPL y GLD durante este ciclo ya que el holding time es bajo y no han alcanzado ningún stop-loss ni take-profit. Monitorearemos de cerca el RSI de 1 hora en GLD (30.1) y el cambio de momentum en AAPL buscando el objetivo de take-profit entre +2.0% y +3.5%. Si alguna posición perfora el soporte o cae más de -2.0%, ejecutaremos la venta inmediata."
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
