# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 22:01:03`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.23 USD** | **$34.92 USD** | **$39.15 USD** | 🔴 **-2.13%** ($-0.85) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 11h 10m |
| `SOL-USD` | 0.095785 | $104.40 | $104.43 | $10.00 | 📈 +0.03% | 5h 30m |
| `ETH-USD` | 0.004135 | $2418.34 | $2420.52 | $10.01 | 📈 +0.09% | 3h 0m |
| `BTC-USD` | 0.000061 | $81640.68 | $81625.29 | $5.00 | 📉 -0.02% | 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado y sus precios congelados, por lo que toda la atención operativa se concentra en las criptomonedas (BTC-USD, ETH-USD, SOL-USD), que operan 24/7. Las criptomonedas muestran signos de consolidación tras las recientes caídas, con indicadores RSI de 1 hora en niveles de sobreventa extrema pero intentando girar al alza con pequeños cambios porcentuales positivos por hora. La posición en AAPL se mantiene estable pero el mercado está cerrado, mientras que las criptomonedas se mantienen dentro del rango de tolerancia de pérdida sin alcanzar el stop-loss estricto."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD mantiene un comportamiento estable con un pequeño cambio positivo de 1h (+0.2%) y un RSI de 1h en 29.7, preparándose para un posible rebote técnico desde la zona de sobreventa. Se mantiene la posición abierta buscando el take-profit.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra un comportamiento similar con un cambio de 1h positivo (+0.19%) y un RSI de 1h en 22.6. La posición está ligeramente en positivo y se mantiene en busca del objetivo de ganancia sin romper los soportes de riesgo.
- **[HOLD] BTC-USD** (Confianza: 70%): BTC-USD opera en niveles de sobreventa extrema con un RSI de 1h en 22.8 y un leve repunte a 1h. Se mantiene la posición dentro de los límites de riesgo a la espera de la confirmación del rebote técnico.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas en criptomonedas (BTC-USD, ETH-USD, SOL-USD) y la acción tradicional (AAPL) que está en mercado cerrado. Esperar a la próxima sesión para evaluar posibles tomas de ganancias si el RSI supera 70 o si se alcanza el take-profit del +2.0% al +3.5%. Vigilar estrictamente que ninguna posición cruce el límite de pérdida del -2.0% para cortar pérdidas de inmediato. Mantener la liquidez actual intacta."
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
