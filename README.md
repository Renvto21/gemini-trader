# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 00:50:35`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.18 USD** | **$40.29 USD** | 🟢 **+0.73%** ($+0.29) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.29 | $20.05 | 📈 +0.25% |
| `ETH-USD` | 0.006448 | $2481.58 | $2502.25 | $16.13 | 📈 +0.83% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto se encuentra en condiciones de sobreventa extrema a corto plazo (SOL con RSI de 21.5 y ETH con RSI de 27.6), lo que presenta una oportunidad clásica de rebote técnico (mean reversion). Nuestras posiciones actuales muestran ganancias muy modestas (0.25% y 0.83%) y aún no alcanzan el objetivo de take-profit del 2.5%, pero el RSI extremadamente deprimido nos indica que los precios están listos para un rebote impulsivo. Dado que la liquidez en efectivo es de $4.11 USD (exactamente el límite mínimo de reserva), mantendremos las posiciones actuales para capturar la recuperación sin realizar nuevas compras en este ciclo."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL se encuentra en niveles de sobreventa extrema con un RSI de 21.5 tras una caída semanal del -10.07%. Mantenemos la posición para capturar el inminente rebote técnico hacia la media, respetando estrictamente el stop-loss si perfora soportes.
- **[HOLD] ETH-USD** (Confianza: 82%): ETH muestra un RSI de 27.6 en zona de sobreventa clara. Mantenemos la posición actual para aprovechar la reversión a la media esperada en el sector cripto.

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
