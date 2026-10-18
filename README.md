# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 04:40:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.20 USD** | **$38.24 USD** | 🔴 **-4.39%** ($-1.76) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81589.11 | $10.05 | 📈 +0.52% | 9h 39m |
| `SOL-USD` | 0.097418 | $102.65 | $103.20 | $10.05 | 📈 +0.54% | 9h 29m |
| `ETH-USD` | 0.004193 | $2385.05 | $2407.15 | $10.09 | 📈 +0.93% | 9h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene operando 24/7 con una ligera estabilidad en las posiciones principales (BTC, ETH y SOL), aunque con un momentum de corto plazo moderado tras casi 10 horas de retención. Los activos de Wall Street se encuentran cerrados, por lo que la liquidez y las operaciones se concentran exclusivamente en el sector cripto. Las posiciones actuales muestran ganancias moderadas pero aún no alcanzan el objetivo de take-profit óptimo del +2.0% al +3.5%."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 70%): La posición muestra un rendimiento positivo de +0.52% tras casi 10 horas, operando de manera estable. Se mantiene para buscar el objetivo de take-profit completo.
- **[HOLD] SOL-USD** (Confianza: 70%): SOL-USD registra una ganancia moderada de +0.54% y se mantiene dentro de los parámetros esperados de rebote técnico a la espera de mayor impulso.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD lidera las posiciones con un beneficio actual de +0.93%, acercándose progresivamente al rango de toma de ganancias táctico sin mostrar señales de debilidad.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas en BTC-USD, SOL-USD y ETH-USD por un ciclo más debido a que muestran rendimientos positivos estables. Vigilar de cerca el indicador RSI de 1 hora y el avance de los precios hacia la zona de take-profit objetivo (+2.0% a +3.5%). El stop-loss estricto a -2.0% continúa activo como salvaguarda ante cualquier reversión inesperada. No se realizarán nuevas compras en este ciclo para preservar la liquidez mínima requerida."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **67** | 🎯 **38.8%** (26W / 27L / 14BE) | 🔴 **$-1.84 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-17 19:10` | 🟢 BUY | `ETH-USD` | $10.00 | $2385.05 | ETH-USD muestra un RSI de 1H en 29.0 (sobreventa profunda) combinado con un cambio de 1h p... |
| `2026-10-17 19:10` | 🟢 BUY | `SOL-USD` | $10.00 | $102.65 | SOL-USD presenta un RSI de 1H en 31.5 saliendo de zona de sobreventa estricta y un cambio ... |
| `2026-10-17 19:00` | 🟢 BUY | `BTC-USD` | $10.00 | $81170.65 | BTC-USD muestra un RSI de 1H saliendo de niveles bajos (37.5) con un cambio positivo de 0.... |
| `2026-10-17 18:40` | 🔴 SELL (-0.22$) | `ETH-USD` | $9.78 | $2370.09 | La posición acumula una pérdida de -2.21%, excediendo el umbral de stop-loss del -2.0%. El... |
| `2026-10-17 18:40` | 🔴 SELL (-0.21$) | `SOL-USD` | $9.79 | $101.78 | La posición ha alcanzado una pérdida de -2.08%, rompiendo el límite de stop-loss estricto ... |

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
