# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 22:50:37`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.06 USD** | **$38.35 USD** | 🔴 **-4.14%** ($-1.65) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.19 | $10.05 | 📈 +0.46% | 7h 49m |
| `ETH-USD` | 0.004144 | $2412.98 | $2415.62 | $10.01 | 📈 +0.11% | 6h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general se encuentra bajo presión y con tendencia bajista en los principales índices y criptomonedas, con varios activos operando por debajo de su SMA20. Wall Street permanece cerrado, por lo que toda la actividad se concentra en el mercado de criptomonedas (24/7). Los indicadores RSI en 1 hora de SOL-USD y ETH-USD han vuelto a descender a niveles de sobreventa profunda (29.9 y 20.2 respectivamente), lo que indica un estancamiento temporal en el rebote esperado pero manteniendo intactos los niveles de soporte macro diario."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición en SOL-USD muestra un pequeño beneficio del +0.46% tras casi 8 horas abierto. Aunque el RSI de 1 hora ha bajado a 29.9, el precio se mantiene estable por encima del precio de entrada y no ha activado ningún stop-loss. Mantenemos la posición a la espera del rebote técnico.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD se mantiene prácticamente plano con un PnL de +0.11% tras algo más de 6 horas. El RSI diario en sobreventa extrema (30.4) justifica mantener la posición a la espera de la reacción alcista del mercado cripto.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas de SOL-USD y ETH-USD durante este ciclo a pesar de la lentitud temporal y la ligera caída en el RSI de 1 hora. El objetivo sigue siendo buscar un take-profit en el rango de +2.0% a +3.5% en cuanto el volumen repunte y cruce el RSI de 1 hora por encima de 40. Monitorear rigurosamente que las pérdidas no alcancen el límite de stop-loss de -2.0%. Mantener el efectivo actual de reserva."
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
