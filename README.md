# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 21:30:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.28 USD** | **$40.39 USD** | 🟢 **+0.98%** ($+0.39) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.83 | $20.15 | 📈 +0.74% |
| `ETH-USD` | 0.006448 | $2481.58 | $2502.31 | $16.13 | 📈 +0.84% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo positivo general con QQQ y SPY consolidándose al alza, mientras que las criptomonedas (SOL-USD y ETH-USD) se encuentran en condiciones extremas de sobreventa técnica con RSI en 23.4 y 27.6 respectivamente, manteniendo nuestras posiciones actuales con un modesto beneficio pero listas para un rebote mayor."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD tiene un RSI muy bajo de 23.4, lo que indica sobreventa extrema. Mantenemos la posición para capturar el esperado rebote técnico hacia la zona de resistencia superior según nuestra estrategia de mean reversion.

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
