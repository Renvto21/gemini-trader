# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 04:20:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.23 USD** | **$38.27 USD** | 🔴 **-4.32%** ($-1.73) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81596.75 | $10.05 | 📈 +0.52% | 9h 19m |
| `SOL-USD` | 0.097418 | $102.65 | $103.49 | $10.08 | 📈 +0.82% | 9h 9m |
| `ETH-USD` | 0.004193 | $2385.05 | $2406.80 | $10.09 | 📈 +0.91% | 9h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se mantiene abierto 24/7 mostrando un rebote moderado tras las compras recientes. Las posiciones actuales en BTC-USD, SOL-USD y ETH-USD registran ganancias moderadas entre +0.52% y +0.91%, aproximándose de manera favorable a nuestra zona objetivo de toma de ganancias de +2.0% a +3.5%. Los indicadores RSI de 1 hora se han estabilizado en rangos neutrales saludables, mientras que el mercado tradicional permanece cerrado. Mantendremos el plan táctico actual sin forzar nuevas entradas para permitir que el capital desplegado continúe su evolución."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): La posición muestra un rendimiento positivo del 0.52% tras 9 horas de haber sido abierta. El RSI de 1 hora se encuentra en 59.1, lo que indica un desarrollo favorable hacia nuestro objetivo de take-profit sin señales de agotamiento inmediato. Mantenemos la posición para capturar la ganancia esperada.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas en BTC-USD, SOL-USD y ETH-USD vigilando de cerca su evolución hacia el objetivo de take-profit de +2.0% a +3.5% o hasta que el RSI de 1 hora alcance la zona de sobrecompra superior a 70. El stop-loss estricto a -2.0% permanece activo como mecanismo de protección de capital. No se realizarán nuevas operaciones en este ciclo con el fin de preservar la liquidez disponible y evaluar la estabilidad del impulso alcista actual."
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
