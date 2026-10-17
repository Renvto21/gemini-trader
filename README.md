# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 15:40:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.48 USD** | **$19.95 USD** | **$38.43 USD** | 🔴 **-3.94%** ($-1.57) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096209 | $103.94 | $103.81 | $9.99 | 📉 -0.13% | 5h 20m |
| `ETH-USD` | 0.004126 | $2423.75 | $2414.71 | $9.96 | 📉 -0.37% | 3h 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se encuentra abierto 24/7 y muestra signos de estabilización con ligeros repuntes en el momentum de corto plazo, a pesar de mantener una tendencia bajista macro en el gráfico diario. Los mercados tradicionales permanecen cerrados. SOL-USD y ETH-USD muestran mejoras incrementales en su RSI de 1 hora (39.7 y 44.5 respectivamente) y cambios positivos en la última hora, lo que indica que el rebote técnico sigue gestándose de manera pausada. Mantenemos las posiciones abiertas para permitir que desarrollen su potencial alcista hacia el objetivo de take-profit."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición en SOL-USD se mantiene estable con una pérdida marginal (-0.13%) tras 5 horas y 20 minutos abierta. El RSI de 1 hora ha subido a 39.7 con un cambio positivo de 0.47% en la última hora, lo que sugiere que el rebote técnico sigue en marcha. Esperamos que alcance la zona de take-profit.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra un comportamiento similar, con una pérdida menor de -0.37% tras 3 horas y 50 minutos. Su RSI de 1 hora se sitúa en 44.5 y registra un cambio positivo de 0.25% en la última hora. Conservamos la posición para capturar el impulso de reversión a la media.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas de SOL-USD y ETH-USD durante este ciclo, ya que se encuentran estables y respetando los niveles de soporte diario. Monitorear de cerca el RSI de 1 hora para asegurar beneficios parciales al alcanzar la zona de +2.0% a +3.5% o niveles de sobrecompra (>70). Mantener un stop-loss estricto si las pérdidas superan el -2.0% y conservar la liquidez en efectivo actual por encima del mínimo requerido."
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
