# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 00:30:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$23.61 USD** | **$14.86 USD** | **$38.48 USD** | 🔴 **-3.81%** ($-1.52) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 13h 39m |
| `BTC-USD` | 0.000061 | $81640.68 | $80913.21 | $4.96 | 📉 -0.89% | 3h 20m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general se encuentra bajo presión bajista, con los principales índices de Wall Street cerrados y las criptomonedas operando 24/7 en niveles de sobreventa extrema (RSI de 1 hora muy deprimidos). BTC-USD muestra debilidad temporal pero se mantiene en cartera esperando el rebote de reversión a la media, mientras que ETH-USD y SOL-USD continúan con caídas profundas pero RSI extremadamente bajos, vigilando posibles activaciones de rebote en cuanto aparezca momentum horario positivo."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 75%): La posición en BTC-USD lleva poco más de 3 horas abierta con una pérdida leve de -0.89%. El RSI de 1 hora está en 24.4 (sobreventa), por lo que mantenemos la posición buscando el rebote técnico hacia la media sin activar el stop-loss del -2.0%.
- **[HOLD] AAPL** (Confianza: 70%): AAPL se encuentra en mercado cerrado con una pérdida no realizada mínima de -0.92% tras casi 14 horas. Su tendencia diaria es alcista y no ha alcanzado el límite de stop-loss, por lo que se mantiene hasta la apertura de Wall Street.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener AAPL y BTC-USD bajo estrecha vigilancia de stop-loss a -2.0%. Dado que el mercado tradicional está cerrado, nos enfocamos exclusivamente en Cripto. Esperaremos la confirmación de cambio de tendencia en el change_1h_pct y RSI 1h para reintentar compras tácticas en SOL-USD o ETH-USD si muestran signos de giro. Mantener colchón de efectivo por encima de los $4.00 USD."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **54** | 🎯 **40.7%** (22W / 18L / 14BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-14 23:30` | 🔴 SELL (-0.30$) | `SOL-USD` | $9.70 | $101.32 | La posición en SOL-USD acumula una pérdida de -2.95%, acercándose al límite crítico y sin ... |
| `2026-10-14 23:30` | 🔴 SELL (-0.32$) | `ETH-USD` | $9.68 | $2340.86 | 🚨 STOP-LOSS AUTOMÁTICO (CIRCUIT BREAKER): Pérdida de -3.20% superó el límite de seguridad ... |
| `2026-10-14 21:10` | 🟢 BUY | `BTC-USD` | $5.00 | $81640.68 | BTC-USD presenta un RSI de 1h en 24.9 (sobreventa extrema) y liquidez disponible suficient... |
| `2026-10-14 19:00` | 🟢 BUY | `ETH-USD` | $10.00 | $2418.34 | ETH-USD presenta un RSI de 1h en 22.0 (sobreventa extrema) y un cambio de 1h que comienza ... |
| `2026-10-14 16:30` | 🟢 BUY | `SOL-USD` | $10.00 | $104.40 | SOL-USD presenta un RSI de 1h en 30.9 saliendo de la zona de compresión y un cambio positi... |

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
