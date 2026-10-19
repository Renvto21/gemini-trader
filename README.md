# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 01:30:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$30.48 USD** | **$8.05 USD** | **$38.53 USD** | 🔴 **-3.67%** ($-1.47) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.003330 | $2402.76 | $2419.10 | $8.05 | 📈 +0.68% | 4h 10m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado por fin de semana, por lo que la liquidez activa se concentra en las criptomonedas. ETH-USD mantiene una ganancia moderada pero su RSI de 1 hora se encuentra en 65.6, acercándose a la zona de sobrecompra. Por otro lado, SOL-USD y BTC-USD muestran un RSI de 1 hora en sobrecompra extrema (73.5 y 77.3 respectivamente), lo que indica agotamiento del impulso alcista de corto plazo y posibles zonas de toma de ganancias."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD muestra una ganancia actual del +0.68% con un holding time de poco más de 4 horas. Aunque el RSI de 1 hora está en 65.6 acercándose a sobrecompra, aún no alcanza el objetivo estricto de take-profit (+2.0% a +3.5% o RSI > 70). Mantenemos la posición esperando la culminación del impulso.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos ETH-USD en cartera mientras monitoreamos de cerca su aproximación a la zona de sobrecompra (>70 en RSI de 1 hora) o el rango objetivo de ganancia del +2.0% al +3.5% para proceder a una venta inmediata y asegurar efectivo. Con una reserva de efectivo sólida de $30.48 USD, esperaremos un retroceso técnico saludable en SOL-USD o BTC-USD para reentrar con fuerza en cuanto sus indicadores de corto plazo se aligeren."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **76** | 🎯 **42.1%** (32W / 29L / 15BE) | 🔴 **$-1.38 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-19 01:00` | 🔴 SELL (-0.00$) | `SOL-USD` | $8.00 | $105.08 | SOL-USD ha entrado en sobrecompra con un RSI de 1 hora en 72.7, cumpliendo estrictamente c... |
| `2026-10-18 23:20` | 🟢 BUY | `SOL-USD` | $8.00 | $105.11 | SOL-USD presenta un RSI diario en 21.8 (sobreventa extrema) y un momentum de 24 horas alci... |
| `2026-10-18 23:10` | 🔴 SELL (+0.17$) | `SOL-USD` | $8.17 | $105.19 | SOL-USD acumula una ganancia del +2.12%, cumpliendo con la regla de toma rápida de gananci... |
| `2026-10-18 21:20` | 🟢 BUY | `ETH-USD` | $8.00 | $2402.76 | ETH-USD muestra un RSI diario fuertemente sobrevendido en 23.2 y un cambio positivo en la ... |
| `2026-10-18 21:00` | 🔴 SELL (+0.16$) | `ETH-USD` | $8.16 | $2409.06 | ETH-USD ha alcanzado una ganancia del +2.03%, cumpliendo con la regla de toma rápida de ga... |

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
