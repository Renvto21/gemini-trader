# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 21:00:48`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.15 USD** | **$38.19 USD** | 🔴 **-4.51%** ($-1.81) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81358.49 | $10.02 | 📈 +0.23% | 2h 0m |
| `SOL-USD` | 0.097418 | $102.65 | $103.34 | $10.07 | 📈 +0.67% | 1h 50m |
| `ETH-USD` | 0.004193 | $2385.05 | $2398.78 | $10.06 | 📈 +0.58% | 1h 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene operando 24/7 mientras los activos tradicionales de Wall Street permanecen cerrados. Las criptomonedas principales (BTC-USD, ETH-USD, SOL-USD) muestran ligeros retrocesos en la última hora con el RSI de 1H comprimiéndose cerca de los niveles iniciales de entrada, manteniendo una estructura de rebote latente pero con bajo momentum a corto plazo. No se han alcanzado los objetivos de Take-Profit (+2.0%), por lo que se decide mantener las posiciones actuales a la espera de una expansión de volatilidad alcista."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 75%): La posición en BTC-USD se mantiene en terreno ligeramente positivo (+0.23%) tras casi dos horas. El RSI de 1H se sitúa en 39.8 sin señales de debilidad extrema, por lo que se mantiene para buscar el objetivo de take-profit.
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD muestra un PnL positivo de +0.67% y un RSI de 1H en 31.8. Se mantiene la posición intacta a la espera de un impulso alcista que permita asegurar ganancias parciales.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD registra un PnL de +0.58% con un RSI de 1H en 30.3. La posición cumple con el plan táctico inicial y se retiene mientras no se acerque al stop-loss o alcance la zona de sobrecompra.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales (BTC-USD, SOL-USD, ETH-USD) ya que se encuentran estables dentro del rango de tolerancia y sin tocar el stop-loss de -2.0%. Estar atentos en los próximos ciclos a que el RSI de 1H supere los niveles de 60-70 o que el PnL alcance el objetivo de +2.0% para realizar tomas de beneficio. Si el momentum se erosiona aún más o rompe soportes clave, se procederá a cortar pérdidas de forma estricta."
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
