# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 06:00:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.21 USD** | **$38.25 USD** | 🔴 **-4.37%** ($-1.75) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81642.21 | $10.06 | 📈 +0.58% | 10h 59m |
| `SOL-USD` | 0.097418 | $102.65 | $103.13 | $10.05 | 📈 +0.47% | 10h 50m |
| `ETH-USD` | 0.004193 | $2385.05 | $2409.06 | $10.10 | 📈 +1.01% | 10h 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene operando 24/7 con un comportamiento lateral pero positivo. Las posiciones abiertas en BTC-USD, SOL-USD y ETH-USD muestran ganancias moderadas (entre +0.47% y +1.01%) tras haber cazado el rebote técnico en sobreventa. Los mercados tradicionales de Wall Street se encuentran cerrados, por lo que toda la atención táctica se centra en consolidar estas posiciones y asegurar beneficios si el momentum se acelera hacia el rango de +2.0% a +3.5%."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): BTC-USD se encuentra en terreno positivo con una ganancia actual de +0.58%. El RSI de 1H se estabiliza en 54.9 y el precio se mantiene por encima del promedio de compra inicial. Mantenemos la posición a la espera de que se acerque al objetivo de take-profit del +2.0%.
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD registra una ganancia moderada de +0.47% tras casi 11 horas de holding. Aunque la tendencia diaria es bajista, el rebote técnico intradiario sigue activo. Mantenemos la posición respetando la disciplina de stop-loss y take-profit.
- **[HOLD] ETH-USD** (Confianza: 85%): ETH-USD lidera las ganancias del portafolio con un rendimiento actual de +1.01% y un precio de 2409.06. Nos acercamos progresivamente a la zona de toma de ganancias (+2.0% a +3.5%). Mantenemos la posición activa para maximizar el impulso alcista actual.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en BTC-USD, SOL-USD y ETH-USD ya que se encuentran en terreno positivo. El objetivo para los siguientes ciclos es vigilar de cerca el RSI de 1H y 24H: si ETH-USD u otro activo alcanza el rango objetivo de take-profit (+2.0% a +3.5%) o entra en sobrecompra (RSI 1H > 70), procederemos a vender de inmediato para realizar beneficios y acumular liquidez. El stop-loss estricto permanece anclado en una pérdida del -2.0% por posición."
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
