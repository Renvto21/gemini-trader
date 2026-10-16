# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 16:10:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$21.90 USD** | **$16.29 USD** | **$38.19 USD** | 🔴 **-4.53%** ($-1.81) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $525.07 | $6.38 | 📉 -1.89% | 1d 5h |
| `SOL-USD` | 0.096423 | $103.71 | $102.79 | $9.91 | 📉 -0.89% | 1h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sesgo general bajista o de consolidación débil con la mayoría de los activos operando por debajo de sus SMA20, aunque varias criptomonedas y tecnologías clave se encuentran en zonas de sobreventa en gráficos de 1 hora. La presión vendedora persiste pero abre oportunidades tácticas selectas de rebote (mean reversion)."

**Operaciones del ciclo:**
- **[HOLD] MSFT** (Confianza: 60%): La posición en MSFT lleva más de un día abierta con una pérdida moderada de -1.89%. Aunque el momentum es débil y está cerca del límite de stop-loss del plan táctico, la tendencia diaria sigue siendo alcista sobre la SMA20, por lo que mantendré un ciclo más evaluando si respeta el soporte actual.
- **[HOLD] SOL-USD** (Confianza: 65%): SOL-USD se encuentra en zona de sobreventa extrema con un RSI de 1 hora en 26.0. La pérdida actual es de -0.89%, muy lejos del stop-loss estricto del -2.0%. Mantengo la posición buscando el rebote técnico hacia el take-profit fijado.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "En MSFT, el holding supera un día con un PnL de -1.89% y el RSI de 1 hora está en 32.2; si no muestra recuperación inmediata o rompe la zona crítica, procederé a vender para liberar capital. En SOL-USD, el RSI de 1 hora ha bajado a 26.0 y el PnL está en -0.89%; mantendré la posición buscando el objetivo de take-profit en +2.5% o aplicaré un stop-loss estricto en -2.0% si continúa el deterioro. La liquidez en efectivo se mantendrá vigilante para nuevas entradas tácticas cuando se confirme un verdadero cambio de momentum."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **62** | 🎯 **38.7%** (24W / 24L / 14BE) | 🔴 **$-1.49 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-16 15:01` | 🟢 BUY | `SOL-USD` | $10.00 | $103.71 | SOL-USD presenta un RSI de 1 hora en 34.3 saliendo de la zona de sobreventa extrema, acomp... |
| `2026-10-16 14:30` | 🔴 SELL (-0.15$) | `ETH-USD` | $6.85 | $2399.90 | ETH-USD ha rebasado el umbral estricto de stop-loss (-2.12%), operando en tendencia bajist... |
| `2026-10-16 13:40` | 🔴 SELL (-0.02$) | `NVDA` | $7.98 | $216.80 | NVDA lleva más de 24 horas abierto operando bajo la SMA20 con un momentum débil, acumula u... |
| `2026-10-16 12:50` | 🔴 SELL (-0.06$) | `SOL-USD` | $2.94 | $104.34 | SOL-USD lleva varias horas abierto sin generar el rebote esperado, acumulando una pérdida ... |
| `2026-10-16 10:50` | 🔴 SELL (-0.04$) | `QQQ` | $9.95 | $721.83 | QQQ lleva más de 22 horas abierto operando bajo la SMA20 con un RSI de 1 hora en 30.2 y un... |

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
