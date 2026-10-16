# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 07:20:52`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.17 USD** | **$34.57 USD** | **$38.74 USD** | 🔴 **-3.15%** ($-1.26) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $539.44 | $6.55 | 📈 +0.80% | 20h 30m |
| `QQQ` | 0.013791 | $725.09 | $728.00 | $10.04 | 📈 +0.40% | 19h 0m |
| `NVDA` | 0.036812 | $217.32 | $217.23 | $8.00 | 📉 -0.04% | 18h 30m |
| `ETH-USD` | 0.002855 | $2451.90 | $2450.70 | $7.00 | 📉 -0.05% | 2h 49m |
| `SOL-USD` | 0.028214 | $106.33 | $105.96 | $2.99 | 📉 -0.35% | 2h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de acciones tradicionales se encuentra cerrado, manteniendo los precios congelados, por lo que la operativa actual se centra exclusivamente en criptomonedas (abiertas 24/7). Las posiciones en cripto (ETH-USD y SOL-USD) muestran estabilidad con ligeras variaciones, mientras que las acciones en cartera (MSFT, QQQ, NVDA) operan lateralmente a la espera de la apertura de Wall Street. El efectivo disponible es limitado, por lo que mantendremos el enfoque en proteger posiciones y evaluar salidas por take-profit o stop-loss según la evolución del impulso."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 75%): La posición en ETH-USD se mantiene estable con un PnL neutral (-0.05%) tras pocas horas de apertura. El RSI diario se encuentra en zona baja (32.7) y el mercado cripto opera 24/7, por lo que mantenemos la posición buscando el rebote técnico hacia la zona objetivo de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en ETH-USD y SOL-USD vigilando de cerca los soportes para evitar activar el stop-loss del -2.0%. En cuanto abra Wall Street, evaluar la toma de beneficios en MSFT y QQQ si alcanzan el objetivo de +2.0% a +3.5%, o rotar capital si pierden momentum. Esperar confirmación de volumen en cripto para posibles reentradas."
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
