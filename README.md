# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 07:20:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$11.61 USD** | **$26.88 USD** | **$38.49 USD** | 🔴 **-3.77%** ($-1.51) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 20h 29m |
| `BTC-USD` | 0.000061 | $81640.68 | $81057.94 | $4.96 | 📉 -0.71% | 10h 10m |
| `ETH-USD` | 0.002539 | $2362.71 | $2364.87 | $6.01 | 📈 +0.09% | 6h 9m |
| `SOL-USD` | 0.058789 | $102.06 | $102.10 | $6.00 | 📈 +0.04% | 3h 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra completamente cerrado, por lo que toda la atención operativa se concentra exclusivamente en las criptomonedas (24/7). Las criptos principales en cartera (BTC-USD, ETH-USD, SOL-USD) muestran un movimiento lateral a bajista en el corto plazo tras los rebotes recientes, con un momentum de 1h ligeramente negativo pero manteniéndose estables dentro de los límites de riesgo. Las posiciones están relativamente planas, sin alcanzar todavía los objetivos de take-profit (+2% a +3.5%) ni activar los stop-loss."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD se mantiene estable con una pequeña ganancia del 0.09%. El RSI de 1h se encuentra en 35.7 tras el rebote inicial. Mantendremos la posición en busca de la zona de take-profit entre +2.0% y +3.5%.
- **[HOLD] SOL-USD** (Confianza: 70%): SOL-USD opera estable sin cambios significativos desde su compra reciente. El holding time es bajo (3h 59m) y mantiene su estructura sin romper soportes, esperando nuevos impulsos alcistas.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en criptomonedas (BTC-USD, ETH-USD, SOL-USD) y la posición tecnológica (AAPL) que sigue cerrada. Monitorear de cerca los indicadores de 1h para asegurar beneficios si ETH-USD o SOL-USD reactivan su impulso alcista hacia el rango de +2% a +3.5%. Proteger rigurosamente el capital respetando el stop-loss de -2.0% ante cualquier caída imprevista en el fin de semana."
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
