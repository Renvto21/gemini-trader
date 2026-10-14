# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 02:00:52`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.54 USD** | **$17.06 USD** | **$39.60 USD** | 🔴 **-0.99%** ($-0.40) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001993 | $2508.37 | $2511.39 | $5.01 | 📈 +0.12% | 8h 50m |
| `BTC-USD` | 0.000072 | $83128.62 | $83635.21 | $6.04 | 📈 +0.61% | 5h 0m |
| `SOL-USD` | 0.055840 | $107.45 | $107.81 | $6.02 | 📈 +0.34% | 2h 49m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se mantiene abierto y operando con ligera estabilidad tras los rebotes recientes. Los activos en cartera (ETH-USD, BTC-USD y SOL-USD) muestran ganancias moderadas pero estables, aunque ninguna ha alcanzado aún el objetivo de take-profit del 2.0% al 3.5%. Los mercados tradicionales (Wall Street) se encuentran cerrados, por lo que toda la atención táctica se centra en la gestión de las criptomonedas abiertas."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): La posición en BTC-USD muestra un rendimiento positivo de +0.61% tras su reciente apertura, manteniendo un comportamiento técnico estable sin alcanzar todavía el umbral de take-profit ni mostrar debilidad que active un stop-loss.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas actuales (ETH-USD, BTC-USD, SOL-USD) monitoreando de cerca su evolución hacia el rango de take-profit del 2.0% al 3.5% o hasta que el RSI de 1 hora supere 70. Mantener una reserva de liquidez cercana al efectivo actual ($22.54) y esperar señales de aceleración del momentum o rupturas claras antes de realizar nuevas compras o rotaciones."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **48** | 🎯 **45.8%** (22W / 12L / 14BE) | 🔴 **$-0.38 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 23:11` | 🟢 BUY | `SOL-USD` | $6.00 | $107.45 | SOL-USD presenta un RSI diario en niveles de sobreventa extrema (28.3) y muestra un sólido... |
| `2026-10-13 21:00` | 🟢 BUY | `BTC-USD` | $6.00 | $83128.62 | BTC-USD muestra un RSI de 1H en 31.7 aproximándose a niveles de sobreventa y un cambio pos... |
| `2026-10-13 19:40` | 🔴 SELL (-0.10$) | `SOL-USD` | $29.86 | $106.84 | SOL-USD lleva más de 5 horas de holding sin mostrar el rebote esperado, operando bajo la S... |
| `2026-10-13 17:10` | 🟢 BUY | `ETH-USD` | $5.00 | $2508.37 | ETH-USD se encuentra en zona de sobreventa técnica con un RSI de 35.9 y un cambio positivo... |
| `2026-10-13 17:00` | 🔴 SELL | `ETH-USD` | $9.67 | $2506.14 | ETH-USD ha registrado un rebote diario del 2.53% acercándose a una zona de neutralidad a c... |

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
