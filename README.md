# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 21:20:38`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.31 USD** | **$40.43 USD** | 🟢 **+1.06%** ($+0.43) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.96 | $20.17 | 📈 +0.86% |
| `ETH-USD` | 0.006448 | $2481.58 | $2503.70 | $16.14 | 📈 +0.89% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra criptomonedas fuertemente sobrevendidas técnicamente con RSI en niveles extremos de mínimos (SOL en 23.9 y ETH en 27.9), lo cual representa una oportunidad clásica de rebote técnico (mean reversion) tras caídas semanales significativas. Las posiciones actuales en SOL-USD y ETH-USD se mantienen estables con pequeñas ganancias (+0.86% y +0.89%) pero aún lejos del objetivo de take-profit del 2.5%. Dado que el efectivo disponible se encuentra en el límite mínimo establecido de 4.11 USD y las criptomonedas muestran condiciones ideales para un rebote inminente de corto plazo, la estrategia óptima es mantener las posiciones actuales y conservar la paciencia hasta alcanzar el objetivo de beneficio o activar un stop-loss estricto."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): La criptomoneda se encuentra en un estado de sobreventa extrema (RSI de 23.9) con un potencial de rebote alcista muy alto. Mantenemos la posición para capturar el movimiento hacia la zona de take-profit manteniendo el riesgo controlado.
- **[HOLD] ETH-USD** (Confianza: 82%): Condiciones técnicas similares a Solana, con un RSI de 27.9 indicando sobreventa profunda y un soporte claro. Mantenemos la posición actual a la espera de una expansión del impulso alcista que permita asegurar ganancias superiores al 2.5%.

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
