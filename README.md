# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 00:20:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$14.17 USD** | **$24.59 USD** | **$38.76 USD** | 🔴 **-3.11%** ($-1.24) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $539.44 | $6.55 | 📈 +0.80% | 13h 29m |
| `QQQ` | 0.013791 | $725.09 | $728.00 | $10.04 | 📈 +0.40% | 11h 59m |
| `NVDA` | 0.036812 | $217.32 | $217.23 | $8.00 | 📉 -0.04% | 11h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado bursátil de Wall Street se encuentra actualmente CERRADO, manteniendo congelados los precios y con baja actividad en activos tradicionales. En contraste, las criptomonedas operan 24/7 y muestran niveles elevados de RSI de 1h en zona de sobrecompra (ETH-USD en 79.6, SOL-USD en 75.1 y BTC-USD en 72.6), lo que indica agotamiento del impulso alcista de corto plazo tras los rebotes recientes. Las posiciones actuales de MSFT, QQQ y NVDA se mantienen en portafolio esperando la apertura del mercado bursátil."

**Operaciones del ciclo:**
- *Sin cambios en este ciclo (HOLD)*

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas de MSFT, QQQ y NVDA hasta la apertura de Wall Street para evaluar la toma de beneficios si alcanzan el rango de +2.0% a +3.5% o ejecutar stop-loss si el precio quiebra soportes clave. En el sector cripto, se observa sobrecompra intradiaria (RSI 1h > 70); esperaremos a que los indicadores se enfríen por debajo de 50 para buscar nuevas oportunidades de entrada bajo la estrategia de mean reversion."
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
