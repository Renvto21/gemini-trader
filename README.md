# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 14:10:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.31 USD** | **$19.97 USD** | **$39.28 USD** | 🔴 **-1.81%** ($-0.72) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $344.06 | $9.94 | 📉 -0.60% | 3h 20m |
| `SOL-USD` | 0.095511 | $104.70 | $105.00 | $10.03 | 📈 +0.29% | 1h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado se encuentra en un contexto mayormente bajista con la mayoría de los índices y activos cotizando por debajo de su SMA20 y presentando RSI diarios débiles o en zonas de sobreventa. Sin embargo, AAPL se mantiene fuerte con tendencia alcista y un RSI de 1h en 62.4, mientras que SOL-USD muestra indicios de consolidación y soporte tras haber salido de sobreventa extrema en ciclos anteriores. La liquidez disponible es reducida, por lo que la gestión actual se centra en proteger posiciones con momentum y mantener la disciplina táctica."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 80%): AAPL mantiene una tendencia alcista firme sobre la SMA20 y un RSI de 1h en 62.4, mostrando resiliencia frente al contexto bajista general. Se mantiene la posición para buscar acercarse a la zona de take-profit cerca de sobrecompra.
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD se mantiene estable con una pequeña ganancia tras el rebote inicial. Se conserva la posición vigilando de cerca el soporte y esperando un incremento adicional en el momentum intradiario.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener la posición de SOL-USD y vigilar su comportamiento en torno al soporte actual, estableciendo un stop-loss estricto si pierde el nivel de entrada. Monitorear de cerca a AAPL para asegurar beneficios si el RSI de 1h se aproxima a la zona de sobrecompra (>70). Mantener una reserva de efectivo estricta y buscar nuevas oportunidades de rebote intradiario solo si se confirma un cambio claro de tendencia."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **51** | 🎯 **43.1%** (22W / 15L / 14BE) | 🔴 **$-0.59 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-14 12:30` | 🟢 BUY | `SOL-USD` | $10.00 | $104.70 | SOL-USD presenta un RSI de 1h en 29.2 saliendo de sobreventa extrema y un cambio de 1h pos... |
| `2026-10-14 11:20` | 🔴 SELL (-0.09$) | `BTC-USD` | $5.89 | $81874.95 | BTC-USD lleva más de 14 horas abierto con un PnL negativo persistente (-1.51%) y un RSI de... |
| `2026-10-14 10:50` | 🟢 BUY | `AAPL` | $10.00 | $346.15 | AAPL se encuentra con un excelente momentum alcista intradiario, un incremento de 1.4% en ... |
| `2026-10-14 10:10` | 🔴 SELL (-0.11$) | `SOL-USD` | $5.89 | $105.41 | La posición en SOL-USD acumula una pérdida cercana al -1.9%, rozando nuestro stop-loss est... |
| `2026-10-14 02:50` | 🔴 SELL (-0.01$) | `ETH-USD` | $4.99 | $2502.14 | ETH-USD lleva más de 9 horas de holding con PnL plano (-0.25%) y un RSI de 1H en 42.3 sin ... |

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
