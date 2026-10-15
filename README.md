# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 14:30:50`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.26 USD** | **$34.49 USD** | **$38.75 USD** | 🔴 **-3.11%** ($-1.25) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $344.43 | $9.95 | 📉 -0.50% | 1d 3h |
| `MSFT` | 0.012146 | $535.17 | $538.93 | $6.55 | 📈 +0.70% | 3h 40m |
| `QQQ` | 0.013791 | $725.09 | $724.60 | $9.99 | 📉 -0.07% | 2h 10m |
| `NVDA` | 0.036812 | $217.32 | $217.40 | $8.00 | 📈 +0.04% | 1h 40m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un entorno mixto con presión bajista en gran parte de los índices y tecnológicas (QQQ, NVDA), aunque con indicadores de RSI de 1 hora en niveles de sobreventa extrema que sugieren oportunidades inminentes de rebote (mean reversion). Por otro lado, los criptoactivos (BTC-USD, SOL-USD, ETH-USD) se mantienen abiertos 24/7 con un momentum positivo constante y RSI al alza, destacando como alternativas óptimas para la rotación y captura rápida de beneficios."

**Operaciones del ciclo:**
- **[HOLD] MSFT** (Confianza: 80%): MSFT se encuentra en tendencia alcista con un rendimiento positivo de +0.7% y un RSI diario fuerte en 66.0. Mantenemos la posición a la espera de alcanzar el objetivo de take-profit entre +2.0% y +3.5%.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales (AAPL, MSFT, QQQ, NVDA) vigilando estrictamente el stop-loss en -2.0% y el objetivo de take-profit entre +2.0% y +3.5%. Dado que el efectivo es muy bajo ($4.26 USD), el plan táctico para el próximo ciclo es esperar la toma de ganancias en MSFT o AAPL para liberar liquidez y ejecutar compras en criptoactivos con momentum favorable si continúan con buen rendimiento."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **57** | 🎯 **42.1%** (24W / 19L / 14BE) | 🔴 **$-1.12 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-15 12:50` | 🟢 BUY | `NVDA` | $8.00 | $217.32 | NVDA presenta un RSI de 1h en sobreventa extrema (21.5) con un inicio de recuperación en s... |
| `2026-10-15 12:20` | 🟢 BUY | `QQQ` | $10.00 | $725.09 | QQQ muestra un RSI de 1h en sobreventa extrema (28.7) cruzando al alza con un cambio posit... |
| `2026-10-15 12:10` | 🔴 SELL (+0.14$) | `ETH-USD` | $6.14 | $2417.73 | ETH-USD ha alcanzado un rendimiento del +2.33%, cumpliendo con el rango establecido para l... |
| `2026-10-15 11:50` | 🔴 SELL (+0.13$) | `SOL-USD` | $6.13 | $104.21 | SOL-USD ha alcanzado un rendimiento de +2.11%, cumpliendo con la regla de toma rápida de g... |
| `2026-10-15 10:50` | 🟢 BUY | `MSFT` | $6.50 | $535.17 | MSFT presenta un RSI de 1h ultra comprimido en sobreventa extrema (14.7) con un cambio pos... |

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
