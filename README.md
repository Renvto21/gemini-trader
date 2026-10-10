# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 20:30:41`

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
| `ETH-USD` | 0.006448 | $2481.58 | $2505.43 | $16.15 | 📈 +0.96% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones de sobreventa extrema con SOL-USD (RSI 24.1) y ETH-USD (RSI 28.2), activos que mantenemos en cartera con ganancias moderadas pero estancadas. Dado que no alcanzan aún el take-profit del 2.5% y muestran intenciones de rebote técnico desde niveles de soporte, mantenemos ambas posiciones actuales para capturar la recuperación completa hacia el objetivo de +3% a +6%. El efectivo disponible es de apenas $4.11 USD, cumpliendo con la regla de reserva mínima, por lo que no realizamos nuevas compras en este ciclo y nos enfocamos en gestionar la volatilidad existente."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): La posición se encuentra con una ganancia del 0.92% y un RSI de 24.1 que confirma sobreventa profunda. Mantenemos para cazar el rebote técnico hacia la zona de take-profit sin activar el stop-loss, ya que la tendencia de 24 horas empieza a girar al alza (+0.82%).
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD registra un RSI de 28.2 y una ganancia actual del 0.96%. Esperamos el impulso alcista para asegurar ganancias cercanas al objetivo de +2.5% antes de rotar el capital.

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
