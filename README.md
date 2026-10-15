# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 10:40:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$16.50 USD** | **$21.96 USD** | **$38.45 USD** | 🔴 **-3.86%** ($-1.55) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $346.59 | $10.01 | 📈 +0.13% | 23h 50m |
| `ETH-USD` | 0.002539 | $2362.71 | $2347.25 | $5.96 | 📉 -0.65% | 9h 30m |
| `SOL-USD` | 0.058789 | $102.06 | $101.79 | $5.98 | 📉 -0.26% | 7h 20m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sentimiento predominantemente bajista con múltiples activos por debajo de sus medias móviles de 20 periodos. Sin embargo, se observan oportunidades interesantes de sobreventa extrema en el sector tecnológico y cripto. MSFT destaca con un RSI de 1h en 20.3 pero un sólido RSI diario de 64.8 en tendencia alcista. Las criptomonedas (ETH-USD y SOL-USD) se mantienen estables pero sin el momentum explosivo esperado, mientras que AAPL se mantiene con ligera ganancia pero sin romper hacia arriba de manera contundente."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 70%): La posición se mantiene estable con una ganancia marginal del 0.13% y operando en tendencia alcista sobre la SMA20. Se mantiene en cartera a la espera de un mayor impulso hacia la zona de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener posición en AAPL mientras conserve su tendencia alcista sobre SMA20, monitoreando take-profit si alcanza el rango de +2%. Evaluar la salida de ETH-USD o SOL-USD si el momentum de 1h no logra superar los niveles críticos. Vigilar a MSFT para una posible entrada si confirma el rebote técnico desde su sobreventa de 1h aprovechando la liquidez disponible."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **55** | 🎯 **40.0%** (22W / 19L / 14BE) | 🔴 **$-1.39 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-15 10:30` | 🔴 SELL (-0.10$) | `BTC-USD` | $4.88 | $80081.22 | La posición en BTC-USD se acerca al límite de tolerancia de pérdida (-1.91%) y el activo p... |
| `2026-10-15 03:20` | 🟢 BUY | `SOL-USD` | $6.00 | $102.06 | SOL-USD muestra un RSI de 1h en 33.3 saliendo de zonas de compresión bajista, acompañado d... |
| `2026-10-15 01:10` | 🟢 BUY | `ETH-USD` | $6.00 | $2362.71 | ETH-USD presenta un RSI de 1h extremadamente bajo en 23.5 saliendo de sobreventa y un camb... |
| `2026-10-14 23:30` | 🔴 SELL (-0.30$) | `SOL-USD` | $9.70 | $101.32 | La posición en SOL-USD acumula una pérdida de -2.95%, acercándose al límite crítico y sin ... |
| `2026-10-14 23:30` | 🔴 SELL (-0.32$) | `ETH-USD` | $9.68 | $2340.86 | 🚨 STOP-LOSS AUTOMÁTICO (CIRCUIT BREAKER): Pérdida de -3.20% superó el límite de seguridad ... |

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
