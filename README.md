# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 14:20:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.31 USD** | **$40.42 USD** | 🟢 **+1.04%** ($+0.42) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.90 | $20.16 | 📈 +0.80% |
| `ETH-USD` | 0.006448 | $2481.58 | $2504.10 | $16.15 | 📈 +0.91% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo alcista moderado en los índices tradicionales como QQQ y SPY, mientras que las criptomonedas principales (SOL y ETH) se mantienen en niveles de sobreventa técnica profunda con un RSI de 23.7 y 27.9 respectivamente, consolidando una clara oportunidad de mean reversion y rebote alcista. Ambas posiciones actuales registran ligeras ganancias positivas (+0.8% y +0.91%), manteniendo el capital óptimamente desplegado mientras respetamos la reserva mínima de efectivo."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL se encuentra en niveles de extrema sobreventa técnica (RSI de 23.7) bajo la SMA20, lo cual es ideal para buscar el rebote esperado según nuestra estrategia de mean reversion. Mantenemos la posición para capturar el movimiento alcista sin vender prematuramente, ya que aún no alcanza el take-profit del +2.5%.
- **[HOLD] ETH-USD** (Confianza: 82%): ETH presenta un RSI de 27.9 indicando sobreventa clara y potencial de rebote inminente. La posición está ligeramente en positivo (+0.91%) y se mantiene activa a la espera de un impulso que active el take-profit del +2.5% o superior.

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
