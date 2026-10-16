# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 23:30:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$14.17 USD** | **$24.59 USD** | **$38.76 USD** | 🔴 **-3.11%** ($-1.24) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $539.44 | $6.55 | 📈 +0.80% | 12h 39m |
| `QQQ` | 0.013791 | $725.09 | $728.00 | $10.04 | 📈 +0.40% | 11h 9m |
| `NVDA` | 0.036812 | $217.32 | $217.23 | $8.00 | 📉 -0.04% | 10h 40m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado bursátil de Wall Street se encuentra actualmente CERRADO, por lo que las posiciones en acciones (MSFT, QQQ, NVDA) permanecen con precios congelados y sin actividad inmediata. Por otro lado, las criptomonedas operan 24/7 y muestran un sesgo moderado alcista en las últimas 24 horas (ETH-USD y SOL-USD con 0.73% y 1.09% respectivamente), aunque sus indicadores de RSI en 1 hora se acercan a zonas de sobrecompra (~69) y sus tendencias diarias siguen bajo la SMA20. Dado que las posiciones actuales en acciones no han alcanzado el objetivo de take-profit entre +2.0% y +3.5%, y que el efectivo disponible es limitado a $14.17 USD, la estrategia óptima para este ciclo es mantener las posiciones actuales a la espera de la apertura de los mercados tradicionales y conservar la liquidez sin forzar entradas en criptomonedas."

**Operaciones del ciclo:**
- **[HOLD] MSFT** (Confianza: 80%): El mercado de Wall Street está cerrado y la posición muestra una ganancia leve del 0.8%, manteniéndose por debajo del objetivo de take-profit de +2.0% a +3.5%. Se mantiene para esperar la apertura.
- **[HOLD] QQQ** (Confianza: 80%): Activo cerrado. La posición se encuentra estable con una pequeña ganancia de 0.4% y un holding time de 11 horas, esperando la apertura para buscar la salida objetivo.
- **[HOLD] NVDA** (Confianza: 80%): Mercado cerrado. La posición se mantiene prácticamente plana (-0.04%) esperando la volatilidad de la sesión regular para buscar el rebote técnico esperado.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas de MSFT, QQQ y NVDA hasta la apertura de Wall Street para buscar la toma de beneficios si alcanzan el rango de +2.0% a +3.5% o cortar pérdidas estrictamente si bajan del -2.0%. Vigilar de cerca el comportamiento de ETH-USD y SOL-USD por si se presenta una corrección técnica intradía que permita una entrada de rebote de alta convicción con el efectivo disponible."
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
