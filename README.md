# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 20:00:50`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.42 USD** | **$40.53 USD** | 🟢 **+1.32%** ($+0.53) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $110.37 | $20.25 | 📈 +1.24% |
| `ETH-USD` | 0.006448 | $2481.58 | $2507.90 | $16.17 | 📈 +1.06% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento mixto con el sector tech y los índices principales (QQQ, SPY) con tendencias alcistas estables, mientras que las criptomonedas (SOL, ETH) continúan mostrando condiciones de sobreventa profunda tras caídas semanales, aunque intentan estabilizarse. Nuestras posiciones actuales en SOL-USD y ETH-USD muestran ganancias moderadas (+1.24% y +1.06%), pero dado que la regla de take-profit se activa con un +2.5% o sobrecompra y aún no alcanzamos dichos niveles, mantendremos las posiciones vigentes para permitirles capturar un rebote más fuerte. El efectivo disponible se mantiene cerca de la reserva mínima táctica de $4.00, por lo que la prioridad actual es mantener la exposición a los activos de alta beta en recuperación y esperar una mayor confirmación de momentum antes de rotar capital."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): La posición en SOL-USD se mantiene en terreno positivo (+1.24%) tras el rebote desde niveles de extrema sobreventa (RSI de 25.3). Mantenemos la posición para buscar el objetivo de ganancia del +2.5% antes de realizar toma de beneficios.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD muestra un comportamiento similar con un RSI de 28.6 y una ganancia actual del +1.06%. Conservamos la posición para capitalizar la continuación del rebote técnico a corto plazo.

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
