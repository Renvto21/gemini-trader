# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 06:00:49`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.17 USD** | **$34.60 USD** | **$38.77 USD** | 🔴 **-3.08%** ($-1.23) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $539.44 | $6.55 | 📈 +0.80% | 19h 10m |
| `QQQ` | 0.013791 | $725.09 | $728.00 | $10.04 | 📈 +0.40% | 17h 40m |
| `NVDA` | 0.036812 | $217.32 | $217.23 | $8.00 | 📉 -0.04% | 17h 10m |
| `ETH-USD` | 0.002855 | $2451.90 | $2453.72 | $7.01 | 📈 +0.07% | 1h 29m |
| `SOL-USD` | 0.028214 | $106.33 | $106.65 | $3.01 | 📈 +0.30% | 49m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de Wall Street se encuentra cerrado y sus precios congelados, por lo que la liquidez activa se concentra en las criptomonedas (ABIERTO 24/7). Las posiciones actuales en ETH-USD y SOL-USD muestran ligeras ganancias pero sin el momentum suficiente para alcanzar el objetivo de take-profit del +2.0% al +3.5%. Las acciones de MSFT, QQQ y NVDA se mantienen en HOLD a la espera de la apertura de los mercados tradicionales."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 70%): La posición en ETH-USD se mantiene estable con un pequeño beneficio marginal. Esperamos a que el RSI de 1H supere 70 o se acerque al take-profit objetivo.
- **[HOLD] SOL-USD** (Confianza: 70%): SOL-USD muestra un comportamiento lateral con leve ganancia. Mantenemos la posición buscando capturar el rebote técnico hacia la zona de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en criptomonedas (ETH-USD y SOL-USD) y en renta variable (MSFT, QQQ, NVDA) mientras operamos bajo estrictos márgenes de control de riesgo. Vigilar que ETH-USD y SOL-USD alcancen el rango de take-profit (+2.0% a +3.5%) o un RSI de 1H superior a 70. Prepararse para rotar capital hacia oportunidades de alta convicción en cuanto Wall Street abra o si surge una ruptura clara en cripto."
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
