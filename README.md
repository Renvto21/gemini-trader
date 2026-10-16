# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 06:50:50`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.17 USD** | **$34.59 USD** | **$38.75 USD** | 🔴 **-3.11%** ($-1.25) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $539.44 | $6.55 | 📈 +0.80% | 20h 0m |
| `QQQ` | 0.013791 | $725.09 | $728.00 | $10.04 | 📈 +0.40% | 18h 30m |
| `NVDA` | 0.036812 | $217.32 | $217.23 | $8.00 | 📉 -0.04% | 18h 0m |
| `ETH-USD` | 0.002855 | $2451.90 | $2450.95 | $7.00 | 📉 -0.04% | 2h 19m |
| `SOL-USD` | 0.028214 | $106.33 | $106.39 | $3.00 | 📈 +0.06% | 1h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado accionario de Wall Street se encuentra CERRADO, manteniendo los precios congelados mientras operamos con baja volatilidad en las criptomonedas. Los activos tecnológicos y cripto en cartera muestran movimientos laterales con ligeras ganancias o pérdidas contenidas. Mantenemos la estrategia defensiva en acciones cerradas y observamos el comportamiento de ETH-USD y SOL-USD en el mercado abierto 24/7."

**Operaciones del ciclo:**
- **[HOLD] MSFT** (Confianza: 70%): El mercado de Wall Street está cerrado y la posición muestra una ganancia moderada de +0.8%. Mantenemos a la espera de la apertura para buscar la toma de beneficios en la zona objetivo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear las posiciones actuales en criptomonedas (ETH-USD y SOL-USD) para evaluar posibles tomas de beneficios si alcanzan el objetivo de +2.0% a +3.5%. En cuanto abra Wall Street, vigilar de cerca el comportamiento de MSFT y QQQ para asegurar ganancias o cortar pérdidas rápidamente si el momentum se debilita."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **58** | 🎯 **41.4%** (24W / 20L / 14BE) | 🔴 **$-1.22 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-16 05:10` | 🟢 BUY | `SOL-USD` | $3.00 | $106.33 | SOL-USD presenta un RSI diario en zona de sobreventa extrema (29.0) y un cambio positivo e... |
| `2026-10-16 04:30` | 🟢 BUY | `ETH-USD` | $7.00 | $2451.90 | Aprovechamos la liquidez disponible sobre la reserva mínima ($14.17 vs $4.00 requeridos) p... |
| `2026-10-15 16:20` | 🔴 SELL (-0.10$) | `AAPL` | $9.90 | $342.86 | AAPL lleva más de un día abierta (1d 5h) sin mostrar un momentum significativo ni alcanzar... |
| `2026-10-15 12:50` | 🟢 BUY | `NVDA` | $8.00 | $217.32 | NVDA presenta un RSI de 1h en sobreventa extrema (21.5) con un inicio de recuperación en s... |
| `2026-10-15 12:20` | 🟢 BUY | `QQQ` | $10.00 | $725.09 | QQQ muestra un RSI de 1h en sobreventa extrema (28.7) cruzando al alza con un cambio posit... |

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
