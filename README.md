# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 19:10:36`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.68 USD** | **$34.88 USD** | **$39.56 USD** | 🔴 **-1.11%** ($-0.44) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.279466 | $107.20 | $106.91 | $29.88 | 📉 -0.27% | 5h 9m |
| `ETH-USD` | 0.001993 | $2508.37 | $2507.34 | $5.00 | 📉 -0.04% | 1h 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene operando 24/7 con un tono mixto a consolidación de corto plazo. SOL-USD y ETH-USD muestran RSI de 1 hora neutrales (~44) tras los rebotes recientes, encontrándose todavía bajo sus medias móviles de 20 días en gráfico diario, pero manteniendo soportes clave. Los mercados tradicionales están cerrados, por lo que toda la atención táctica se centra en la gestión de las posiciones actuales."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición en SOL-USD acumula una pérdida menor de -0.27% tras 5 horas abierta. Se mantiene dentro de los parámetros de riesgo aceptables y el RSI diario en 26.8 sugiere que sigue en zona de sobreventa con potencial de rebote hacia objetivos de +2.0%.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra estabilidad con una pérdida marginal de -0.04% tras casi 2 horas desde su reentrada. Se mantiene en cartera a la espera de un impulso alcista que active el take-profit fijado entre +2.0% y +3.5%.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener posiciones de SOL-USD y ETH-USD vigentes buscando el objetivo de take-profit entre +2.0% y +3.5% o protegiendo capital ante un quiebre del stop-loss estricto en -2.0%. Estar alerta a un incremento en el RSI de 1 hora por encima de 70 para realizar tomas de beneficios y liberar capital."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **47** | 🎯 **46.8%** (22W / 11L / 14BE) | 🔴 **$-0.28 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 17:10` | 🟢 BUY | `ETH-USD` | $5.00 | $2508.37 | ETH-USD se encuentra en zona de sobreventa técnica con un RSI de 35.9 y un cambio positivo... |
| `2026-10-13 17:00` | 🔴 SELL | `ETH-USD` | $9.67 | $2506.14 | ETH-USD ha registrado un rebote diario del 2.53% acercándose a una zona de neutralidad a c... |
| `2026-10-13 16:30` | 🟢 BUY | `ETH-USD` | $9.68 | $2507.92 | ETH-USD muestra un RSI de 35.8 en zona de fuerte sobreventa y un impulso alcista diario de... |
| `2026-10-13 16:30` | 🔴 SELL | `SOL-USD` | $9.69 | $107.65 | Realizamos una toma parcial de beneficios y rotación de capital liberando aproximadamente ... |
| `2026-10-13 14:01` | 🟢 BUY | `SOL-USD` | $7.97 | $107.29 | SOL-USD presenta una condición de sobreventa extrema con un RSI de 27.9 y un desplome sema... |

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
