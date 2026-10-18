# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 19:10:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$30.15 USD** | **$8.08 USD** | **$38.23 USD** | 🔴 **-4.43%** ($-1.77) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.003388 | $2361.22 | $2384.06 | $8.08 | 📈 +0.97% | 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de Wall Street se encuentra cerrado por lo que la liquidez activa se concentra en criptomonedas. SOL-USD muestra un rendimiento positivo con un PnL de +2.07%, alcanzando nuestro objetivo de take-profit inicial, mientras que ETH-USD se encuentra en +0.97% acercándose progresivamente a la zona objetivo. El impulso de corto plazo en cripto se mantiene constructivo con RSI de 1 hora recuperándose hacia la zona media."

**Operaciones del ciclo:**
- **[SELL] SOL-USD** (Confianza: 90%): SOL-USD ha alcanzado un rendimiento de +2.07% cumpliendo con nuestra regla de toma rápida de ganancias (take-profit entre +2.0% y +3.5%) para asegurar efectivo y rotar capital.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Asegurar beneficios vendiendo la posición de SOL-USD que ha alcanzado el objetivo de take-profit del +2.07%. Mantener la posición de ETH-USD vigilando de cerca su evolución hacia el objetivo de +2.0% a +3.5%. Mantener la reserva de efectivo por encima de los $4.00 USD requeridos y buscar reingresos tácticos si se presentan nuevas oportunidades en el sector cripto."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **73** | 🎯 **41.1%** (30W / 29L / 14BE) | 🔴 **$-1.71 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-18 19:10` | 🔴 SELL (+0.17$) | `SOL-USD` | $8.17 | $102.92 | SOL-USD ha alcanzado un rendimiento de +2.07% cumpliendo con nuestra regla de toma rápida ... |
| `2026-10-18 18:40` | 🟢 BUY | `ETH-USD` | $8.00 | $2361.22 | ETH-USD muestra un RSI diario deprimido en 21.5 y un RSI de 1 hora que se recupera a 34.3 ... |
| `2026-10-18 17:00` | 🟢 BUY | `SOL-USD` | $8.00 | $100.83 | SOL-USD muestra un RSI diario extremadamente deprimido en 15.3 y un RSI de 1 hora en 23.4 ... |
| `2026-10-18 16:40` | 🔴 SELL (-0.19$) | `ETH-USD` | $9.81 | $2332.39 | ETH-USD registra una pérdida del -1.92% con un RSI de 1 hora en 18.5 que refleja debilidad... |
| `2026-10-18 16:40` | 🔴 SELL (-0.20$) | `SOL-USD` | $9.80 | $100.90 | La posición en SOL-USD lleva casi 6 horas abierta con una pérdida del -1.95% y un RSI de 1... |

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
