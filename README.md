# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 10:01:05`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$11.61 USD** | **$26.78 USD** | **$38.40 USD** | 🔴 **-4.01%** ($-1.60) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 23h 10m |
| `BTC-USD` | 0.000061 | $81640.68 | $80510.60 | $4.93 | 📉 -1.38% | 12h 50m |
| `ETH-USD` | 0.002539 | $2362.71 | $2348.66 | $5.96 | 📉 -0.59% | 8h 50m |
| `SOL-USD` | 0.058789 | $102.06 | $101.75 | $5.98 | 📉 -0.30% | 6h 40m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general se encuentra bajo presión bajista, con los activos tradicionales cerrados y el mercado cripto operando en un rango lateral-bajista con indicios iniciales de estabilización. Los indicadores RSI de 1 hora en cripto se mantienen comprimidos alrededor de 30-38, sugiriendo que la presión vendedora de corto plazo está disminuyendo pero aún falta un volumen de confirmación alcista contundente."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 60%): La posición se encuentra con una pérdida controlada de -1.38% dentro del tiempo de retención. El mercado cripto muestra signos de consolidación y preferimos mantener la posición a la espera de un cruce alcista definitivo del RSI de 1h por encima de 50.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales (AAPL, BTC-USD, ETH-USD, SOL-USD) vigilando estrictamente el stop-loss del -2.0% para evitar pérdidas mayores. Dado que las posiciones llevan varias horas sin el rebote esperado, no realizaremos nuevas compras hasta que los indicadores RSI de 1h superen los 50 puntos con un cambio porcentual horario claramente positivo. Preservaremos el efectivo actual para buscar mejores oportunidades de rotación cuando el mercado accionario abra o se consolide un impulso claro en cripto."
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
