# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 12:00:49`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.48 USD** | **$20.02 USD** | **$38.50 USD** | 🔴 **-3.75%** ($-1.50) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096209 | $103.94 | $104.20 | $10.03 | 📈 +0.25% | 1h 40m |
| `ETH-USD` | 0.004126 | $2423.75 | $2423.71 | $10.00 | 📈 -0.00% | 10m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado accionario se encuentra cerrado con precios congelados, por lo que toda la atención y liquidez activa se concentran en las criptomonedas (abiertas 24/7). SOL-USD y ETH-USD muestran RSI diarios profundamente deprimidos, indicando condiciones de sobreventa macro donde buscamos rebotes técnicos. Sin embargo, en el corto plazo (1 hora) el impulso se mantiene neutral, con SOL-USD con un PnL de +0.25% y ETH-USD plano. Mantenemos ambas posiciones mientras esperamos una aceleración del momentum o la llegada a los objetivos de take-profit entre +2.0% y +3.5%."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición en SOL-USD muestra un beneficio marginal de +0.25% tras 1 hora y 40 minutos. El RSI diario se mantiene en sobreventa extrema (22.7), lo que respalda la tesis del rebote alcista. Mantenemos la posición a la espera de que el RSI de 1 hora supere los 70 puntos o alcancemos el objetivo de ganancia del 2% al 3.5%.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD se encuentra operando de manera plana (PnL -0.0%) con un tiempo en cartera muy breve (10 minutos). Su RSI diario se mantiene bajo en 28.9, justificando la búsqueda de un rebote por reversión a la media. Mantenemos la posición vigilando de cerca que no perfore soportes y buscando capturar un movimiento alcista rápido.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones abiertas en SOL-USD y ETH-USD supervisando su evolución de corto plazo. Establecemos como objetivo de take-profit un rendimiento de +2.0% a +3.5% o una lectura de RSI de 1 hora superior a 70. El stop-loss estricto se mantiene en -2.0% para proteger el capital. Si el momentum se estanca y surge una oportunidad de mayor convicción en BTC-USD u otro activo, evaluaremos rotar capital."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **65** | 🎯 **40.0%** (26W / 25L / 14BE) | 🔴 **$-1.41 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-17 11:50` | 🟢 BUY | `ETH-USD` | $10.00 | $2423.75 | ETH-USD presenta un RSI diario en niveles de sobreventa profunda (28.9) y un cambio positi... |
| `2026-10-17 10:20` | 🟢 BUY | `SOL-USD` | $10.00 | $103.94 | SOL-USD presenta un RSI diario en niveles de sobreventa extrema (22.5) y un cambio positiv... |
| `2026-10-17 04:30` | 🔴 SELL (+0.12$) | `SOL-USD` | $10.12 | $104.94 | SOL-USD ha alcanzado un RSI de 1 hora de 70.4, entrando en zona de sobrecompra, y acumula ... |
| `2026-10-17 04:00` | 🔴 SELL (+0.07$) | `ETH-USD` | $10.07 | $2429.64 | ETH-USD ha alcanzado un RSI de 1 hora de 73.3, entrando en zona de sobrecompra. Siguiendo ... |
| `2026-10-16 16:30` | 🟢 BUY | `ETH-USD` | $10.00 | $2412.98 | ETH-USD muestra un RSI diario en niveles de sobreventa extrema (30.3) y un cambio positivo... |

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
