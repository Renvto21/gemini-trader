# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 11:20:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$10.00 USD** | **$28.54 USD** | **$38.54 USD** | 🔴 **-3.65%** ($-1.46) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $345.29 | $9.98 | 📉 -0.25% | 1d 0h |
| `ETH-USD` | 0.002539 | $2362.71 | $2370.61 | $6.02 | 📈 +0.33% | 10h 10m |
| `SOL-USD` | 0.058789 | $102.06 | $103.11 | $6.06 | 📈 +1.03% | 8h 0m |
| `MSFT` | 0.012146 | $535.17 | $533.94 | $6.49 | 📉 -0.23% | 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sesgo bajista generalizado en temporalidades diarias (por debajo de las SMA20), pero con señales claras de sobreventa extrema en el corto plazo en varios activos tecnológicos e índices (QQQ con RSI 1h en 16.4 y SPY en 22.4). Las criptomonedas (SOL-USD y ETH-USD) se mantienen operando 24/7 y muestran ligeros rebotes en la última hora, aunque la liquidez general se mantiene cauta con un efectivo de $10.00 USD."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD muestra un rendimiento positivo de +1.03% y un impulso continuo en 1h. Se mantiene en cartera para buscar el objetivo de ganancia de +2% a +3.5% antes de realizar toma de beneficios.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales (AAPL, ETH-USD, SOL-USD, MSFT) mientras desarrollen su rebote técnico. Monitorear de cerca SOL-USD y ETH-USD para asegurar beneficios parciales si se acercan al rango de objetivo del +2.0% al +3.5%. Proteger rigurosamente el capital y estar preparados para tomar ganancias o rotar posiciones si el momentum de corto plazo se desvanece."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **55** | 🎯 **40.0%** (22W / 19L / 14BE) | 🔴 **$-1.39 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-15 10:50` | 🟢 BUY | `MSFT` | $6.50 | $535.17 | MSFT presenta un RSI de 1h ultra comprimido en sobreventa extrema (14.7) con un cambio pos... |
| `2026-10-15 10:30` | 🔴 SELL (-0.10$) | `BTC-USD` | $4.88 | $80081.22 | La posición en BTC-USD se acerca al límite de tolerancia de pérdida (-1.91%) y el activo p... |
| `2026-10-15 03:20` | 🟢 BUY | `SOL-USD` | $6.00 | $102.06 | SOL-USD muestra un RSI de 1h en 33.3 saliendo de zonas de compresión bajista, acompañado d... |
| `2026-10-15 01:10` | 🟢 BUY | `ETH-USD` | $6.00 | $2362.71 | ETH-USD presenta un RSI de 1h extremadamente bajo en 23.5 saliendo de sobreventa y un camb... |
| `2026-10-14 23:30` | 🔴 SELL (-0.30$) | `SOL-USD` | $9.70 | $101.32 | La posición en SOL-USD acumula una pérdida de -2.95%, acercándose al límite crítico y sin ... |

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
