# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 18:30:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.37 USD** | **$40.48 USD** | 🟢 **+1.19%** ($+0.48) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $110.16 | $20.21 | 📈 +1.04% |
| `ETH-USD` | 0.006448 | $2481.58 | $2506.01 | $16.16 | 📈 +0.98% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo alcista moderado en los índices y acciones tecnológicas como MSFT y QQQ, mientras que las criptomonedas continúan mostrando condiciones de sobreventa profunda (SOL-USD con RSI de 24.6 y ETH-USD con RSI de 28.3). Nuestras posiciones actuales en cripto se mantienen estables con ligeras ganancias (+1.04% y +0.98%), pero dado que aún no alcanzan el objetivo de take-profit del +2.5% y operamos con una reserva de efectivo muy justa de $4.11 USD, la estrategia óptima en este momento es mantener (HOLD) para permitir que el rebote técnico madure y capturemos el impulso alcista esperado en SOL y ETH."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): La posición tiene un PnL positivo del +1.04% y un RSI extremadamente bajo de 24.6, lo cual indica sobreventa y alto potencial de rebote alcista. Mantenemos la posición para buscar el objetivo de take-profit superior al +2.5%.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD presenta un RSI de 28.3 en zona de sobreventa con una ganancia actual de +0.98%. Conservamos la posición para capitalizar la recuperación técnica esperada sin incurrir en costos de rotación innecesarios.

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
