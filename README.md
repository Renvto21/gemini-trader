# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 11:40:50`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$10.00 USD** | **$28.59 USD** | **$38.58 USD** | 🔴 **-3.54%** ($-1.42) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $344.61 | $9.96 | 📉 -0.44% | 1d 0h |
| `ETH-USD` | 0.002539 | $2362.71 | $2377.91 | $6.04 | 📈 +0.64% | 10h 30m |
| `SOL-USD` | 0.058789 | $102.06 | $103.60 | $6.09 | 📈 +1.51% | 8h 20m |
| `MSFT` | 0.012146 | $535.17 | $535.25 | $6.50 | 📈 +0.01% | 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra señales mixtas con presión bajista generalizada en temporalidad diaria, pero con oportunidades claras de rebote técnico de corto plazo en criptomonedas y tecnología. SOL-USD y ETH-USD continúan su recuperación mostrando impulsos de 1h positivos, mientras que activos como NVDA y QQQ presentan condiciones de sobreventa extrema en RSI de 1 hora que podrían activar potentes rebotes. Mantenemos una postura agresiva y de rotación rápida de capital según nuestros niveles de take-profit y stop-loss."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): La posición acumula un rendimiento positivo de 1.51% y muestra buen impulso de corto plazo con change_1h_pct positivo (+2.14%). Se mantiene abierta buscando alcanzar el objetivo de take-profit del 2.0% al 3.5%.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear de cerca SOL-USD (actualmente con +1.51% de ganancia) para asegurar ganancias si se acerca al rango de +2.0% a +3.5%. Evaluar la posición en MSFT y AAPL para mantener estrictos stop-loss ante cualquier giro bajista. Estar preparados para reasignar liquidez hacia NVDA o QQQ si confirman la salida de sobreventa en gráficos de 1 hora."
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
