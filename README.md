# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 20:10:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$34.54 USD** | **$4.98 USD** | **$39.52 USD** | 🔴 **-1.21%** ($-0.48) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001993 | $2508.37 | $2497.10 | $4.98 | 📉 -0.45% | 3h 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra completamente cerrado, por lo que toda la atención y liquidez disponible deben concentrarse estrictamente en los activos criptográficos (ETH-USD, BTC-USD y SOL-USD) que operan 24/7. ETH-USD se mantiene abierto en cartera con un rendimiento actual de -0.45% tras casi 3 horas de tenencia, mostrando un RSI de 1H en 40.9 y un RSI diario en 34.6, lo que indica que sigue comprimido cerca de soportes. BTC-USD y SOL-USD muestran ligeros retrocesos intradiarios pero mantienen un sesgo de consolidación. Dado que la posición actual en ETH-USD no ha alcanzado ni su stop-loss estricto (-2.0%) ni su objetivo de take-profit (+2.0% a +3.5%), optamos por mantenerla activa mientras evaluamos nuevas entradas si el impulso mejora."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 70%): La posición en ETH-USD lleva cerca de 3 horas abierta con una pérdida marginal de -0.45%, manteniéndose muy por encima del stop-loss estricto de -2.0%. Esperamos que el rebote técnico se materialice hacia la zona de objetivos de ganancia (+2.0% a +3.5%).

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener la posición actual en ETH-USD vigilando de cerca el soporte en la zona de 2490 USD. El stop-loss se mantiene estricto en -2.0% y buscaremos la toma de beneficios si alcanza el rango de +2.0% a +3.5% o si el RSI de 1H supera los 70 puntos. Mantener liquidez disponible y no realizar nuevas entradas hasta que se confirme un cruce alcista o un repunte claro en el RSI de 1H en los activos cripto."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **48** | 🎯 **45.8%** (22W / 12L / 14BE) | 🔴 **$-0.38 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 19:40` | 🔴 SELL (-0.10$) | `SOL-USD` | $29.86 | $106.84 | SOL-USD lleva más de 5 horas de holding sin mostrar el rebote esperado, operando bajo la S... |
| `2026-10-13 17:10` | 🟢 BUY | `ETH-USD` | $5.00 | $2508.37 | ETH-USD se encuentra en zona de sobreventa técnica con un RSI de 35.9 y un cambio positivo... |
| `2026-10-13 17:00` | 🔴 SELL | `ETH-USD` | $9.67 | $2506.14 | ETH-USD ha registrado un rebote diario del 2.53% acercándose a una zona de neutralidad a c... |
| `2026-10-13 16:30` | 🟢 BUY | `ETH-USD` | $9.68 | $2507.92 | ETH-USD muestra un RSI de 35.8 en zona de fuerte sobreventa y un impulso alcista diario de... |
| `2026-10-13 16:30` | 🔴 SELL | `SOL-USD` | $9.69 | $107.65 | Realizamos una toma parcial de beneficios y rotación de capital liberando aproximadamente ... |

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
