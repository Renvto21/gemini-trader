# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 20:40:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.08 USD** | **$38.13 USD** | 🔴 **-4.67%** ($-1.87) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81225.00 | $10.01 | 📈 +0.07% | 1h 39m |
| `SOL-USD` | 0.097418 | $102.65 | $103.05 | $10.04 | 📈 +0.39% | 1h 29m |
| `ETH-USD` | 0.004193 | $2385.05 | $2394.15 | $10.04 | 📈 +0.38% | 1h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene operando 24/7 con un sesgo lateral a ligeramente alcista en las últimas horas tras los rebotes iniciales. Las posiciones en BTC-USD, SOL-USD y ETH-USD muestran ligeras ganancias positivas (+0.07% a +0.39%), pero el RSI de 1H de estos activos aún no alcanza la zona de sobrecompra (> 70) que justifique una toma de beneficios por objetivos de +2.0% a +3.5%. Los mercados tradicionales (Wall Street) se encuentran cerrados, por lo que la liquidez está completamente concentrada en mantener y evaluar el comportamiento de las criptomonedas abiertas."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 75%): BTC-USD se mantiene estable con una ganancia marginal del 0.07% tras 1.6 horas de tenencia. El RSI de 1H se ubica en 42.5 y no ha alcanzado la zona de take-profit óptima, mientras se mantiene alejado del stop-loss.
- **[HOLD] SOL-USD** (Confianza: 78%): SOL-USD muestra un comportamiento positivo con una ganancia actual de +0.39%. El precio se sostiene bien sobre el nivel de entrada, por lo que se mantiene la posición en busca de un mayor impulso alcista hacia el objetivo de +2.0%.
- **[HOLD] ETH-USD** (Confianza: 78%): ETH-USD mantiene una rentabilidad positiva de +0.38%. El rebote técnico sigue su curso y no existen señales de debilidad estructural que fuercen una salida anticipada antes de los objetivos previstos.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales (BTC-USD, SOL-USD, ETH-USD) ya que se encuentran estables con pequeñas ganancias y no han tocado el stop-loss estricto (-2.0%). Esperar a que el RSI de 1H alcance niveles superiores a 60-70 o que el PnL llegue al objetivo de +2.0% para realizar tomas de beneficio y liberar efectivo. Monitorear de cerca el impulso de corto plazo en los siguientes ciclos."
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
