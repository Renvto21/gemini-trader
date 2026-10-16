# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 19:00:50`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.05 USD** | **$38.34 USD** | 🔴 **-4.16%** ($-1.66) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.17 | $10.04 | 📈 +0.44% | 3h 59m |
| `ETH-USD` | 0.004144 | $2412.98 | $2413.94 | $10.00 | 📈 +0.04% | 2h 30m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas permanece abierto 24/7 con un sesgo lateral a bajista, mientras que los mercados tradicionales están cerrados. SOL-USD y ETH-USD se mantienen en rangos estrechos con ganancias marginales (0.44% y 0.04% respectivamente), mostrando baja volatilidad en este ciclo pero respetando los soportes macro sin activar ningún stop-loss. Mantenemos la cautela y la liquidez en reserva para capturar movimientos direccionales claros."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 70%): La posición en SOL-USD se encuentra en terreno ligeramente positivo (+0.44%) tras casi 4 horas abierta. El RSI de 1 hora está en 30.7, cerca de la zona de rebote, por lo que mantenemos la posición esperando el impulso hacia el objetivo de take-profit sin necesidad de forzar una venta prematura.
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD se mantiene estable con un PnL de +0.04% tras 2.5 horas de holding. El RSI diario se encuentra en niveles de sobreventa extrema (30.3), lo que respalda la tesis de un rebote técnico inminente. Conservamos la posición para dejar trabajar la estrategia.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales en SOL-USD y ETH-USD mientras no rompan a la baja el soporte del -2.0% o alcancen el objetivo de take-profit entre +2.0% y +3.5%. Monitorearemos de cerca el RSI de 1 hora de ambos activos. Si alguna posición se estanca o pierde momentum, procederemos a rotar el capital hacia oportunidades con mayor volumen en el siguiente ciclo."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **63** | 🎯 **38.1%** (24W / 25L / 14BE) | 🔴 **$-1.60 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-16 16:30` | 🟢 BUY | `ETH-USD` | $10.00 | $2412.98 | ETH-USD muestra un RSI diario en niveles de sobreventa extrema (30.3) y un cambio positivo... |
| `2026-10-16 16:30` | 🔴 SELL (-0.11$) | `MSFT` | $6.39 | $526.18 | MSFT lleva más de 1 día y 5 horas abierto mostrando debilidad persistente y un rendimiento... |
| `2026-10-16 15:01` | 🟢 BUY | `SOL-USD` | $10.00 | $103.71 | SOL-USD presenta un RSI de 1 hora en 34.3 saliendo de la zona de sobreventa extrema, acomp... |
| `2026-10-16 14:30` | 🔴 SELL (-0.15$) | `ETH-USD` | $6.85 | $2399.90 | ETH-USD ha rebasado el umbral estricto de stop-loss (-2.12%), operando en tendencia bajist... |
| `2026-10-16 13:40` | 🔴 SELL (-0.02$) | `NVDA` | $7.98 | $216.80 | NVDA lleva más de 24 horas abierto operando bajo la SMA20 con un momentum débil, acumula u... |

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
