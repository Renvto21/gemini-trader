# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 22:30:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.23 USD** | **$34.85 USD** | **$39.08 USD** | 🔴 **-2.30%** ($-0.92) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 11h 39m |
| `SOL-USD` | 0.095785 | $104.40 | $104.07 | $9.97 | 📉 -0.32% | 5h 59m |
| `ETH-USD` | 0.004135 | $2418.34 | $2413.44 | $9.98 | 📉 -0.20% | 3h 29m |
| `BTC-USD` | 0.000061 | $81640.68 | $81557.34 | $4.99 | 📉 -0.10% | 1h 20m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado accionario tradicional (Wall Street) se encuentra CERRADO, por lo que toda la actividad se concentra exclusivamente en los criptoactivos (BTC-USD, ETH-USD, SOL-USD), que operan 24/7. Las criptomonedas muestran condiciones de sobreventa extrema en el corto plazo (RSI de 1h oscilando entre 19 y 26), pero la tendencia principal se mantiene bajista bajo la SMA20. Las posiciones actuales muestran pérdidas mínimas controladas y se encuentran dentro de los márgenes de tolerancia antes de activar el stop-loss o take-profit."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición en SOL-USD lleva poco tiempo abierta (aprox. 6 horas) con una pérdida marginal del -0.32%. El RSI de 1h en 26.7 indica que sigue en zona de compresión a la espera de un rebote técnico. Se mantiene para buscar la zona de take-profit.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD presenta un RSI de 1h extremadamente bajo en 19.9, lo que sugiere una condición de sobreventa profunda ideal para un rebote inminente. La pérdida actual es de solo -0.20%, por lo que se mantiene la posición.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas en criptomonedas (SOL-USD, ETH-USD, BTC-USD) y la acción de AAPL a la espera de un rebote técnico que permita alcanzar el objetivo de take-profit (+2.0% a +3.5%). Vigilar estrictamente el límite de stop-loss del -2.0% en cada activo. Mantener la liquidez actual de $4.23 y estar preparados para vender o rotar capital en cuanto los indicadores de 1h muestren señales claras de sobrecompra (> 70) o si el impulso alcista falla."
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
