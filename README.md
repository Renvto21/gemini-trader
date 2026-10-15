# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 03:00:56`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$17.61 USD** | **$20.79 USD** | **$38.41 USD** | 🔴 **-3.99%** ($-1.59) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 16h 10m |
| `BTC-USD` | 0.000061 | $81640.68 | $80475.20 | $4.93 | 📉 -1.43% | 5h 50m |
| `ETH-USD` | 0.002539 | $2362.71 | $2345.73 | $5.96 | 📉 -0.72% | 1h 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado bursátil de EE. UU. se encuentra cerrado, por lo que toda la atención se desplaza hacia el mercado cripto que opera 24/7. Las principales criptomonedas (BTC-USD, ETH-USD y SOL-USD) muestran una fuerte presión bajista en el gráfico diario, con RSI de 1 hora extremadamente deprimidos (ETH-USD en 18.5 y BTC-USD en 28.4), lo que indica condiciones de sobreventa profunda pero con riesgo de continuación si no aparecen flujos de compra. Las posiciones en cartera acumulan pérdidas moderadas pero se mantienen bajo el límite del stop-loss del -2.0%, a la espera de un rebote técnico inminente."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 60%): BTC-USD se encuentra en sobreventa con RSI de 1h en 28.4, aunque la tendencia diaria es bajista. La pérdida actual es de -1.43%, manteniéndose dentro del margen de seguridad antes del stop-loss del -2.0%. Se prefiere mantener a la espera de un volumen de compra que active el rebote.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en AAPL (mercado cerrado), BTC-USD y ETH-USD. Vigilar estrictamente el stop-loss en BTC-USD y ETH-USD si las pérdidas superan el -2.0% o si el momentum bajista quiebra los soportes actuales. Conservar la liquidez actual para buscar entradas adicionales solo si se confirma un cambio de tendencia intradiario en cripto o cuando abra Wall Street."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **54** | 🎯 **40.7%** (22W / 18L / 14BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-15 01:10` | 🟢 BUY | `ETH-USD` | $6.00 | $2362.71 | ETH-USD presenta un RSI de 1h extremadamente bajo en 23.5 saliendo de sobreventa y un camb... |
| `2026-10-14 23:30` | 🔴 SELL (-0.30$) | `SOL-USD` | $9.70 | $101.32 | La posición en SOL-USD acumula una pérdida de -2.95%, acercándose al límite crítico y sin ... |
| `2026-10-14 23:30` | 🔴 SELL (-0.32$) | `ETH-USD` | $9.68 | $2340.86 | 🚨 STOP-LOSS AUTOMÁTICO (CIRCUIT BREAKER): Pérdida de -3.20% superó el límite de seguridad ... |
| `2026-10-14 21:10` | 🟢 BUY | `BTC-USD` | $5.00 | $81640.68 | BTC-USD presenta un RSI de 1h en 24.9 (sobreventa extrema) y liquidez disponible suficient... |
| `2026-10-14 19:00` | 🟢 BUY | `ETH-USD` | $10.00 | $2418.34 | ETH-USD presenta un RSI de 1h en 22.0 (sobreventa extrema) y un cambio de 1h que comienza ... |

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
