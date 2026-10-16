# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 20:40:36`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.08 USD** | **$38.37 USD** | 🔴 **-4.07%** ($-1.63) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.24 | $10.05 | 📈 +0.51% | 5h 39m |
| `ETH-USD` | 0.004144 | $2412.98 | $2420.61 | $10.03 | 📈 +0.32% | 4h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que toda la actividad se concentra en criptomonedas (ABIERTO 24/7). SOL-USD y ETH-USD muestran un momentum débil pero estable tras sus respectivas entradas por rebote técnico, con ligeras ganancias actuales (0.51% y 0.32% respectivamente). Ninguna de las posiciones ha alcanzado aún el objetivo de take-profit (+2.0% a +3.5%) ni ha caído hacia el stop-loss, y el RSI de 1 hora se mantiene neutral-bajo sin mostrar sobrecompra ni desplomes abruptos."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición en SOL-USD presenta una ganancia modesta de +0.51% tras 5 horas de tenencia. Aunque el momentum de corto plazo se ha desacelerado levemente, el precio se mantiene por encima del precio de entrada y no ha activado ninguna señal de stop-loss ni take-profit. Se mantiene para permitir que evolucione hacia la zona objetivo.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra un comportamiento similar, registrando un beneficio de +0.32% y manteniéndose estable tras su reciente apertura. Se conserva la posición a la espera de que el impulso alcista gane fuerza en el transcurso de las próximas horas para asegurar beneficios en el rango del +2.0%.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en SOL-USD y ETH-USD mientras continúan buscando el objetivo de take-profit (+2.0% a +3.5%). Monitorear de cerca el RSI de 1 hora y el comportamiento de los precios; si alguna cruza el umbral de ganancia objetivo o entra en sobrecompra (> 70 RSI), proceder a la venta inmediata. Vigilar estrictamente el stop-loss (-2.0%) para cortar pérdidas ante cualquier giro bajista. La liquidez de efectivo disponible se mantendrá por encima del mínimo requerido mientras se espera la consolidación del rebote."
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
