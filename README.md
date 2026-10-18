# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 05:50:37`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.17 USD** | **$38.21 USD** | 🔴 **-4.46%** ($-1.79) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81590.52 | $10.05 | 📈 +0.52% | 10h 49m |
| `SOL-USD` | 0.097418 | $102.65 | $102.95 | $10.03 | 📈 +0.29% | 10h 39m |
| `ETH-USD` | 0.004193 | $2385.05 | $2405.80 | $10.09 | 📈 +0.87% | 10h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene operando 24/7 con un tono moderado y lateral, mientras que los activos tradicionales de Wall Street permanecen cerrados. Nuestras posiciones actuales en BTC-USD, SOL-USD y ETH-USD muestran ganancias moderadas pero estables tras el rebote inicial, aunque aún no alcanzan la zona de take-profit del +2.0% al +3.5%."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): BTC-USD se encuentra en terreno positivo con un PnL de +0.52% tras casi 11 horas de holding. El RSI de 1H en 55.7 muestra estabilidad y no amerita venta todavía, esperando alcanzar el objetivo de take-profit de +2.0% o superior.
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD mantiene un PnL positivo de +0.29%. A pesar de un ligero cambio negativo de -0.22% en la última hora, el precio sigue respetando la zona de rebote y no ha activado los parámetros de stop-loss.
- **[HOLD] ETH-USD** (Confianza: 82%): ETH-USD lidera las ganancias actuales del portafolio con un PnL de +0.87%. Mantiene un buen impulso técnico y se aproxima adecuadamente al rango objetivo de toma de ganancias.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en BTC-USD, SOL-USD y ETH-USD dado que se encuentran en zona positiva y sin señales de reversión bajista. El objetivo es mantener el monitoreo continuo para asegurar ganancias al llegar al rango de +2.0% a +3.5% de beneficio, o recortar de inmediato si se observa pérdida de momentum o ruptura del soporte del -2.0%. La liquidez se mantiene operativamente ajustada."
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
