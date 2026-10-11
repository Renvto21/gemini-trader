# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 00:20:37`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.22 USD** | **$40.33 USD** | 🟢 **+0.83%** ($+0.33) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.45 | $20.08 | 📈 +0.39% |
| `ETH-USD` | 0.006448 | $2481.58 | $2503.77 | $16.14 | 📈 +0.89% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un comportamiento mixto con un sesgo alcista moderado en los índices generales (SPY y QQQ con tendencias alcistas), mientras que el sector cripto (SOL-USD y ETH-USD) se encuentra en niveles de profunda sobreventa técnica con RSI de 22.1 y 27.9 respectivamente, tras caídas semanales significativas. Esto representa una oportunidad ideal de rebote (mean reversion) acorde con la estrategia agresiva. Dado que nuestras posiciones actuales en SOL-USD y ETH-USD registran ganancias marginales pero están operando en zonas de sobreventa extrema, decidimos mantenerlas para capturar el rebote alcista inminente hacia el objetivo del +2% o más, mientras gestionamos activamente la liquidez actual que se encuentra en el límite mínimo permitido."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD se encuentra en un estado de sobreventa extrema con un RSI de 22.1 y una caída semanal de casi el 10%. Mantenemos la posición ya que cumple perfectamente con la tesis de cazar rebotes técnicos en cripto, esperando un movimiento de recuperación rápido hacia la resistencia cercana.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-10 12:10` | 🔴 SELL | `MSFT` | $4.11 | $535.07 | MSFT ha alcanzado un RSI de 72.3 (sobrecompra) cumpliendo con la regla táctica de toma de ... |
| `2026-10-10 12:00` | 🟢 BUY | `MSFT` | $4.11 | $535.07 | Aprovechamos el capital liberado de GLD para entrar en MSFT, que muestra un fuerte momentu... |
| `2026-10-10 12:00` | 🔴 SELL | `GLD` | $4.11 | $384.58 | Liberamos la totalidad de la posición en GLD ya que se encuentra estancada con 0% de PnL y... |
| `2026-10-10 11:50` | 🟢 BUY | `GLD` | $4.11 | $384.58 | Aprovechamos el efectivo disponible para cazar un rebote por sobreventa en GLD, cuyo RSI s... |
| `2026-10-09 19:00` | 🟢 BUY | `ETH-USD` | $5.00 | $2482.07 | ETH-USD se encuentra en una zona de sobreventa extrema con un RSI de 25.0. Utilizando el c... |

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
