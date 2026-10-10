# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 13:30:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.34 USD** | **$40.45 USD** | 🟢 **+1.12%** ($+0.45) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $110.12 | $20.20 | 📈 +1.01% |
| `ETH-USD` | 0.006448 | $2481.58 | $2502.70 | $16.14 | 📈 +0.85% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones extremas de sobreventa con RSI profundamente deprimidos en SOL-USD (24.4) y ETH-USD (27.7), lo cual representa una oportunidad clásica de rebote técnico (mean reversion) acorde con nuestra estrategia agresiva. Por otro lado, las posiciones actuales muestran ganancias moderadas (+1.01% y +0.85%) pero aún no alcanzan el objetivo estricto de take-profit del +2.5% ni se encuentran en sobrecompra, por lo que se decide mantenerlas para exprimir el rebote en curso. La liquidez en efectivo se mantiene en el mínimo operativo requerido ($4.11 USD)."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD se encuentra en una zona de sobreventa extrema (RSI de 24.4), lo que aumenta considerablemente la probabilidad de un rebote técnico a corto plazo. Mantenemos la posición para capturar el movimiento alcista hacia la resistencia inmediata.
- **[HOLD] ETH-USD** (Confianza: 82%): Al igual que Solana, Ethereum presenta un RSI de 27.7 que indica sobreventa profunda. La posición actual muestra un rendimiento positivo pero contenida, por lo que retener la posición nos permite buscar el objetivo de ganancia del +2.5%.

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
