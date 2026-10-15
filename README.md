# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 21:10:36`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.23 USD** | **$34.86 USD** | **$39.09 USD** | 🔴 **-2.29%** ($-0.91) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $341.27 | $9.86 | 📉 -1.41% | 10h 19m |
| `SOL-USD` | 0.095785 | $104.40 | $104.24 | $9.98 | 📉 -0.15% | 4h 39m |
| `ETH-USD` | 0.004135 | $2418.34 | $2421.93 | $10.01 | 📈 +0.15% | 2h 9m |
| `BTC-USD` | 0.000061 | $81640.68 | $81640.68 | $5.00 | 📈 +0.00% | 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra CERRADO, por lo que toda la atención operativa se desplaza hacia los criptoactivos (24/7). Observamos a BTC-USD en sobreventa extrema con un RSI de 1h en 24.9, ofreciendo una oportunidad táctica de rebote por reversión a la media. ETH-USD y SOL-USD se mantienen estables con ligeros incrementos en su cambio de 1h, vigilando de cerca los objetivos de take-profit entre +2.0% y +3.5%."

**Operaciones del ciclo:**
- **[BUY] BTC-USD** (Confianza: 85%): BTC-USD presenta un RSI de 1h en 24.9 (sobreventa extrema) y liquidez disponible suficiente tras mantener la reserva mínima. Entramos buscando un rebote técnico de corto plazo en un mercado activo 24/7.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener posiciones de ETH-USD y SOL-USD operando activamente y buscar toma de ganancias si alcanzan el rango de +2.0% a +3.5%. Aprovechar la liquidez disponible para abrir una posición en BTC-USD aprovechando su RSI de 1h en sobreventa extrema (< 25). Stop-loss estrictamente fijado en -2.0% para todas las posiciones activas."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **52** | 🎯 **42.3%** (22W / 16L / 14BE) | 🔴 **$-0.67 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-14 21:10` | 🟢 BUY | `BTC-USD` | $5.00 | $81640.68 | BTC-USD presenta un RSI de 1h en 24.9 (sobreventa extrema) y liquidez disponible suficient... |
| `2026-10-14 19:00` | 🟢 BUY | `ETH-USD` | $10.00 | $2418.34 | ETH-USD presenta un RSI de 1h en 22.0 (sobreventa extrema) y un cambio de 1h que comienza ... |
| `2026-10-14 16:30` | 🟢 BUY | `SOL-USD` | $10.00 | $104.40 | SOL-USD presenta un RSI de 1h en 30.9 saliendo de la zona de compresión y un cambio positi... |
| `2026-10-14 15:20` | 🔴 SELL (-0.08$) | `SOL-USD` | $9.92 | $103.86 | SOL-USD lleva varias horas sin mostrar el rebote esperado, su RSI de 1h ha caído hasta 25.... |
| `2026-10-14 12:30` | 🟢 BUY | `SOL-USD` | $10.00 | $104.70 | SOL-USD presenta un RSI de 1h en 29.2 saliendo de sobreventa extrema y un cambio de 1h pos... |

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
