# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 11:50:48`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$29.31 USD** | **$9.96 USD** | **$39.27 USD** | 🔴 **-1.83%** ($-0.73) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $344.82 | $9.96 | 📉 -0.38% | 1h 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un tono mayormente defensivo y bajista en el corto plazo, con los principales índices (QQQ, SPY, GLD) registrando descensos de 24 horas y RSI de 1 hora en zonas de sobreventa o cercanas a ella. Los activos cripto como BTC-USD, ETH-USD y SOL-USD continúan presionados a la baja sin mostrar aún un punto de inflexión confirmado. En renta variable, AAPL se mantiene relativamente estable dentro de nuestra cartera, aunque su impulso de la última hora se ha tornado ligeramente negativo (-0.34%) pero con un RSI de 1h en 62.4 que respalda la postura de retención a corto plazo."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 75%): La posición en AAPL lleva solo 1 hora abierta con una pérdida marginal de -0.38%. El RSI de 1 hora se encuentra en un nivel saludable de 62.4 y la tendencia diaria sigue siendo alcista por encima de la SMA20. Mantenemos la posición para permitir que alcance nuestro objetivo de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendré la posición abierta en AAPL bajo supervisión directa, vigilando que respete el soporte actual y se acerque al objetivo de take-profit entre +2.0% y +3.5%, o activando el stop-loss estricto si perfora niveles críticos. El efectivo disponible ($29.31) se mantiene temporalmente a la espera de que activos como BTC o ETH salgan de la sobreventa extrema en RSI de 1h y muestren una reversión clara de precio con un cambio de 1h positivo antes de reintentar una compra."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **51** | 🎯 **43.1%** (22W / 15L / 14BE) | 🔴 **$-0.59 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-14 11:20` | 🔴 SELL (-0.09$) | `BTC-USD` | $5.89 | $81874.95 | BTC-USD lleva más de 14 horas abierto con un PnL negativo persistente (-1.51%) y un RSI de... |
| `2026-10-14 10:50` | 🟢 BUY | `AAPL` | $10.00 | $346.15 | AAPL se encuentra con un excelente momentum alcista intradiario, un incremento de 1.4% en ... |
| `2026-10-14 10:10` | 🔴 SELL (-0.11$) | `SOL-USD` | $5.89 | $105.41 | La posición en SOL-USD acumula una pérdida cercana al -1.9%, rozando nuestro stop-loss est... |
| `2026-10-14 02:50` | 🔴 SELL (-0.01$) | `ETH-USD` | $4.99 | $2502.14 | ETH-USD lleva más de 9 horas de holding con PnL plano (-0.25%) y un RSI de 1H en 42.3 sin ... |
| `2026-10-13 23:11` | 🟢 BUY | `SOL-USD` | $6.00 | $107.45 | SOL-USD presenta un RSI diario en niveles de sobreventa extrema (28.3) y muestra un sólido... |

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
