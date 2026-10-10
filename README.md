# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 18:00:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.39 USD** | **$40.50 USD** | 🟢 **+1.25%** ($+0.50) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $110.26 | $20.23 | 📈 +1.14% |
| `ETH-USD` | 0.006448 | $2481.58 | $2506.61 | $16.16 | 📈 +1.01% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento mixto con el S&P 500 y QQQ manteniendo tendencias alcistas moderadas, mientras que las criptomonedas principales como SOL-USD y ETH-USD se encuentran en niveles de sobreventa extrema (RSI de 24.9 y 28.4 respectivamente) tras caídas semanales significativas. Esto presenta una oportunidad clásica de rebote técnico (mean reversion) para nuestras posiciones actuales, las cuales ya muestran una ligera recuperación positiva pero aún no alcanzan la toma de beneficios objetivo del +2.5%. Dado que nuestro efectivo disponible es de apenas $4.11 (respetando casi el límite mínimo) y nuestras posiciones actuales están repuntando desde la sobreventa, la mejor estrategia táctica actual es mantener (HOLD) ambas criptomonedas para permitir que el impulso alcista diario capture el rebote buscado hacia nuestros objetivos de ganancia."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 82%): SOL-USD presenta un RSI extremadamente bajo de 24.9 y una caída semanal de -9.27%, lo que confirma una fuerte sobreventa. Aunque se encuentra bajo su SMA20, muestra un rebote en las últimas 24 horas (+1.03%) y un PnL positivo del 1.14%. Mantenemos la posición para capturar el objetivo de ganancia del +2.5% antes de rotar el capital.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD muestra un RSI de sobreventa en 28.4 y un retroceso semanal del -8.07%. La posición actual ya registra un beneficio del 1.01%. Esperamos que continúe el rebote técnico actual impulsado por la ligera recuperación del mercado cripto para asegurar ganancias al llegar al umbral del +2.5%.

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
