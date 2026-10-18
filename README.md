# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 21:30:47`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.12 USD** | **$38.17 USD** | 🔴 **-4.57%** ($-1.83) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81331.15 | $10.02 | 📈 +0.20% | 2h 30m |
| `SOL-USD` | 0.097418 | $102.65 | $103.18 | $10.05 | 📈 +0.52% | 2h 20m |
| `ETH-USD` | 0.004193 | $2385.05 | $2397.69 | $10.05 | 📈 +0.53% | 2h 20m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que la operativa se concentra 100% en las criptomonedas (BTC-USD, ETH-USD, SOL-USD) que operan 24/7. Las posiciones actuales muestran ligeras ganancias marginales (entre +0.2% y +0.53%), pero los indicadores de 1 hora (cambios negativos recientes y RSI acercándose nuevamente a zonas de soporte) reflejan un momentum de corto plazo plano a ligeramente bajista. No se han alcanzado los objetivos de take-profit (+2.0% a +3.5%) ni los niveles de stop-loss (-2.0%), por lo que se decide mantener las posiciones actuales mientras se consolida la estructura de precios."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 75%): La posición mantiene un beneficio menor de +0.20% tras 2.5 horas de holding. El RSI de 1H está en 39.7 y no ha dado señal clara de salida ni ha alcanzado el take-profit deseado, por lo que se mantiene para permitir que el rebote continúe.
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD registra una ganancia del +0.52%. A pesar de un leve retroceso en la última hora, se mantiene por encima del precio de entrada y dentro del rango operativo seguro, esperando el catalizador alcista hacia el objetivo de take-profit.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra un rendimiento positivo de +0.53%. Mantenemos la posición abierta ya que no se han activado ni el take-profit ni el stop-loss, y el sesgo técnico de soporte diario sigue vigente.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en BTC-USD, SOL-USD y ETH-USD durante este ciclo. Monitorear de cerca el RSI de 1H; si las ganancias rozan el rango de +2.0% a +3.5% o el RSI supera los 70 puntos, ejecutaremos take-profit inmediato para asegurar liquidez. Si el momentum se deteriora y alguna posición vulnera el -1.5% o -2.0% de pérdida, aplicaremos stop-loss preventivo."
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
