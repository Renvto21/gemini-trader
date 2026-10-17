# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 01:50:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.14 USD** | **$38.43 USD** | 🔴 **-3.94%** ($-1.57) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.66 | $10.09 | 📈 +0.92% | 10h 49m |
| `ETH-USD` | 0.004144 | $2412.98 | $2423.95 | $10.05 | 📈 +0.45% | 9h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de valores tradicional se encuentra cerrado, por lo que toda la atención operativa se concentra en el mercado de criptomonedas (abierto 24/7). Tanto SOL-USD como ETH-USD muestran un comportamiento lateral con ligeras ganancias positivas flotantes (+0.92% y +0.45% respectivamente), pero aún no han alcanzado el objetivo de take-profit óptimo de +2.0% a +3.5%. Los indicadores de 1 hora se mantienen neutrales y no muestran señales de venta por sobrecompra ni motivos para activación de stop-loss, por lo que se prioriza mantener posiciones a la espera de un mayor impulso."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 70%): La posición mantiene un rendimiento positivo de +0.92% tras casi 11 horas abierta. El RSI de 1 hora está en 42.0 y no ha alcanzado el objetivo de take-profit (+2.0% a +3.5%), manteniéndose lejos del stop-loss, por lo que se decide mantener para dejar correr la ganancia.
- **[HOLD] ETH-USD** (Confianza: 70%): La posición muestra un beneficio del +0.45% con un tiempo abierto de más de 9 horas. El RSI diario se mantiene bajo en 30.8 apoyando un potencial rebote técnico mayor. Se mantiene la posición a la espera de alcanzar el objetivo de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas en SOL-USD y ETH-USD supervisando de cerca el avance hacia el objetivo de take-profit entre +2.0% y +3.5%. Proteger rigurosamente con stop-loss si alguna posición perfora el -2.0% de pérdida. Conservar la liquidez actual de 18.29 USD hasta que se presente una oportunidad de alta convicción o activación clara de rebote en los activos disponibles."
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
