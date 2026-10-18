# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 23:20:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.22 USD** | **$38.26 USD** | 🔴 **-4.34%** ($-1.74) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81567.52 | $10.05 | 📈 +0.49% | 4h 19m |
| `SOL-USD` | 0.097418 | $102.65 | $103.49 | $10.08 | 📈 +0.82% | 4h 9m |
| `ETH-USD` | 0.004193 | $2385.05 | $2405.38 | $10.09 | 📈 +0.85% | 4h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene operando 24/7 con una ligera estabilidad en las posiciones actuales (BTC-USD, SOL-USD, ETH-USD), las cuales muestran ganancias moderadas entre +0.49% y +0.85% tras el rebote inicial. El RSI de 1 hora se encuentra neutralizado en rangos medios (42-54), lejos de la zona de sobrecompra requerida para tomar beneficios (+2.0% a +3.5%) y lejos del stop-loss de -2.0%. Los mercados tradicionales (Wall Street) permanecen cerrados. La liquidez disponible es baja ($8.05 USD), por lo que la prioridad es mantener las posiciones abiertas actuales y gestionar la reserva de efectivo."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): La posición mantiene una ganancia moderada de +0.49% con un holding time de poco más de 4 horas. El RSI de 1 hora se encuentra en 54.3, por debajo del objetivo de sobrecompra (>70) para take-profit, y el precio está por encima del nivel de entrada. Mantenemos para buscar el objetivo de +2.0%.
- **[HOLD] SOL-USD** (Confianza: 80%): La posición registra una ganancia de +0.82%. El RSI de 1 hora está en 47.3 y no ha activado ninguna señal de salida ni de take-profit. Se mantiene operativa dentro del plan táctico.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD muestra un beneficio actual de +0.85% con un RSI de 1 hora en 42.3. Se conserva en cartera a la espera de un mayor impulso alcista que permita asegurar ganancias en el rango del +2.0% al +3.5%.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener firmemente las posiciones abiertas en BTC-USD, SOL-USD y ETH-USD durante este ciclo. Monitorear de cerca los niveles de ganancia para ejecutar take-profit tan pronto como alcancen el rango de +2.0% a +3.5% o si el RSI de 1 hora cruza el nivel de sobrecompra (>70). Mantener activo el stop-loss estricto a -2.0% para proteger el capital. No realizar nuevas operaciones en este ciclo para preservar la liquidez mínima requerida de $4.00 USD."
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
