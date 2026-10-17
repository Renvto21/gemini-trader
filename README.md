# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 15:30:55`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.48 USD** | **$19.95 USD** | **$38.42 USD** | 🔴 **-3.94%** ($-1.58) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096209 | $103.94 | $103.74 | $9.98 | 📉 -0.19% | 5h 10m |
| `ETH-USD` | 0.004126 | $2423.75 | $2416.08 | $9.97 | 📉 -0.32% | 3h 40m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas continúa operando con un sentimiento mixto y tendencia general bajista bajo la SMA20, pero con señales claras de consolidación y soporte macro diario en sobreventa para activos como SOL-USD y ETH-USD. Los mercados tradicionales están cerrados, por lo que toda la atención táctica se centra en la liquidez 24/7 de las criptos para capturar rebotes por mean reversion."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición lleva unas horas abierta con una leve fluctuación (-0.19%), manteniendo el soporte en RSI diario de sobreventa y registrando un cambio positivo de 1h del 0.41%. Esperamos el desarrollo del rebote técnico.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD mantiene un comportamiento similar, con un PnL de -0.32% y un cambio positivo de 1h de 0.31%. El RSI diario profundamente en sobreventa sugiere potencial alcista continuo a corto plazo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas de SOL-USD y ETH-USD ya que se encuentran estables con pérdidas mínimas y mostrando ligeros incrementos en el momentum de 1 hora. Monitorear el RSI de 1 hora para asegurar beneficios parciales al alcanzar la zona de +2.0% a +3.5% o sobrecompra (>70). Mantener un stop-loss estricto si las pérdidas superan el -2.0% y conservar la liquidez en efectivo por encima del mínimo requerido de $4.00 USD."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **65** | 🎯 **40.0%** (26W / 25L / 14BE) | 🔴 **$-1.41 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-17 11:50` | 🟢 BUY | `ETH-USD` | $10.00 | $2423.75 | ETH-USD presenta un RSI diario en niveles de sobreventa profunda (28.9) y un cambio positi... |
| `2026-10-17 10:20` | 🟢 BUY | `SOL-USD` | $10.00 | $103.94 | SOL-USD presenta un RSI diario en niveles de sobreventa extrema (22.5) y un cambio positiv... |
| `2026-10-17 04:30` | 🔴 SELL (+0.12$) | `SOL-USD` | $10.12 | $104.94 | SOL-USD ha alcanzado un RSI de 1 hora de 70.4, entrando en zona de sobrecompra, y acumula ... |
| `2026-10-17 04:00` | 🔴 SELL (+0.07$) | `ETH-USD` | $10.07 | $2429.64 | ETH-USD ha alcanzado un RSI de 1 hora de 73.3, entrando en zona de sobrecompra. Siguiendo ... |
| `2026-10-16 16:30` | 🟢 BUY | `ETH-USD` | $10.00 | $2412.98 | ETH-USD muestra un RSI diario en niveles de sobreventa extrema (30.3) y un cambio positivo... |

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
