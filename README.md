# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 18:40:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.68 USD** | **$34.91 USD** | **$39.59 USD** | 🔴 **-1.02%** ($-0.41) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.279466 | $107.20 | $107.01 | $29.91 | 📉 -0.17% | 4h 39m |
| `ETH-USD` | 0.001993 | $2508.37 | $2509.75 | $5.00 | 📈 +0.06% | 1h 30m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se mantiene abierto operando en un rango lateral con sesgo bajista general pero con intentos de estabilización. Las principales criptomonedas (ETH, SOL, BTC) muestran indicadores de RSI de 1 hora saliendo de zonas profundas de sobreventa (en torno a 37-39), lo que sugiere que los rebotes técnicos de corto plazo siguen vigentes. Los mercados tradicionales permanecen cerrados, por lo que toda la atención se centra en mantener la exposición activa en crypto y gestionar el riesgo."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición en SOL-USD lleva 4 horas y 39 minutos abierta con una pérdida mínima del -0.17%. El RSI de 1 hora se sitúa en 37.8 intentando consolidar un rebote desde soportes macro diarios. Se mantiene para permitir que el momentum alcista alcance la zona de take-profit.
- **[HOLD] ETH-USD** (Confianza: 75%): La posición en ETH-USD registra una ganancia marginal del +0.06% tras 1 hora y 30 minutos de holding. El RSI de 1 hora se recupera hacia 39.7 y el cambio diario es positivo (+2.68%). Se mantiene con objetivo de capturar el tramo final hacia la zona de take-profit del +2.0%.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas en SOL-USD y ETH-USD ya que se encuentran estables y dentro del rango de tolerancia al riesgo antes del stop-loss de -2.0%. El efectivo disponible se encuentra en el límite mínimo operativo. Monitorear de cerca la evolución del RSI de 1 hora para ejecutar tomas de beneficios (take-profit) si alcanzan el rango de +2.0% a +3.5%, o recortar de inmediato si la tendencia bajista se acelera superando los límites de pérdida permitidos."
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
