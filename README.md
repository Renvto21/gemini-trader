# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 11:10:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$23.41 USD** | **$15.87 USD** | **$39.29 USD** | 🔴 **-1.79%** ($-0.71) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000072 | $83128.62 | $82150.85 | $5.93 | 📉 -1.18% | 14h 9m |
| `AAPL` | 0.028889 | $346.15 | $344.20 | $9.94 | 📉 -0.56% | 20m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado accionario de EE.UU. y los índices principales (QQQ, SPY) muestran debilidad general con caídas de corto plazo, pero activos como AAPL mantienen un comportamiento defensivo y alcista sobre su SMA20. En criptomonedas, BTC-USD y ETH-USD presentan lecturas de sobreventa extrema en el RSI de 1 hora, anticipando posibles rebotes tácticos por reversión a la media, aunque la tendencia macro sigue siendo bajista."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 85%): AAPL mantiene un excelente momentum alcista intradiario con un RSI de 1h en 58.1 y tendencia por encima de la SMA20. La posición lleva poco tiempo abierta y se encuentra dentro de los parámetros esperados de crecimiento, por lo que conservamos la inversión para buscar el objetivo de take-profit.
- **[HOLD] BTC-USD** (Confianza: 75%): BTC-USD presenta un RSI de 1h en sobreventa extrema (28.6). Aunque lleva más de 14 horas abierto con un PnL ligeramente negativo (-1.18%), el nivel técnico sugiere que un rebote por reversión a la media es inminente. Mantendremos la posición vigilando de cerca el stop-loss.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendré la posición en AAPL buscando su objetivo de take-profit en +2.5% y protegiendo con stop-loss en -1.5%. Para BTC-USD, el tiempo abierto supera las 14 horas con un rendimiento ligeramente negativo (-1.18%) y un RSI de 1h en 28.6; vigilaré de cerca si consolida el rebote o si rompe la zona de soporte para rotar el capital. Mantendré la reserva de efectivo requerida y buscaré oportunidades agresivas exclusivamente en activos con momentum alcista."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **50** | 🎯 **44.0%** (22W / 14L / 14BE) | 🔴 **$-0.50 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-14 10:50` | 🟢 BUY | `AAPL` | $10.00 | $346.15 | AAPL se encuentra con un excelente momentum alcista intradiario, un incremento de 1.4% en ... |
| `2026-10-14 10:10` | 🔴 SELL (-0.11$) | `SOL-USD` | $5.89 | $105.41 | La posición en SOL-USD acumula una pérdida cercana al -1.9%, rozando nuestro stop-loss est... |
| `2026-10-14 02:50` | 🔴 SELL (-0.01$) | `ETH-USD` | $4.99 | $2502.14 | ETH-USD lleva más de 9 horas de holding con PnL plano (-0.25%) y un RSI de 1H en 42.3 sin ... |
| `2026-10-13 23:11` | 🟢 BUY | `SOL-USD` | $6.00 | $107.45 | SOL-USD presenta un RSI diario en niveles de sobreventa extrema (28.3) y muestra un sólido... |
| `2026-10-13 21:00` | 🟢 BUY | `BTC-USD` | $6.00 | $83128.62 | BTC-USD muestra un RSI de 1H en 31.7 aproximándose a niveles de sobreventa y un cambio pos... |

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
