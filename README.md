# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 21:40:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$41.13 USD** | **$41.13 USD** | 🟢 **+2.83%** ($+1.13) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.369416 | $111.58 | $111.33 | $41.13 | 📉 -0.23% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo mixto con los índices principales y tech (QQQ, SPY) con tendencias alcistas saludables, mientras que las criptomonedas experimentan una fuerte sobreventa tras caídas semanales (SOL-USD con RSI de 26.4 y ETH-USD con RSI de 34.4). Mantenemos nuestra posición en SOL-USD ya que se encuentra en una zona clásica de rebote técnico por sobreventa extrema, esperando el impulso alcista para capturar ganancias rápidas."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): La posición en SOL-USD tiene una pérdida marginal del -0.23% pero su RSI está en 26.4 (sobreventa extrema), lo que indica una alta probabilidad de un rebote técnico a corto plazo cumpliendo nuestra estrategia de mean reversion. No ha tocado el stop-loss estricto del -2.5% o -3.0%, por lo que debemos mantenerla para capturar el movimiento alcista.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 21:20` | 🟢 BUY | `SOL-USD` | $4.24 | $111.11 | Aprovechamos el capital liberado para incrementar la exposición en SOL-USD. Se encuentra e... |
| `2026-10-11 21:20` | 🔴 SELL | `ETH-USD` | $4.24 | $2534.63 | Vendemos la totalidad de la posición en ETH-USD (valorada en aproximadamente 4.24 USD) par... |
| `2026-10-11 21:10` | 🟢 BUY | `SOL-USD` | $3.82 | $111.13 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 25.7 y una caída semanal de... |
| `2026-10-11 21:10` | 🔴 SELL | `MSFT` | $3.82 | $535.07 | MSFT ha alcanzado un RSI de 72.3 en zona de sobrecompra y acumula un avance sólido. Ejecut... |
| `2026-10-11 21:00` | 🟢 BUY | `MSFT` | $3.82 | $535.07 | MSFT muestra un fuerte momentum alcista con un incremento de 2.38% en 24 horas y un RSI en... |

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
