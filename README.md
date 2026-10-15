# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 23:30:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$23.61 USD** | **$14.85 USD** | **$38.46 USD** | 🔴 **-3.86%** ($-1.54) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 12h 39m |
| `BTC-USD` | 0.000061 | $81640.68 | $80621.15 | $4.94 | 📉 -1.25% | 2h 20m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto 24/7 muestra un fuerte impulso bajista con SOL-USD y BTC-USD profundizando caídas y acercándose a niveles de sobreventa extrema, aunque sin señales claras de giro al alza en 1h todavía. Los mercados tradicionales permanecen cerrados. El portafolio sufre presión bajista, destacando SOL-USD con una pérdida del -2.95%, cerca del umbral de stop-loss del -2.0% estipulado en las reglas tácticas."

**Operaciones del ciclo:**
- **[SELL] SOL-USD** (Confianza: 90%): La posición en SOL-USD acumula una pérdida de -2.95%, acercándose al límite crítico y sin mostrar el rebote esperado tras casi 7 horas de holding. Aplicamos disciplina táctica para cortar la pérdida y proteger liquidez.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear estrictamente SOL-USD. Si su pérdida supera el -2.0% o rompe soportes adicionales, proceder a la venta inmediata para proteger capital y mantener la reserva de efectivo. Esperar confirmaciones con RSI de 1h saliendo de sobreventa (> 35) con cambio porcentual positivo para reenganchar capital en cripto."
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
