# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 18:40:47`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.04 USD** | **$38.33 USD** | 🔴 **-4.18%** ($-1.67) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.11 | $10.04 | 📈 +0.39% | 3h 39m |
| `ETH-USD` | 0.004144 | $2412.98 | $2413.54 | $10.00 | 📈 +0.02% | 2h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado y operando bajo precios congelados, por lo que el foco operativo se concentra exclusivamente en el mercado de criptomonedas (ABIERTO 24/7). Las criptomonedas principales (SOL-USD y ETH-USD) muestran una consolidación lateral con ligeros sesgos positivos en el corto plazo, manteniendo sus indicadores técnicos en zonas de soporte y con potencial para buscar rebotes técnicos una vez que el impulso de compra aumente. Las posiciones actuales se mantienen estables dentro de los márgenes permitidos, sin alcanzar aún los objetivos de take-profit ni activar los stop-loss."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD se mantiene operando estables con un pequeño rendimiento positivo (+0.39%) tras casi 4 horas de holding. El RSI de 1 hora se mantiene en 34.8 y el precio respeta la zona de soporte sin alcanzar el take-profit deseado ni gatillar el stop-loss.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD se encuentra en rango neutral con un PnL cercano a 0% (+0.02%) tras poco más de 2 horas desde su apertura. Se mantiene en cartera a la espera de que el RSI diario en sobreventa extrema impulse el rebote técnico esperado.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en SOL-USD y ETH-USD mientras continúan su consolidación. Estar atentos a alcanzar el objetivo de take-profit entre +2.0% y +3.5%, o un RSI de 1 hora superior a 70. Mantener un stop-loss estricto en -2.0% para proteger el capital. La liquidez restante de $18.29 USD se mantendrá a la espera de una mayor confirmación de volumen o una ruptura alcista más clara en BTC-USD o altcoins."
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
