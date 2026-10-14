# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 13:00:58`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.31 USD** | **$19.88 USD** | **$39.19 USD** | 🔴 **-2.02%** ($-0.81) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $344.92 | $9.96 | 📉 -0.36% | 2h 10m |
| `SOL-USD` | 0.095511 | $104.70 | $103.86 | $9.92 | 📉 -0.80% | 30m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sentimiento general bajista en gran parte de los activos tradicionales y criptomonedas, con múltiples índices y criptos cotizando por debajo de su SMA20 y presentando RSI de 1 hora extremadamente bajos en niveles de sobreventa profunda, lo que sugiere un posible escenario de rebote por reversión a la media pero con alta volatilidad."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 75%): AAPL se mantiene estable con un PnL de -0.36% y un RSI de 1h en 63.4, acercándose a la zona de sobrecompra para buscar el take-profit objetivo.
- **[HOLD] SOL-USD** (Confianza: 70%): SOL-USD muestra un RSI de 1h muy bajo (19.7) pero un cambio de 1h positivo, mantendremos la posición vigilando estrictamente el stop-loss de -2.0%.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos AAPL vigilando de cerca la zona de take-profit entre +2.0% y +3.5% ya que su RSI 1h se encuentra en 63.4. Mantendremos SOL-USD monitoreando su soporte a pesar de la debilidad macro, aplicando un stop-loss estricto a -2.0% si el impulso falla. Conservamos el efectivo disponible ($19.31) esperando una mayor confirmación de volumen antes de arriesgar capital adicional en nuevos activos."
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
