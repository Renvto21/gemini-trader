# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 14:40:37`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.34 USD** | **$40.45 USD** | 🟢 **+1.13%** ($+0.45) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $110.00 | $20.18 | 📈 +0.90% |
| `ETH-USD` | 0.006448 | $2481.58 | $2506.79 | $16.16 | 📈 +1.02% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo mixto con criptomonedas fuertemente castigadas en los últimos 7 días pero mostrando condiciones técnicas excepcionales de sobreventa extrema (RSI de 24.0 para SOL-USD y 28.4 para ETH-USD), lo cual es ideal para nuestra estrategia de rebotes (mean reversion). Nuestras posiciones actuales en SOL-USD y ETH-USD registran ganancias moderadas (+0.9% y +1.02% respectivamente), pero aún no alcanzan el take-profit óptimo del +2.5% ni presentan sobrecompra, por lo que decidimos mantenerlas y aprovechar el impulso técnico para buscar un tramo alcista adicional, manteniendo una reserva de efectivo muy ajustada de acuerdo con las reglas."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD presenta un RSI de 24.0 (sobreventa profunda) tras una caída semanal del 9.49%, lo que ofrece un escenario ideal para un rebote técnico inminente. Nuestra posición actual está ligeramente positiva (+0.9%) y mantenemos la operativa para buscar el objetivo de ganancia del +2.5%.
- **[HOLD] ETH-USD** (Confianza: 82%): ETH-USD se encuentra en condiciones similares de sobreventa con un RSI de 28.4. La posición actual muestra una ganancia del +1.02% y mantenemos el activo para capturar el rebote alcista hacia la resistencia inmediata, protegiendo con los niveles de stop-loss y take-profit establecidos.

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
