# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 20:10:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.08 USD** | **$38.37 USD** | 🔴 **-4.07%** ($-1.63) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.24 | $10.05 | 📈 +0.51% | 5h 9m |
| `ETH-USD` | 0.004144 | $2412.98 | $2420.38 | $10.03 | 📈 +0.31% | 3h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, manteniendo congelados los precios de los activos principales como QQQ, SPY y NVDA. En el sector cripto (activo 24/7), SOL-USD y ETH-USD muestran consolidación leve tras las recientes entradas en busca de rebotes por sobreventa. Las posiciones actuales muestran ganancias muy marginales (SOL con +0.51% y ETH con +0.31%), manteniéndose por debajo de la zona objetivo de take-profit (+2.0% a +3.5%) y lejos de la zona de stop-loss. No hay suficiente impulso nuevo de alta convicción en este momento para abrir nuevas operaciones, por lo que se prioriza mantener la paciencia y proteger el capital."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): La posición en SOL-USD se mantiene estable con una pequeña ganancia del 0.51%. El activo sigue operando dentro del plan táctico de rebote técnico, por lo que se mantiene la posición a la espera de alcanzar el objetivo de take-profit.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD muestra un comportamiento similar, con una ganancia actual de 0.31%. El holding time es de pocas horas y no ha mostrado señales de fallo en el rebote, por lo que se mantiene en cartera para buscar el objetivo de ganancia.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas en SOL-USD y ETH-USD para permitir que alcancen la zona objetivo de take-profit entre +2.0% y +3.5%. Monitorear de cerca el RSI de 1 hora y el comportamiento del precio; si alcanzan la rentabilidad esperada o entran en sobrecompra (> 70), proceder con la venta para asegurar beneficios. Vigilar los límites de stop-loss (-2.0%) para cortar pérdidas inmediatamente si el mercado cripto gira a la baja. La liquidez de $18.29 USD se mantendrá intacta hasta el próximo ciclo o hasta que aparezca una oportunidad de alta convicción."
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
