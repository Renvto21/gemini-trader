# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 03:40:38`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.26 USD** | **$38.31 USD** | 🔴 **-4.23%** ($-1.69) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81651.06 | $10.06 | 📈 +0.59% | 8h 39m |
| `SOL-USD` | 0.097418 | $102.65 | $103.62 | $10.09 | 📈 +0.94% | 8h 29m |
| `ETH-USD` | 0.004193 | $2385.05 | $2411.21 | $10.11 | 📈 +1.10% | 8h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se mantiene abierto 24/7 con un comportamiento moderadamente alcista en las últimas horas tras los rebotes iniciados en el ciclo previo. Las posiciones en BTC-USD, SOL-USD y ETH-USD muestran ganancias moderadas pero aún se encuentran por debajo del rango objetivo de take-profit de +2.0% a +3.5%. Los activos tradicionales (acciones y ETFs) se encuentran cerrados y con baja tendencia o sobreventa técnica estancada, por lo que el foco operativo sigue plenamente en las criptomonedas."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): BTC-USD muestra una ganancia actual de +0.59% con un RSI de 1H en 63.0. Continúa el rebote esperado pero aún no alcanza el objetivo de take-profit de +2.0% a +3.5%. Se mantiene la posición para dejar correr los beneficios.
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD registra un PnL positivo de +0.94% con un RSI de 1H en 54.3. El impulso técnico se mantiene intacto dentro del plan táctico, por lo que se mantiene la posición en busca de la zona de toma de ganancias.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD presenta una rentabilidad actual de +1.10% con un RSI de 1H en 54.4. La posición evoluciona favorablemente según lo planeado y se mantiene en cartera para capturar el objetivo completo de ganancias.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en BTC-USD, SOL-USD y ETH-USD mientras continúan su movimiento de recuperación hacia el objetivo de take-profit de +2.0% a +3.5%. Monitorear de cerca los niveles de RSI de 1 hora para asegurar beneficios si se acercan a la zona de sobrecompra (>70). Mantener activo el stop-loss estricto a -2.0% para proteger el capital ante cualquier reversión imprevista."
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
