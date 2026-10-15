# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 13:40:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.26 USD** | **$34.45 USD** | **$38.71 USD** | 🔴 **-3.22%** ($-1.29) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $344.22 | $9.94 | 📉 -0.56% | 1d 2h |
| `MSFT` | 0.012146 | $535.17 | $539.65 | $6.55 | 📈 +0.84% | 2h 49m |
| `QQQ` | 0.013791 | $725.09 | $723.38 | $9.98 | 📉 -0.24% | 1h 20m |
| `NVDA` | 0.036812 | $217.32 | $216.61 | $7.97 | 📉 -0.33% | 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de Wall Street se encuentra abierto pero operando con cautela y una tendencia general bajista a mediano plazo (por debajo de las SMA20). Sin embargo, se observan oportunidades claras de sobreventa extrema en activos tecnológicos como QQQ (rsi_1h en 22.7) y NVDA (rsi_1h en 19.7), lo cual presenta escenarios ideales para capturar rebotes técnicos por reversión a la media. La liquidez de la cuenta se mantiene ajustada con un remanente en efectivo mínimo de $4.26 USD, operando de manera altamente eficiente."

**Operaciones del ciclo:**
- **[HOLD] MSFT** (Confianza: 80%): MSFT mantiene una rentabilidad positiva de +0.84% y tendencia alcista sobre la SMA20. Se mantiene en cartera a la espera de alcanzar el objetivo de take-profit entre +2.0% y +3.5%.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener la vigilancia estricta sobre QQQ y NVDA, esperando que sus RSI de 1 hora rompan al alza para asegurar ganancias rápidas si alcanzan el rango de +2.0% a +3.5%, o activar el stop-loss si se acercan al umbral de pérdida del -2.0%. Monitorear a MSFT y AAPL; MSFT se encuentra cerca del objetivo de toma de ganancias (+0.84%). Si el mercado muestra debilidad adicional, rotar el capital hacia criptomonedas o recortar posiciones estancadas."
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
