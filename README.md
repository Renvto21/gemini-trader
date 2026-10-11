# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 21:40:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.29 USD** | **$40.40 USD** | 🟢 **+1.01%** ($+0.40) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.87 | $20.16 | 📈 +0.78% |
| `ETH-USD` | 0.006448 | $2481.58 | $2502.89 | $16.14 | 📈 +0.86% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un fuerte contraste técnico. Por un lado, las criptomonedas principales como SOL-USD y ETH-USD se encuentran en profunda sobreventa (RSI de 23.6 y 27.7 respectivamente) tras caídas semanales significativas, lo que activa nuestra estrategia de Mean Reversion y búsqueda de rebotes técnicos. Por otro lado, activos tecnológicos como MSFT han alcanzado niveles de sobrecompra (RSI 72.3). Dado que nuestras posiciones actuales en SOL y ETH muestran ganancias modestas (+0.78% y +0.86%) y aún no alcanzan el objetivo de take-profit del +2.5% ni presentan señales de agotamiento inmediato al estar rebotando desde mínimos extremos, mantenemos la postura actual mientras consolidamos liquidez."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 82%): SOL-USD se encuentra en un nivel de sobreventa extrema (RSI 23.6), lo que favorece un rebote técnico inminente. La posición actual muestra una ganancia leve del +0.78% y debemos mantenerla para capturar el movimiento alcista esperado hacia el objetivo del +2.5%.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD presenta un RSI de 27.7, reflejando condiciones claras de sobreventa. Mantenemos la posición actual para aprovechar la reversión a la media y buscar una toma de ganancias rápida cuando el precio recupere terreno.

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
