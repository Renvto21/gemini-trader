# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 12:20:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.41 USD** | **$40.52 USD** | 🟢 **+1.29%** ($+0.52) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $110.37 | $20.25 | 📈 +1.24% |
| `ETH-USD` | 0.006448 | $2481.58 | $2506.09 | $16.16 | 📈 +0.99% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento mixto con sesgo alcista en indices generales como SPY y QQQ, mientras que las criptomonedas principales (SOL, ETH, BTC) continúan recuperándose tras caídas semanales pero se mantienen con RSI en zona de sobreventa o baja, ideales para capturar rebotes técnicos agresivos. Nuestras posiciones actuales en SOL-USD y ETH-USD muestran ligeras ganancias pero aún no alcanzan el objetivo del take-profit (+2.5%), y el efectivo disponible ($4.11 USD) se encuentra en el límite mínimo de reserva, por lo que la mejor estrategia táctica en este ciclo es mantener las posiciones actuales y permitir que continúe la recuperación del momentum."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD muestra un RSI de 25.3 indicando condiciones de profunda sobreventa previa y un intento de rebote en 24 horas (+1.13%). Mantenemos la posición actual para capturar el movimiento alcista hacia el objetivo de take-profit sin activar el stop-loss.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD presenta un RSI de 28.3 con un ligero repunte diario. Dado que nuestro efectivo está al límite de la reserva mínima y la posición está en positivo (+0.99%), es óptimo mantener y dejar correr las ganancias.

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
