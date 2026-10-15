# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 22:40:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.23 USD** | **$34.90 USD** | **$39.13 USD** | 🔴 **-2.17%** ($-0.87) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 11h 49m |
| `SOL-USD` | 0.095785 | $104.40 | $104.37 | $10.00 | 📉 -0.03% | 6h 9m |
| `ETH-USD` | 0.004135 | $2418.34 | $2417.53 | $10.00 | 📉 -0.03% | 3h 39m |
| `BTC-USD` | 0.000061 | $81640.68 | $81665.38 | $5.00 | 📈 +0.03% | 1h 30m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, manteniendo los precios estables para AAPL, NVDA, MSFT, QQQ y SPY. Los criptoactivos (BTC-USD, ETH-USD, SOL-USD) operan con normalidad 24/7 y muestran signos de consolidación tras las recientes caídas, con indicadores de RSI en 1h profundamente deprimidos pero intentando estabilizarse en busca de un rebote técnico."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 75%): La posición en AAPL se mantiene con una pérdida marginal del -0.92%. El mercado accionario está cerrado, por lo que no es posible operar. Mantenemos la posición a la espera de la apertura para buscar su objetivo de take-profit.
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD se encuentra operando en zona de soporte con un RSI de 1h en 33.6 intentando buscar un rebote técnico. El rendimiento está plano (-0.03%), por lo que se mantiene la posición buscando el objetivo alcista de corto plazo.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD muestra un RSI de 1h en 23.5 en sobreventa, consolidando tras el movimiento bajista previo. Se mantiene la posición a la espera del repunte hacia la zona de take-profit.
- **[HOLD] BTC-USD** (Confianza: 80%): BTC-USD se mantiene estable con una pequeña ganancia del +0.03%. Continuamos manteniendo la posición abierta para capturar el momentum alcista de corto plazo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas en criptomonedas (SOL-USD, ETH-USD, BTC-USD) y la acción de AAPL. Vigilar de cerca los objetivos de take-profit entre +2.0% y +3.5% y el límite estricto de stop-loss del -2.0%. La liquidez actual se mantiene en $4.23. En el siguiente ciclo se evaluará rotar capital si alguna posición cripto alcanza sobrecompra (> 70 RSI en 1h) o si se activa el stop-loss."
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
