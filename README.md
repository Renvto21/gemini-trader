# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 20:30:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.07 USD** | **$38.36 USD** | 🔴 **-4.11%** ($-1.64) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.16 | $10.04 | 📈 +0.43% | 5h 29m |
| `ETH-USD` | 0.004144 | $2412.98 | $2419.02 | $10.03 | 📈 +0.25% | 3h 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado y operando con precios congelados, manteniendo una tendencia bajista general en los índices principales como SPY y QQQ. Los mercados de criptomonedas continúan abiertos 24/7, mostrando un comportamiento lateral con ligera presión bajista pero manteniendo soportes en gráficos diarios. Las posiciones actuales en SOL-USD y ETH-USD se mantienen estables con ligeras ganancias porcentuales, a la espera de un mayor impulso alcista que permita alcanzar los objetivos de take-profit sin activar los stop-loss."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición en SOL-USD se mantiene estable con una pequeña ganancia del 0.43% tras 5 horas y media abierta. El RSI de 1 hora se mantiene en 33.9 y el activo sigue respetando el soporte diario, por lo que se mantiene la posición buscando el objetivo de take-profit sin alterar el plan actual.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra un comportamiento similar, con una ganancia actual de 0.25% tras casi 4 horas abierta. El RSI diario se mantiene en niveles de sobreventa extrema (30.6), lo que respalda la tesis de rebote técnico a mediano plazo. Se mantiene la posición a la espera de mayor tracción.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas en SOL-USD y ETH-USD mientras evolucionan hacia la zona de take-profit (+2.0% a +3.5%). Monitorear el RSI de 1 hora y el comportamiento de los precios; si alguna cruza el umbral de ganancia objetivo o entra en sobrecompra (> 70 RSI), proceder a la venta inmediata para asegurar beneficios. Vigilar estrictamente el stop-loss (-2.0%) para cortar pérdidas ante cualquier giro bajista abrupto. Mantener la liquidez actual a la espera de un fuerte momentum en activos abiertos."
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
