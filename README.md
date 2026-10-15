# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 23:40:36`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$23.61 USD** | **$14.87 USD** | **$38.48 USD** | 🔴 **-3.80%** ($-1.52) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 12h 49m |
| `BTC-USD` | 0.000061 | $81640.68 | $81001.31 | $4.96 | 📉 -0.78% | 2h 30m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de Wall Street se encuentra cerrado, por lo que toda la actividad se concentra en los activos cripto, que operan 24/7. Las criptomonedas principales (BTC-USD, ETH-USD, SOL-USD) muestran una tendencia bajista y lecturas débiles en el RSI de 1h, aunque ETH y BTC presentan niveles de sobreventa extrema. Los activos bursátiles tradicionales como AAPL se mantienen estables pero cerrados."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 60%): La posición abierta en BTC-USD registra una pérdida leve de -0.78% y se encuentra operando en un mercado 24/7. Aunque el RSI de 1h está bajo (21.6), aún no activa el stop-loss estricto de -2.0%. Mantendremos la posición vigilando de cerca el soporte para evitar pérdidas mayores.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener la posición de AAPL dada su tendencia alcista diaria a pesar del cierre del mercado. Monitorear de cerca BTC-USD: si su rendimiento cae por debajo del stop-loss de -2.0% o si no muestra una recuperación en el RSI de 1h (> 35) en los siguientes ciclos, proceder a liquidar. Vigilar SOL-USD y ETH-USD por posibles rebotes técnicos si el RSI de 1h cruza al alza con un cambio porcentual positivo. Mantener liquidez para aprovechar entradas agresivas en cripto en cuanto se confirme el momentum."
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
