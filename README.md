# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-09 18:40:50`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.12 USD** | **$35.99 USD** | **$40.11 USD** | 🟢 **+0.28%** ($+0.11) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `NVDA` | 0.021772 | $229.65 | $229.28 | $4.99 | 📉 -0.16% |
| `QQQ` | 0.006652 | $751.70 | $751.27 | $5.00 | 📉 -0.06% |
| `SOL-USD` | 0.137539 | $109.06 | $109.02 | $14.99 | 📉 -0.04% |
| `ETH-USD` | 0.004433 | $2481.36 | $2482.55 | $11.01 | 📈 +0.05% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado de criptomonedas presenta una capitulación severa a corto plazo, dejando a SOL-USD y ETH-USD en niveles de sobreventa extrema (RSI de 20.3 y 25.0 respectivamente). Mientras tanto, los índices tradicionales como el SPY se mantienen estables pero con bajo momentum de corto plazo. Aprovechamos la regla de rotación activa de capital para liquidar nuestra posición lenta en SPY y redoblar la apuesta en el rebote técnico de SOL-USD, maximizando el potencial de retorno rápido."*

**Operaciones del ciclo:**
- **[SELL] SPY** (Confianza: 90%): Liberamos capital de SPY, un activo de bajo beta y lento movimiento, para financiar una operación de alta convicción y volatilidad en cripto que ofrece un potencial de rebote mucho mayor.
- **[BUY] SOL-USD** (Confianza: 95%): SOL-USD está extremadamente sobrevendido con un RSI de 20.3. Ejecutamos una compra agresiva para promediar y capturar un rebote técnico rápido del +2% al +6% hacia su media móvil.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-09 18:40` | 🟢 BUY | `SOL-USD` | $5.00 | $109.02 | SOL-USD está extremadamente sobrevendido con un RSI de 20.3. Ejecutamos una compra agresiv... |
| `2026-10-09 18:40` | 🔴 SELL | `SPY` | $5.03 | $778.57 | Liberamos capital de SPY, un activo de bajo beta y lento movimiento, para financiar una op... |
| `2026-10-09 18:31` | 🟢 BUY | `ETH-USD` | $6.00 | $2481.06 | Oportunidad de alta convicción por sobreventa extrema (RSI de 24.8). Con los $6.00 USD lib... |
| `2026-10-09 18:31` | 🔴 SELL | `AAPL` | $6.00 | $336.64 | Rotación estratégica de capital. AAPL se encuentra estancada con un rendimiento de -0.01% ... |
| `2026-10-09 18:25` | 🟢 BUY | `ETH-USD` | $5.00 | $2481.72 | ETH-USD muestra un RSI de 24.9, confirmando una capitulación de corto plazo en el mercado ... |

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
