# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 15:30:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$29.23 USD** | **$9.91 USD** | **$39.14 USD** | 🔴 **-2.16%** ($-0.86) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.99 | $9.91 | 📉 -0.91% | 4h 40m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sesgo general bajista en la mayoría de los activos (bajo sus SMA20), con condiciones de sobreventa extrema en varias criptomonedas y ETFs (RSI de 1h por debajo de 25). Sin embargo, AAPL se mantiene estable con tendencia alcista y un RSI de 1h en 56.5, operando cerca de nuestro precio de entrada pero sin alcanzar aún el objetivo de take-profit. La liquidez se mantiene sólida con $29.23 USD listos para ser desplegados ante cualquier confirmación de rebote en los activos abiertos 24/7."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 70%): La posición en AAPL lleva 4h 40m abierta con una pérdida menor de -0.91%. Su tendencia es alcista sobre la SMA20 y el RSI de 1h está en 56.5, lo cual indica que mantiene estabilidad. Esperaremos a que alcance el rango de take-profit (+2.0% a +3.5%) o se acerque a la sobrecompra para asegurar ganancias.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendré la posición de AAPL vigilando de cerca que el RSI de 1h no caiga por debajo de 45 y buscando el objetivo de take-profit entre +2.0% y +3.5% o salida por sobrecompra (>70). Dado que los activos cripto como BTC-USD y SOL-USD se encuentran en sobreventa extrema pero sin un cambio de 1h positivo confirmado, esperaré a que el RSI de 1h cruce al alza junto con un cambio de 1h positivo antes de arriesgar capital en ellos. Mantendré la disciplina en el stop-loss estricto (-2.0%) para AAPL."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **52** | 🎯 **42.3%** (22W / 16L / 14BE) | 🔴 **$-0.67 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-14 15:20` | 🔴 SELL (-0.08$) | `SOL-USD` | $9.92 | $103.86 | SOL-USD lleva varias horas sin mostrar el rebote esperado, su RSI de 1h ha caído hasta 25.... |
| `2026-10-14 12:30` | 🟢 BUY | `SOL-USD` | $10.00 | $104.70 | SOL-USD presenta un RSI de 1h en 29.2 saliendo de sobreventa extrema y un cambio de 1h pos... |
| `2026-10-14 11:20` | 🔴 SELL (-0.09$) | `BTC-USD` | $5.89 | $81874.95 | BTC-USD lleva más de 14 horas abierto con un PnL negativo persistente (-1.51%) y un RSI de... |
| `2026-10-14 10:50` | 🟢 BUY | `AAPL` | $10.00 | $346.15 | AAPL se encuentra con un excelente momentum alcista intradiario, un incremento de 1.4% en ... |
| `2026-10-14 10:10` | 🔴 SELL (-0.11$) | `SOL-USD` | $5.89 | $105.41 | La posición en SOL-USD acumula una pérdida cercana al -1.9%, rozando nuestro stop-loss est... |

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
