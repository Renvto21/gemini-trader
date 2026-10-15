# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 02:40:54`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$17.61 USD** | **$20.87 USD** | **$38.49 USD** | 🔴 **-3.79%** ($-1.51) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 15h 50m |
| `BTC-USD` | 0.000061 | $81640.68 | $81057.17 | $4.96 | 📉 -0.71% | 5h 30m |
| `ETH-USD` | 0.002539 | $2362.71 | $2363.44 | $6.00 | 📈 +0.03% | 1h 30m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional (Wall Street) se encuentra cerrado, por lo que toda la actividad se concentra en las criptomonedas, las cuales operan 24/7 pero muestran un sesgo bajista generalizado de corto plazo. BTC-USD y ETH-USD presentan ligeras caídas en la última hora y un momentum debilitado. AAPL permanece cerrado con una pérdida menor no realizada."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 60%): ETH-USD se encuentra recientemente abierto tras un intento de rebote por sobreventa, con una pérdida casi nula (0.03%). Mantendremos la posición monitoreando de cerca su RSI de 1h y el límite estricto de stop-loss.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener posiciones actuales en AAPL, BTC-USD y ETH-USD mientras el mercado cripto define un soporte claro. Vigilar de cerca el RSI de 1h en ETH-USD y BTC-USD; si rompen a la baja el límite del -2.0% de pérdida o el RSI cae por debajo de 25 sin mostrar rebote, procederé a vender para proteger el capital. Mantener la liquidez disponible para buscar entradas de alto impulso en cuanto se observe un cambio de tendencia intradía."
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
