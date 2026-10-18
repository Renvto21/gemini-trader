# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 20:30:50`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.15 USD** | **$16.24 USD** | **$38.39 USD** | 🔴 **-4.02%** ($-1.61) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.003388 | $2361.22 | $2406.20 | $8.15 | 📈 +1.90% | 1h 50m |
| `SOL-USD` | 0.077662 | $103.01 | $104.16 | $8.09 | 📈 +1.12% | 1h 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado por lo que la liquidez activa se concentra en las criptomonedas. ETH-USD se encuentra operando con un rendimiento positivo de +1.9%, acercándose a nuestro objetivo de take-profit, mientras que SOL-USD muestra un rendimiento del +1.12%. Mantendremos ambas posiciones activas en este ciclo para permitirles alcanzar el rango óptimo de ganancia del +2.0% al +3.5%."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD muestra un rendimiento positivo de +1.9% acercándose al objetivo de take-profit. Mantenemos la posición abierta esperando alcanzar el rango del 2% al 3.5%.
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD presenta un PnL de +1.12% con un RSI de 1h en 52.0. Continuamos dentro de la posición para capturar el rebote técnico completo hacia el rango de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear de cerca ETH-USD y SOL-USD para ejecutar la venta (take-profit) tan pronto alcancen el rango de +2.0% a +3.5% o si el RSI de 1 hora entra en sobrecompra (>70). Mantener la reserva de efectivo requerida y preparar el terreno para rotar capital hacia nuevas oportunidades una vez cerradas estas posiciones."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **73** | 🎯 **41.1%** (30W / 29L / 14BE) | 🔴 **$-1.71 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-18 19:30` | 🟢 BUY | `SOL-USD` | $8.00 | $103.01 | SOL-USD presenta un RSI diario extremadamente bajo (16.5) y un RSI de 1h recuperándose has... |
| `2026-10-18 19:10` | 🔴 SELL (+0.17$) | `SOL-USD` | $8.17 | $102.92 | SOL-USD ha alcanzado un rendimiento de +2.07% cumpliendo con nuestra regla de toma rápida ... |
| `2026-10-18 18:40` | 🟢 BUY | `ETH-USD` | $8.00 | $2361.22 | ETH-USD muestra un RSI diario deprimido en 21.5 y un RSI de 1 hora que se recupera a 34.3 ... |
| `2026-10-18 17:00` | 🟢 BUY | `SOL-USD` | $8.00 | $100.83 | SOL-USD muestra un RSI diario extremadamente deprimido en 15.3 y un RSI de 1 hora en 23.4 ... |
| `2026-10-18 16:40` | 🔴 SELL (-0.19$) | `ETH-USD` | $9.81 | $2332.39 | ETH-USD registra una pérdida del -1.92% con un RSI de 1 hora en 18.5 que refleja debilidad... |

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
