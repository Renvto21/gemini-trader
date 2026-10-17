# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 01:30:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.29 USD** | **$20.13 USD** | **$38.42 USD** | 🔴 **-3.96%** ($-1.58) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096423 | $103.71 | $104.55 | $10.08 | 📈 +0.81% | 10h 29m |
| `ETH-USD` | 0.004144 | $2412.98 | $2424.10 | $10.05 | 📈 +0.46% | 8h 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de valores tradicional (Wall Street) se encuentra cerrado, por lo que la operativa se concentra exclusivamente en el mercado de criptomonedas (ABIERTO 24/7). Las criptomonedas principales (SOL-USD, ETH-USD y BTC-USD) muestran un comportamiento lateral a ligeramente bajista en el corto plazo, con un RSI de 1 hora moderado y sin la fuerza suficiente para alcanzar aún el objetivo de take-profit del +2.0% al +3.5%. Las posiciones actuales se mantienen estables con pequeñas ganancias no realizadas, por lo que es prudente mantenerlas a la espera de un impulso alcista."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 70%): La posición en SOL-USD presenta una ganancia actual de +0.81% tras casi 10 horas de retención. Aunque el momentum de corto plazo se ha desacelerado ligeramente, el RSI diario en zona de soporte sugiere mantener la posición a la espera de alcanzar el objetivo de take-profit.
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD muestra una pequeña ganancia del +0.46%. Dado que el mercado tradicional está cerrado y no hay señales claras de ruptura bajista que activen el stop-loss, se mantiene la posición para capturar el rebote esperado desde la sobreventa diaria.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en SOL-USD y ETH-USD supervisando de cerca el RSI de 1 hora y el cambio porcentual. Esperar a que alcancen el rango objetivo de ganancia (+2.0% a +3.5%) para realizar tomas de beneficio parciales o totales. Proteger estrictamente con stop-loss si alguna posición cae por debajo de -2.0%. Preservar la liquidez actual de 18.29 USD hasta que surja una clara oportunidad de alta convicción con un RSI saliendo de sobreventa extrema en cripto."
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
