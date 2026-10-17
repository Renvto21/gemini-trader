# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 01:20:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.12 USD** | **$38.41 USD** | 🔴 **-3.97%** ($-1.59) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.57 | $10.08 | 📈 +0.83% | 10h 19m |
| `ETH-USD` | 0.004144 | $2412.98 | $2422.75 | $10.04 | 📈 +0.40% | 8h 49m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "Los mercados tradicionales se encuentran cerrados, por lo que toda la actividad se concentra en el mercado de criptomonedas, que opera 24/7. Las posiciones actuales en SOL-USD y ETH-USD muestran ligeras ganancias (+0.83% y +0.40% respectivamente) tras más de 8 horas de retención, pero el momentum de corto plazo se ha enfriado ligeramente con el último cambio negativo de 1 hora. Mantenemos la cautela y dejamos correr las posiciones mientras no alcancen el objetivo de take-profit entre +2.0% y +3.5% ni vulneren los soportes de stop-loss."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición acumula una ganancia moderada de +0.83% tras casi 10 horas de retención. Aunque el impulso de 1 hora se ha desacelerado levemente, el precio se mantiene estable y lejos de la zona de stop-loss, por lo que conviene mantenerla a la espera de alcanzar el objetivo de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener posiciones abiertas en SOL-USD y ETH-USD supervisando de cerca la evolución del RSI de 1 hora para buscar tomas de beneficio parciales o totales al alcanzar el rango de +2.0% a +3.5%. Proteger el capital con stop-loss estrictos si caen por debajo de -2.0%. Preservar la liquidez actual de 18.29 USD hasta que surja una oportunidad clara de alta convicción con un RSI saliendo de sobreventa extrema en cripto."
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
