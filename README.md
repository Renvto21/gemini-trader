# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 03:40:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$14.17 USD** | **$24.59 USD** | **$38.76 USD** | 🔴 **-3.11%** ($-1.24) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $539.44 | $6.55 | 📈 +0.80% | 16h 49m |
| `QQQ` | 0.013791 | $725.09 | $728.00 | $10.04 | 📈 +0.40% | 15h 20m |
| `NVDA` | 0.036812 | $217.32 | $217.23 | $8.00 | 📉 -0.04% | 14h 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "Los mercados de Wall Street se encuentran cerrados, por lo que las acciones (MSFT, QQQ, NVDA) tienen sus precios congelados. El sector cripto (SOL-USD, ETH-USD, BTC-USD) está abierto 24/7 con un comportamiento moderado. Nuestras posiciones actuales en acciones se mantienen estables pero sin alcanzar aún la zona de take-profit entre +2.0% y +3.5%, operando con ganancias mínimas en MSFT y QQQ, y ligeras pérdidas en NVDA."

**Operaciones del ciclo:**
- **[HOLD] MSFT** (Confianza: 80%): El mercado de acciones está cerrado. MSFT muestra una ganancia leve de 0.8% tras 16 horas de retención y se mantiene sobre su SMA20. Esperamos la apertura para buscar el take-profit.
- **[HOLD] QQQ** (Confianza: 80%): El mercado de acciones está cerrado. QQQ mantiene una ganancia marginal de 0.4% y no amerita venta anticipada al estar lejos del stop-loss y con precios congelados.
- **[HOLD] NVDA** (Confianza: 80%): El mercado de acciones está cerrado. NVDA registra una pérdida mínima de -0.04%, muy lejos del stop-loss de -2.0%, por lo que se mantiene hasta la apertura de mercado.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear la apertura de Wall Street para las posiciones abiertas (MSFT, QQQ, NVDA). Mantener las posiciones actuales ya que ninguna ha alcanzado el stop-loss de -2.0%. Esperar a la apertura para buscar la toma de ganancias si alcanzan el objetivo de +2.0% a +3.5% o rotar capital si pierden momentum."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **58** | 🎯 **41.4%** (24W / 20L / 14BE) | 🔴 **$-1.22 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-15 16:20` | 🔴 SELL (-0.10$) | `AAPL` | $9.90 | $342.86 | AAPL lleva más de un día abierta (1d 5h) sin mostrar un momentum significativo ni alcanzar... |
| `2026-10-15 12:50` | 🟢 BUY | `NVDA` | $8.00 | $217.32 | NVDA presenta un RSI de 1h en sobreventa extrema (21.5) con un inicio de recuperación en s... |
| `2026-10-15 12:20` | 🟢 BUY | `QQQ` | $10.00 | $725.09 | QQQ muestra un RSI de 1h en sobreventa extrema (28.7) cruzando al alza con un cambio posit... |
| `2026-10-15 12:10` | 🔴 SELL (+0.14$) | `ETH-USD` | $6.14 | $2417.73 | ETH-USD ha alcanzado un rendimiento del +2.33%, cumpliendo con el rango establecido para l... |
| `2026-10-15 11:50` | 🔴 SELL (+0.13$) | `SOL-USD` | $6.13 | $104.21 | SOL-USD ha alcanzado un rendimiento de +2.11%, cumpliendo con la regla de toma rápida de g... |

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
