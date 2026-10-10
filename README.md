# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 19:00:48`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.39 USD** | **$40.50 USD** | 🟢 **+1.26%** ($+0.50) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $110.24 | $20.22 | 📈 +1.12% |
| `ETH-USD` | 0.006448 | $2481.58 | $2507.96 | $16.17 | 📈 +1.06% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo ligeramente positivo en los índices principales como SPY y QQQ, mientras que el sector cripto se mantiene en una fase de recuperación tras caídas recientes, destacando a SOL-USD y ETH-USD con niveles de RSI de extrema sobreventa (24.8 y 28.6 respectivamente). Nuestras posiciones actuales muestran ganancias moderadas (+1.12% y +1.06%), pero aún no alcanzan el objetivo de take-profit del +2.5% ni presentan señales de sobrecompra. Con un efectivo disponible muy bajo ($4.11 USD), mantenemos una postura de retención (HOLD) para permitir que el momentum alcista en cripto continúe desarrollándose hacia nuestro objetivo de ganancia rápida."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): La posición en Solana muestra un rendimiento positivo de +1.12% y se encuentra en clara zona de sobreventa técnica con un RSI de 24.8. Mantenemos la posición para capturar el rebote técnico hacia el objetivo de +2.5% o superior antes de tomar ganancias.
- **[HOLD] ETH-USD** (Confianza: 80%): Ethereum presenta un comportamiento similar con un PnL de +1.06% y un RSI de 28.6. Dado el capital limitado en efectivo y la cercanía a niveles de reversión alcista, conservamos la posición para dejar correr las ganancias de este rebote de alta volatilidad.

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
