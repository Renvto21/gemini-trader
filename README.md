# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 02:10:59`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.17 USD** | **$38.46 USD** | 🔴 **-3.85%** ($-1.54) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.92 | $10.12 | 📈 +1.17% | 11h 9m |
| `ETH-USD` | 0.004144 | $2412.98 | $2426.17 | $10.05 | 📈 +0.55% | 9h 40m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene abierto con un sesgo ligeramente positivo en el muy corto plazo, mientras que los mercados tradicionales están cerrados. SOL-USD muestra un RSI de 1 hora en 66.2, acercándose a la zona de sobrecompra y acumulando una ganancia de +1.17%. ETH-USD mantiene un comportamiento estable con un rendimiento de +0.55%, aunque su RSI diario se encuentra en niveles bajos. La liquidez disponible es de 18.29 USD, permitiendo mantener la postura táctica actual en activos digitales."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD muestra un rendimiento positivo del 1.17% y un RSI de 1 hora en 66.2, aproximándose a la zona de sobrecompra para la toma de ganancias. Se mantiene la posición a la espera de alcanzar el objetivo de take-profit entre +2.0% y +3.5%.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD se encuentra en terreno positivo con una ganancia del 0.55% y operando en un mercado abierto 24/7. Se mantiene para permitir que el rebote técnico desde la sobreventa diaria continúe desarrollándose hacia los objetivos establecidos.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear de cerca SOL-USD ya que su RSI de 1 hora se aproxima al nivel de sobrecompra (>70) para ejecutar un Take-Profit si alcanza el rango objetivo de +2.0% a +3.5%. Mantener ETH-USD esperando mayor tracción alcista. Proteger ambas posiciones con stop-loss estricto en caso de reversión por debajo del -2.0% y buscar rotar capital adicional si surge una nueva señal de entrada clara."
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
