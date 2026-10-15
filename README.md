# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 18:10:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$14.17 USD** | **$24.59 USD** | **$38.76 USD** | 🔴 **-3.11%** ($-1.24) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $539.44 | $6.55 | 📈 +0.80% | 7h 19m |
| `QQQ` | 0.013791 | $725.09 | $728.00 | $10.04 | 📈 +0.40% | 5h 50m |
| `NVDA` | 0.036812 | $217.32 | $217.23 | $8.00 | 📉 -0.04% | 5h 20m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de valores tradicional (Wall Street) se encuentra actualmente CERRADO, manteniendo los precios congelados para activos como MSFT, QQQ y NVDA, los cuales muestran un comportamiento estable con pequeñas ganancias latentes en MSFT y QQQ. En el sector cripto (abierto 24/7), SOL-USD y ETH-USD muestran un leve impulso alcista, aunque ETH-USD presenta un RSI de 1h en sobrecompra (72.0), lo que sugiere cautela para nuevas entradas inmediatas."

**Operaciones del ciclo:**
- **[HOLD] MSFT** (Confianza: 80%): La posición en MSFT se mantiene abierta con una ganancia latente de +0.8% en un mercado cerrado. Esperando la apertura de Wall Street para buscar el objetivo de take-profit entre +2.0% y +3.5%.
- **[HOLD] QQQ** (Confianza: 80%): QQQ se mantiene con una ganancia ligera del +0.4% mientras el mercado está cerrado. Se conserva para buscar mayores beneficios tras la apertura de la sesión.
- **[HOLD] NVDA** (Confianza: 75%): NVDA se encuentra practicamente plana (-0.04%) con el mercado cerrado, respetando la estructura del rebote técnico iniciado tras la sobreventa extrema previa. Se mantiene a la espera de la apertura.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en MSFT, QQQ y NVDA ya que Wall Street está cerrado y muestran un comportamiento técnico favorable para buscar take-profit en el rango de +2.0% a +3.5% una vez reabra el mercado. En cripto, vigilar un retroceso en ETH-USD tras su sobrecompra en 1h y buscar oportunidades de rebote en SOL-USD si confirma soporte. Mantener la reserva de efectivo por encima del mínimo de $4.00 USD."
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
