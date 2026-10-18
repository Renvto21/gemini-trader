# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 00:20:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.31 USD** | **$38.36 USD** | 🔴 **-4.11%** ($-1.64) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81726.26 | $10.07 | 📈 +0.68% | 5h 19m |
| `SOL-USD` | 0.097418 | $102.65 | $103.78 | $10.11 | 📈 +1.10% | 5h 9m |
| `ETH-USD` | 0.004193 | $2385.05 | $2416.08 | $10.13 | 📈 +1.30% | 5h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de valores tradicional se encuentra cerrado, por lo que toda la operativa se concentra exclusivamente en el mercado de criptomonedas (24/7). Las posiciones abiertas en BTC, SOL y ETH han mostrado un avance positivo recuperando terreno, con rendimientos actuales de +0.68%, +1.1% y +1.3% respectivamente, acercándose a la zona objetivo de take-profit del ciclo pero sin alcanzar aún el umbral crítico del +2.0%. Mantendremos la vigilancia activa esperando que el impulso continúe o procederemos a vender si rozan los objetivos de ganancia."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): BTC-USD mantiene un rendimiento positivo de +0.68% con un RSI de 1H en 58.7. Está evolucionando favorablemente pero aún no alcanza la zona de take-profit de +2.0%, por lo que se mantiene la posición.
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD registra una ganancia actual de +1.1% con un RSI de 1H en 49.6. El rebote técnico va por buen camino y se mantiene en cartera a la espera de llegar al objetivo de ganancia.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD lidera las ganancias del portafolio con +1.3% y un RSI de 1H en 48.3. Se mantiene la posición para permitir que alcance el objetivo de take-profit entre +2.0% y +3.5%.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales (BTC-USD, SOL-USD, ETH-USD) en este ciclo ya que muestran un comportamiento estable y positivo tras más de 5 horas abiertas. Monitorear de cerca si alguna posición alcanza el rango de beneficio del +2.0% al +3.5% para proceder con la toma de ganancias y rotar liquidez. El stop-loss permanece estricto en -2.0% para proteger el capital. No se abren nuevas posiciones por ahora para consolidar el portafolio."
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
