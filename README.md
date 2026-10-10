# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 20:40:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.34 USD** | **$40.45 USD** | 🟢 **+1.12%** ($+0.45) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $110.03 | $20.18 | 📈 +0.92% |
| `ETH-USD` | 0.006448 | $2481.58 | $2504.92 | $16.15 | 📈 +0.94% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento mixto con el sector tecnológico y el S&P 500 operando estables con tendencia alcista moderada. Las criptomonedas (SOL y ETH) muestran señales extremas de sobreventa con RSI de 24.1 y 28.1 respectivamente, encontrándose en zonas ideales de rebote técnico (mean reversion) a pesar de la tendencia bajista de corto plazo. Mantendremos nuestras posiciones actuales para capturar la recuperación dado que el PnL se mantiene positivo y las caídas semanales ya descuentan gran parte del pesimismo."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL se encuentra en sobreventa severa con un RSI de 24.1, lo que ofrece un escenario clásico de rebote técnico inminente. Nuestra posición actual tiene un pequeño beneficio del 0.92% y mantenemos la operativa abierta para buscar el objetivo de +2.5% o superior.
- **[HOLD] ETH-USD** (Confianza: 85%): ETH registra un RSI de 28.1, indicando sobreventa profunda tras caídas semanales del -8.13%. El precio actual muestra indicios de estabilización y mantenemos la posición para capturar el movimiento alcista de recuperación hacia la media.

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
