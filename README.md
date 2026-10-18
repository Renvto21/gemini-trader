# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 07:40:37`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.39 USD** | **$38.43 USD** | 🔴 **-3.92%** ($-1.57) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $82062.52 | $10.11 | 📈 +1.10% | 12h 39m |
| `SOL-USD` | 0.097418 | $102.65 | $104.01 | $10.13 | 📈 +1.32% | 12h 29m |
| `ETH-USD` | 0.004193 | $2385.05 | $2419.17 | $10.14 | 📈 +1.43% | 12h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se mantiene abierto y operando con un sentimiento mixto pero favorable para nuestras posiciones de rebote. Bitcoin, Ethereum y Solana muestran rendimientos positivos en las últimas 24 horas y se aproximan progresivamente a nuestras zonas objetivo de toma de beneficios, aunque el RSI de 1H se ha estabilizado en rangos neutrales sin alcanzar todavía la sobrecompra extrema (>70). Los mercados tradicionales permanecen cerrados, por lo que toda la atención táctica se centra en la gestión del cripto-portafolio."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 75%): La posición en BTC-USD muestra una ganancia actual de +1.1% y un RSI de 1H en 62.8. Aunque se acerca a la zona de toma de beneficios, aún no alcanza el objetivo mínimo de +2.0% a +3.5%, por lo que se mantiene para permitir que el rebote madure.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendré las posiciones actuales en BTC-USD, SOL-USD y ETH-USD ya que se encuentran en terreno positivo (+1.1% a +1.4%) pero aún no alcanzan el objetivo de take-profit de +2.0% a +3.5%. Monitorearé de cerca el comportamiento del RSI de 1H y el precio de cada activo; si alguno de ellos roza o supera el umbral de take-profit o muestra signos de agotamiento, procederé a vender de inmediato para asegurar efectivo y rotar el capital. No se realizarán nuevas compras en este ciclo para preservar la liquidez actual por encima de la reserva mínima."
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
