# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 22:10:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.23 USD** | **$34.94 USD** | **$39.16 USD** | 🔴 **-2.09%** ($-0.84) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 11h 20m |
| `SOL-USD` | 0.095785 | $104.40 | $104.55 | $10.01 | 📈 +0.14% | 5h 39m |
| `ETH-USD` | 0.004135 | $2418.34 | $2419.98 | $10.01 | 📈 +0.07% | 3h 9m |
| `BTC-USD` | 0.000061 | $81640.68 | $81760.94 | $5.01 | 📈 +0.15% | 1h 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que toda la actividad se concentra en las criptomonedas (BTC-USD, ETH-USD, SOL-USD), las cuales operan 24/7 y muestran signos de estabilización tras recientes caídas. Las posiciones actuales se mantienen estables con ligeras ganancias o pérdidas contenidas, respetando el stop-loss y sin alcanzar todavía el take-profit del +2.0%. Mantendremos las posiciones actuales a la espera de un mayor impulso alcista."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición muestra un pequeño beneficio del 0.14% y un RSI de 1h en 35.4 recuperándose. Mantenemos buscando el objetivo de take-profit.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra un RSI de 1h en 24.8 sobrevendido pero con un cambio positivo reciente del 0.17%. Esperamos el rebote técnico.
- **[HOLD] BTC-USD** (Confianza: 75%): BTC-USD se mantiene estable con un leve avance y RSI de 1h en 29.9. Sin señales de alarma, mantenemos la posición.
- **[HOLD] AAPL** (Confianza: 70%): El mercado de valores está cerrado y la posición está dentro de parámetros normales de fluctuación sin romper soportes.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear de cerca el comportamiento de ETH-USD, BTC-USD y SOL-USD. El RSI de 1h se mantiene en niveles bajos o saliendo de sobreventa, por lo que mantendremos las posiciones abiertas buscando capturar el rebote hacia la zona de take-profit (+2.0% a +3.5%). Vigilar que ninguna posición rompa el stop-loss del -2.0% y mantener la liquidez disponible de $4.23 intacta hasta el próximo ciclo."
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
