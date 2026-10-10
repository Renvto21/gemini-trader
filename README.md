# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 12:30:47`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.42 USD** | **$40.54 USD** | 🟢 **+1.34%** ($+0.54) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $110.44 | $20.26 | 📈 +1.30% |
| `ETH-USD` | 0.006448 | $2481.58 | $2507.14 | $16.16 | 📈 +1.03% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un rebote técnico interesante en las criptomonedas tras caídas semanales significativas, situando a SOL-USD y ETH-USD en niveles atractivos de sobreventa con RSI de 25.5 y 28.4 respectivamente. Las posiciones actuales en cartera muestran ganancias moderadas (+1.3% en SOL y +1.03% en ETH), pero aún no alcanzan el objetivo de take-profit del +2.5% ni presentan signos de sobrecompra urgente. El efectivo disponible es de apenas $4.11 USD, cumpliendo con la regla de mantener una reserva mínima de $4.00 USD, por lo que no hay suficiente liquidez para nuevas compras agresivas sin realizar rotaciones. Dado el sesgo bajista a corto plazo en la tendencia principal de las cripto, mantendremos las posiciones actuales esperando un impulso adicional hacia la zona de take-profit."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): La posición se mantiene activa con una ganancia actual del +1.3%. El RSI de 25.5 indica sobreventa previa y está intentando un rebote técnico. Mantendremos la posición hasta alcanzar el objetivo de take-profit cercano al +2.5% o una señal de salida por stop-loss.

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
