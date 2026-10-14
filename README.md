# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 11:20:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$29.31 USD** | **$9.97 USD** | **$39.28 USD** | 🔴 **-1.80%** ($-0.72) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $345.26 | $9.97 | 📉 -0.26% | 30m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general muestra un sentimiento predominantemente bajista de corto plazo con la mayoría de los índices y activos principales cotizando bajo su SMA20 y presentando caídas en la última hora. Sin embargo, AAPL se mantiene fuerte con tendencia alcista sobre la SMA20 y un momentum positivo continuo, resistiendo la debilidad general. Por otro lado, BTC-USD muestra un holding prolongado cercano a las 15 horas con un PnL negativo de -1.51% y un RSI de 1h en 26.1, lo que indica que el rebote esperado no se ha consolidado de manera efectiva."

**Operaciones del ciclo:**
- **[SELL] BTC-USD** (Confianza: 85%): BTC-USD lleva más de 14 horas abierto con un PnL negativo persistente (-1.51%) y un RSI de 1h en 26.1 sin consolidar el rebote esperado. Siguiendo la regla de rotación de capital y gestión de posiciones estancadas, cerramos la operación para proteger el capital y evitar pérdidas mayores.
- **[HOLD] AAPL** (Confianza: 80%): AAPL mantiene una excelente estructura alcista sobre la SMA20, con un incremento de 1.14% en la última hora y un RSI diario saludable de 59.9. Mantenemos la posición buscando alcanzar el objetivo de take-profit entre +2.0% y +3.5%.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Bitácora para el siguiente ciclo: Mantendré la posición en AAPL buscando su objetivo de take-profit en +2.5% y protegiendo con stop-loss en -1.5%. En cuanto a BTC-USD, dado el tiempo prolongado sin mostrar la fuerza de rebote esperada y su persistencia en terreno negativo, he decidido liquidar la posición para rotar el capital hacia liquidez o buscar un nuevo activo con mayor dinamismo alcista. Vigilaré las oportunidades en cripto o activos tecnológicos que presenten rupturas claras con RSI saliendo de sobreventa extrema."
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
