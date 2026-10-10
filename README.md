# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 13:40:37`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.35 USD** | **$40.46 USD** | 🟢 **+1.15%** ($+0.46) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $110.11 | $20.20 | 📈 +1.00% |
| `ETH-USD` | 0.006448 | $2481.58 | $2504.93 | $16.15 | 📈 +0.94% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo mixto con los índices tradicionales (QQQ, SPY) manteniendo tendencias alcistas moderadas, mientras que las criptomonedas (SOL-USD, ETH-USD) se encuentran fuertemente sobrevendidas en el corto plazo (RSI de 24.4 y 28.1 respectivamente) tras caídas semanales significativas. Ambas posiciones actuales en cripto muestran ganancias muy modestas (aprox. +1%) y aún no alcanzan nuestro objetivo de take-profit del +2.5%. Dado que se encuentran en niveles extremos de sobreventa técnica y con alta volatilidad, mantenemos ambas posiciones para capturar el rebote esperado hacia la media."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD se encuentra en condición de extrema sobreventa con un RSI de 24.4 tras una caída semanal del 9.4%. Mantenemos la posición para capturar el rebote técnico inminente sin disparar stop-loss ya que estamos en terreno positivo (+1%).
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD presenta un RSI de 28.1, también en zona de profunda sobreventa. Mantenemos la posición actual con una pequeña ganancia del 0.94% esperando que el impulso alcista del mercado general active el rebote técnico hacia nuestro objetivo.

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
