# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 22:30:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.36 USD** | **$40.47 USD** | 🟢 **+1.18%** ($+0.47) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $110.08 | $20.19 | 📈 +0.97% |
| `ETH-USD` | 0.006448 | $2481.58 | $2507.81 | $16.17 | 📈 +1.06% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones extremas de sobreventa técnica con SOL-USD (RSI 24.3) y ETH-USD (RSI 28.6) cotizando profundamente deprimidos tras caídas semanales del -9.42% y -8.02%, respectivamente. Sin embargo, ambas posiciones actuales se encuentran estancadas en ganancias modestas (+0.97% y +1.06%) sin alcanzar el objetivo de take-profit del +2.5% y lejos de activar los stop-loss. Con una reserva de efectivo muy ajustada de $4.11 USD, mantenemos nuestras posiciones actuales para permitirles capitalizar el rebote por sobreventa, optando por no realizar nuevas compras ni ventas en este ciclo para preservar la liquidez mínima requerida."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD está en clara sobreventa (RSI 14 de 24.3), lo que presenta una alta probabilidad de un rebote técnico inminente hacia nuestra meta de take-profit del +2.5%. Mantenemos la posición para capturar dicho movimiento.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD muestra un RSI de 28.6 en zona de sobreventa con un rendimiento actual del +1.06%. Esperamos el impulso alcista necesario para alcanzar el objetivo de ganancia rápida sin activar el stop-loss.

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
