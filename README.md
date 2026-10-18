# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 05:30:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.18 USD** | **$38.22 USD** | 🔴 **-4.44%** ($-1.78) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81583.34 | $10.05 | 📈 +0.51% | 10h 29m |
| `SOL-USD` | 0.097418 | $102.65 | $103.03 | $10.04 | 📈 +0.37% | 10h 19m |
| `ETH-USD` | 0.004193 | $2385.05 | $2406.11 | $10.09 | 📈 +0.88% | 10h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de Wall Street se encuentra cerrado, por lo que la liquidez y las operaciones activas se concentran exclusivamente en el mercado de criptomonedas (ABIERTO 24/7). Las posiciones actuales en BTC-USD, SOL-USD y ETH-USD muestran rendimientos positivos pero moderados (entre +0.37% y +0.88%), manteniéndose por debajo del objetivo de take-profit del +2.0%. Los indicadores en 1H se han estabilizado tras el rebote inicial, por lo que mantendremos el rumbo actual a la espera de un mayor impulso alcista."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): BTC-USD se encuentra en terreno positivo con una ganancia de 0.51% y un RSI de 1H en 55.5. Aún no alcanza el objetivo de take-profit de +2.0%, por lo que mantenemos la posición para dejar correr las ganancias.
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD mantiene una ganancia moderada de 0.37% con un RSI de 1H en 44.1. Mantenemos la posición a la espera de un mayor impulso alcista hacia el rango de take-profit.
- **[HOLD] ETH-USD** (Confianza: 85%): ETH-USD lidera el portafolio con una ganancia de 0.88% y un RSI de 1H en 46.9. Está progresando adecuadamente hacia el objetivo de take-profit, por lo que se mantiene abierta.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en BTC-USD, SOL-USD y ETH-USD durante este ciclo ya que se encuentran en terreno positivo sin activar ningún stop-loss. Seguiremos monitoreando la acción del precio para asegurar beneficios tan pronto como alcancen el rango de take-profit de +2.0% a +3.5%. La reserva de efectivo se mantiene estricta en el nivel operativo mínimo."
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
