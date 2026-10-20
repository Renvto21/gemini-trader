# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 07:30:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.47 USD** | **$38.47 USD** | 🔴 **-3.83%** ($-1.53) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 20h 50m |
| `ETH-USD` | 0.004178 | $2393.62 | $2384.43 | $9.96 | 📉 -0.38% | 18h 39m |
| `SOL-USD` | 0.096034 | $104.13 | $103.87 | $9.98 | 📉 -0.25% | 14h 50m |
| `BTC-USD` | 0.000105 | $81767.70 | $81509.75 | $8.54 | 📉 -0.32% | 14h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sentimiento mixto a la baja con los principales índices de Wall Street cerrados y operando sin cambios directos. En el mercado cripto 24/7 (BTC-USD, ETH-USD, SOL-USD), los precios se mantienen en rangos laterales estrechos con ligeras fluctuaciones y un momentum alcista de corto plazo moderado (cambios de 1h positivos pero RSI de 1h por debajo de 50). Las posiciones actuales acumulan pérdidas menores que se mantienen dentro del umbral de tolerancia antes del stop-loss de -2.0%."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 70%): La posición en BTC-USD se mantiene estable con una pérdida marginal de -0.32%. Muestra un ligero cambio positivo de 1h (0.16%) y un RSI de 1h en 38.6, lo cual sugiere consolidación previa a un posible intento de rebote. Mantenemos la posición a la espera de mayor volumen.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales (QQQ, ETH-USD, SOL-USD, BTC-USD) ya que ninguna ha alcanzado el stop-loss estricto de -2.0% ni el take-profit. Vigilaré de cerca el RSI de 1 hora en criptomonedas para buscar rupturas por encima de 50 que confirmen el rebote técnico y permitan asegurar beneficios. Si persisten los movimientos laterales sin momentum en las próximas horas, procederé a rotar capital."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **77** | 🎯 **42.9%** (33W / 29L / 15BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-19 23:00` | 🟢 BUY | `BTC-USD` | $4.00 | $81646.39 | BTC-USD presenta un RSI de 1 hora en 27.7, nivel de sobreventa profunda ideal para un rebo... |
| `2026-10-19 17:10` | 🟢 BUY | `BTC-USD` | $4.57 | $81874.05 | BTC-USD muestra señales de rebote técnico con un RSI de 1 hora en 31.1 recuperándose y un ... |
| `2026-10-19 16:40` | 🟢 BUY | `SOL-USD` | $10.00 | $104.13 | SOL-USD presenta un RSI diario extremo de 19.7, indicando condiciones de sobreventa profun... |
| `2026-10-19 12:51` | 🟢 BUY | `ETH-USD` | $10.00 | $2393.62 | ETH-USD presenta un RSI de 1 hora en 34.6, entrando en zona de sobreventa de corto plazo, ... |
| `2026-10-19 10:40` | 🟢 BUY | `QQQ` | $10.00 | $718.92 | QQQ muestra un fuerte momentum intradiario con un cambio de 1h del +1.28%, liderando el re... |

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
