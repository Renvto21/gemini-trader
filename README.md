# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 11:30:48`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$29.31 USD** | **$10.00 USD** | **$39.30 USD** | 🔴 **-1.74%** ($-0.70) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $346.04 | $10.00 | 📉 -0.03% | 40m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general se encuentra bajo presión bajista en la mayoría de los activos tecnológicos y criptomonedas, con múltiples índices y criptos mostrando RSI de 1 hora en niveles de sobreventa o cercanos a ella. Sin embargo, AAPL se mantiene fuerte con tendencia alcista sobre su SMA20 y un RSI diario saludable, consolidándose como nuestra única posición activa por el momento mientras el resto del mercado busca soporte."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 75%): AAPL mantiene una tendencia alcista sobre la SMA20, con un cambio de 24h positivo del 1.4% y un RSI de 1h en 66.6, cerca de la zona de sobrecompra donde buscaremos tomar ganancias. La posición lleva solo 40 minutos abierta y evoluciones favorables respaldan mantenerla.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Bitácora para el siguiente ciclo: Mantendré la posición abierta en AAPL, vigilando su aproximación al objetivo de take-profit en +2.5% o protegiendo con un stop-loss estricto en -1.5%. El efectivo restante de $29.31 se mantendrá en reserva temporalmente a la espera de confirmaciones de rebote en activos como QQQ o criptomonedas que muestren un RSI de 1 hora saliendo de sobreventa extrema con cambio positivo."
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
