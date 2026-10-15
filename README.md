# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 20:00:50`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$14.17 USD** | **$24.59 USD** | **$38.76 USD** | 🔴 **-3.11%** ($-1.24) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $539.44 | $6.55 | 📈 +0.80% | 9h 10m |
| `QQQ` | 0.013791 | $725.09 | $728.00 | $10.04 | 📈 +0.40% | 7h 40m |
| `NVDA` | 0.036812 | $217.32 | $217.23 | $8.00 | 📉 -0.04% | 7h 10m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "Los mercados bursátiles tradicionales (QQQ, MSFT, NVDA) se encuentran cerrados, con sus precios congelados. Por lo tanto, de acuerdo con la estrategia operativa, la liquidez activa debe enfocarse en los mercados de criptomonedas que operan 24/7. En cripto, ETH-USD muestra un RSI de 1h en sobrecompra (72.1), lo que indica agotamiento del impulso alcista local, mientras que SOL-USD y BTC-USD muestran consolidación con RSI cercanos a 60-65 sin una señal clara de entrada por rebote extremo. Las posiciones actuales en cartera (MSFT, QQQ, NVDA) están en modo HOLD debido al cierre de mercado, a la espera de la apertura para asegurar ganancias si alcanzan el objetivo de +2.0% o cortar pérdidas si rompen soportes."

**Operaciones del ciclo:**
- **[HOLD] MSFT** (Confianza: 80%): El mercado de Wall Street está cerrado. La posición se mantiene con una ganancia ligera del 0.8% esperando la apertura para buscar el objetivo de take-profit.
- **[HOLD] QQQ** (Confianza: 80%): Mercado cerrado. La posición se mantiene en HOLD a la espera de la recuperación del índice en la siguiente sesión.
- **[HOLD] NVDA** (Confianza: 75%): Mercado cerrado. PnL neutral (-0.04%), se mantiene a la espera de la reacción del precio tras el fuerte RSI de sobreventa previo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener posiciones abiertas en MSFT, QQQ y NVDA hasta la apertura de Wall Street para buscar la toma de beneficios en el rango de +2.0% a +3.5%. En el sector cripto, mantenerse en observación sin forzar entradas ya que ETH está en sobrecompra y SOL/BTC no muestran divergencias de sobreventa para un mean reversion agresivo. Vigilar la liquidez de reserva de $14.17 USD."
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
