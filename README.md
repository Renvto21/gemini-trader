# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 03:50:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$11.61 USD** | **$26.82 USD** | **$38.43 USD** | 🔴 **-3.93%** ($-1.57) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 17h 0m |
| `BTC-USD` | 0.000061 | $81640.68 | $80720.49 | $4.94 | 📉 -1.13% | 6h 40m |
| `ETH-USD` | 0.002539 | $2362.71 | $2353.81 | $5.98 | 📉 -0.38% | 2h 40m |
| `SOL-USD` | 0.058789 | $102.06 | $101.83 | $5.99 | 📉 -0.23% | 30m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de renta variable tradicional se encuentra cerrado, por lo que la liquidez y la acción operativa se concentran exclusivamente en el mercado de criptomonedas, el cual opera 24/7. Las principales criptomonedas (SOL-USD, ETH-USD y BTC-USD) muestran ligeros intentos de recuperación en su marco temporal de 1 hora con cambios positivos marginales y RSI saliendo de zonas de sobreventa extrema, manteniendo nuestra tesis de rebote técnico (mean reversion). Las posiciones actuales registran pérdidas menores controladas dentro de los rangos de tolerancia antes del stop-loss."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD muestra un RSI de 1h en 31.4 y un cambio positivo de 1h de 0.48%, lo que indica el inicio de un potencial rebote técnico tras la fuerte caída de 24h. Mantenemos la posición para capturar el impulso alcista.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD mantiene un RSI de 1h bajo en 22.2 pero con un cambio de 1h positivo (0.31%). La pérdida actual es marginal (-0.38%), por lo que esperamos la consolidación del rebote hacia la zona de take-profit.
- **[HOLD] BTC-USD** (Confianza: 70%): BTC-USD opera estable con un ligero incremento de 1h del 0.29%. La pérdida actual es de -1.13%, muy lejos del stop-loss y con expectativa de acompañar el movimiento alcista general del mercado cripto.
- **[HOLD] AAPL** (Confianza: 80%): El mercado de Wall Street se encuentra cerrado para AAPL. La posición se mantiene intacta a la espera de la apertura de la bolsa para evaluar su comportamiento técnico.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales en criptomonedas (SOL-USD, ETH-USD, BTC-USD) y la posición en renta variable (AAPL) que está en mercado cerrado. Mantendremos la reserva de efectivo actual y vigilaremos los objetivos de take-profit entre +2.0% y +3.5% para asegurar ganancias parciales o totales. Si alguna posición rompe a la baja superando el límite de -2.0% de pérdida, ejecutaremos la venta inmediata para proteger el capital."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **54** | 🎯 **40.7%** (22W / 18L / 14BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-15 03:20` | 🟢 BUY | `SOL-USD` | $6.00 | $102.06 | SOL-USD muestra un RSI de 1h en 33.3 saliendo de zonas de compresión bajista, acompañado d... |
| `2026-10-15 01:10` | 🟢 BUY | `ETH-USD` | $6.00 | $2362.71 | ETH-USD presenta un RSI de 1h extremadamente bajo en 23.5 saliendo de sobreventa y un camb... |
| `2026-10-14 23:30` | 🔴 SELL (-0.30$) | `SOL-USD` | $9.70 | $101.32 | La posición en SOL-USD acumula una pérdida de -2.95%, acercándose al límite crítico y sin ... |
| `2026-10-14 23:30` | 🔴 SELL (-0.32$) | `ETH-USD` | $9.68 | $2340.86 | 🚨 STOP-LOSS AUTOMÁTICO (CIRCUIT BREAKER): Pérdida de -3.20% superó el límite de seguridad ... |
| `2026-10-14 21:10` | 🟢 BUY | `BTC-USD` | $5.00 | $81640.68 | BTC-USD presenta un RSI de 1h en 24.9 (sobreventa extrema) y liquidez disponible suficient... |

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
