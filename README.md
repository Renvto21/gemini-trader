# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 07:00:49`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.44 USD** | **$38.44 USD** | 🔴 **-3.89%** ($-1.56) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 20h 20m |
| `ETH-USD` | 0.004178 | $2393.62 | $2381.08 | $9.95 | 📉 -0.52% | 18h 9m |
| `SOL-USD` | 0.096034 | $104.13 | $103.90 | $9.98 | 📉 -0.22% | 14h 20m |
| `BTC-USD` | 0.000105 | $81767.70 | $81393.72 | $8.53 | 📉 -0.46% | 13h 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, manteniendo congelados los precios de los activos principales como QQQ. En el frente de criptomonedas (abierto 24/7), los precios de BTC-USD, ETH-USD y SOL-USD muestran un movimiento lateral a bajista con variaciones mínimas en la última hora y un RSI de 1 hora que se mantiene por debajo de 50 (BTC en 33.9, ETH en 37.3, SOL en 41.6). Las pérdidas en las posiciones abiertas son reducidas y se encuentran dentro de los límites aceptables previos al stop-loss, por lo que se prioriza la paciencia hasta observar un momentum alcista definitivo."

**Operaciones del ciclo:**
- **[HOLD] QQQ** (Confianza: 75%): La posición en QQQ se mantiene con una pérdida marginal del -0.08% tras 20 horas abierto. Dado que el mercado está cerrado, no se puede operar y se espera la apertura para evaluar la reacción del precio en busca de un rebote técnico o una rotación si la debilidad persiste.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD registra una leve pérdida de -0.52% con un RSI diario de sobreventa extrema (24.0). Mantenemos la posición esperando el impulso del rebote técnico prometido por las condiciones macro de sobreventa.
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD se mantiene estable con -0.22% de PnL y un RSI diario de 21.1. Las condiciones para un rebote siguen vigentes y la posición está lejos de activar el stop-loss.
- **[HOLD] BTC-USD** (Confianza: 75%): BTC-USD muestra un PnL de -0.46% y un RSI de 1 hora en 33.9. Se conserva la posición a la espera de que el impulso de corto plazo cruce niveles de confirmación alcista.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos todas las posiciones actuales (QQQ, ETH-USD, SOL-USD, BTC-USD) ya que ninguna ha alcanzado el stop-loss de -2.0% ni el objetivo de take-profit. Para los siguientes ciclos, seguiremos monitoreando el RSI de 1 hora en las criptomonedas buscando cruces por encima de 55-60 que confirmen el rebote técnico esperado. Si alguna posición se estanca o rompe soportes a la baja antes del rebote, aplicaremos rotación de capital inmediata."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **77** | 🎯 **42.9%** (33W / 29L / 15BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-19 23:00` | 🟢 BUY | `BTC-USD` | $4.00 | $81646.39 | BTC-USD presenta un RSI de 1 hora en 27.7, nivel de sobreventa profunda ideal para un rebo... |
| `2026-10-19 17:10` | 🟢 BUY | `BTC-USD` | $4.57 | $81874.05 | BTC-USD muestra señales de rebote técnico con un RSI de 1 hora en 31.1 recuperándose y un ... |
| `2026-10-19 16:40` | 🟢 BUY | `SOL-USD` | $10.00 | $104.13 | SOL-USD presenta un RSI diario extremo de 19.7, indicando condiciones de sobreventa profun... |
| `2026-10-19 12:51` | 🟢 BUY | `ETH-USD` | $10.00 | $2393.62 | ETH-USD presenta un RSI de 1 hora en 34.6, entrando en zona de sobreventa de corto plazo, ... |
| `2026-10-19 10:40` | 🟢 BUY | `QQQ` | $10.00 | $718.92 | QQQ muestra un fuerte momentum intradiario con un cambio de 1h del +1.28%, liderando el re... |

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
