# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 23:10:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.20 USD** | **$38.25 USD** | 🔴 **-4.38%** ($-1.75) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81560.04 | $10.05 | 📈 +0.48% | 4h 9m |
| `SOL-USD` | 0.097418 | $102.65 | $103.39 | $10.07 | 📈 +0.72% | 3h 59m |
| `ETH-USD` | 0.004193 | $2385.05 | $2404.64 | $10.08 | 📈 +0.82% | 3h 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que toda la actividad se concentra en los criptoactivos (BTC-USD, ETH-USD, SOL-USD), que operan 24/7. Las posiciones actuales muestran una ligera recuperación en terreno positivo pero con un momentum de 1 hora moderado y sin alcanzar todavía el objetivo de take-profit del +2.0% al +3.5%. Mantenemos las posiciones abiertas esperando un nuevo impulso en las próximas horas."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): La posición muestra un rendimiento positivo moderado del 0.48% y un RSI de 1 hora en 51.6. Mantenemos la posición a la espera de que el precio alcance el objetivo de take-profit entre +2.0% y +3.5%.
- **[HOLD] SOL-USD** (Confianza: 80%): La posición acumula un rendimiento positivo de 0.72% con un RSI de 1 hora en 34.7. Mantenemos la posición vigente para permitir que el rebote táctico continúe hacia nuestra zona de take-profit.
- **[HOLD] ETH-USD** (Confianza: 80%): La posición se mantiene en terreno positivo con un 0.82% de beneficio y un RSI de 1 hora en 30.7. Mantenemos la posición activa respetando el stop-loss de -2.0% y esperando el objetivo de ganancia.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Continuar monitoreando las posiciones actuales en BTC-USD, ETH-USD y SOL-USD. El plan táctico es mantenerlas firmemente mientras no activen el stop-loss de -2.0% y buscar asegurar beneficios parciales o totales tan pronto como alcancen el rango de ganancia de +2.0% a +3.5% o si el RSI de 1 hora cruza el nivel de sobrecompra (>70). No realizar nuevas compras en este ciclo para preservar la liquidez."
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
