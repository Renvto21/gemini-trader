# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 18:30:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.68 USD** | **$34.87 USD** | **$39.55 USD** | 🔴 **-1.13%** ($-0.45) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.279466 | $107.20 | $106.89 | $29.87 | 📉 -0.29% | 4h 29m |
| `ETH-USD` | 0.001993 | $2508.37 | $2506.20 | $5.00 | 📉 -0.09% | 1h 20m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que el foco se concentra 100% en las criptomonedas (SOL-USD, ETH-USD y BTC-USD). El sentimiento general en cripto muestra un movimiento lateral a la baja en la última hora, con RSI de 1 hora oscilando alrededor de 36-37, lo que indica falta de momentum inmediato para un rebote agresivo pero manteniendo soportes técnicos cercanos."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición en SOL-USD lleva 4 horas y 29 minutos abierta con una pérdida marginal de -0.29%, manteniéndose muy por encima del stop-loss estricto de -2.0%. El RSI de 1 hora está en 37.1 y el cambio diario es positivo (+1.26%), por lo que se mantiene la postura de esperar un nuevo impulso alcista.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD presenta una pérdida prácticamente nula (-0.09%) tras 1 hora y 20 minutos de haber sido abierta. Con un RSI de 1 hora en 37.5 y un rendimiento diario del +2.53%, el activo muestra resiliencia y mantiene potencial para buscar la zona de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en SOL-USD y ETH-USD ya que se encuentran dentro de un rango de pérdida aceptable (lejos del stop-loss de -2.0%). El efectivo disponible se mantendrá intacto ($4.68 USD) cumpliendo con la reserva mínima. Monitorear de cerca el RSI de 1 hora en busca de un cruce alcista que permita capturar la zona de take-profit entre +2.0% y +3.5%."
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
