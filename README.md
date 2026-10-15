# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 16:50:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$14.17 USD** | **$24.60 USD** | **$38.76 USD** | 🔴 **-3.09%** ($-1.24) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $539.43 | $6.55 | 📈 +0.80% | 5h 59m |
| `QQQ` | 0.013791 | $725.09 | $728.21 | $10.04 | 📈 +0.43% | 4h 30m |
| `NVDA` | 0.036812 | $217.32 | $217.40 | $8.00 | 📈 +0.04% | 4h 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sesgo mixto con los índices tecnológicos principales (QQQ) y valores clave como NVDA operando bajo su media móvil de 20 días, aunque con indicadores de RSI de 1 hora en niveles de sobreventa extrema (NVDA en 18.0 y QQQ en 29.3), lo que presenta escenarios de rebote técnico inminentes. Las criptomonedas muestran signos de recuperación de corto plazo pero con alta volatilidad."

**Operaciones del ciclo:**
- **[HOLD] MSFT** (Confianza: 80%): MSFT se encuentra en tendencia alcista sobre su SMA20 con un PnL positivo de +0.8%. Se mantiene la posición en búsqueda del objetivo de take-profit entre +2.0% y +3.5%.
- **[HOLD] QQQ** (Confianza: 75%): QQQ mantiene su RSI de 1h en niveles bajos (29.3) y presenta un ligero PnL positivo. Esperando a que el momentum alcista se consolide para asegurar ganancias parciales.
- **[HOLD] NVDA** (Confianza: 70%): NVDA registra un RSI de 1h extremadamente deprimido en 18.0, lo que anticipa un posible rebote técnico fuerte por reversión a la media. Se le otorga este ciclo para mostrar tracción alcista.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en MSFT, QQQ y NVDA mientras se aproximan al rango objetivo de take-profit (+2.0% a +3.5%). NVDA mantiene un RSI de 1 hora extremadamente bajo (18.0), por lo que le daré este ciclo para reaccionar antes de considerar una rotación de capital. Vigilar estrictamente la liquidez disponible de $14.17 USD para buscar nuevas entradas agresivas si se rompen resistencias clave."
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
