# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 12:40:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$36.19 USD** | **$40.19 USD** | 🟢 **+0.47%** ($+0.19) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001175 | $2553.82 | $2527.53 | $2.97 | 📉 -1.03% |
| `SOL-USD` | 0.305055 | $109.55 | $108.89 | $33.22 | 📉 -0.61% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones de sobreventa extrema con ETH-USD (RSI 32.5) y SOL-USD (RSI 27.1), manteniendo nuestras posiciones actuales con ligeras pérdidas pero dentro de los límites de stop-loss. En el ámbito accionario, MSFT presenta un RSI en sobrecompra extrema (78.0), mientras que NVDA cae con un RSI neutral (45.7). Mantendremos las criptomonedas para cazar el rebote técnico inminente debido a la sobreventa, y no realizaremos ventas en este ciclo ya que ninguna posición ha tocado los límites estrictos de stop-loss ni de take-profit, preservando la liquidez mínima requerida de $4.00."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD se encuentra en clara sobreventa con un RSI de 27.1 y una caída acumulada del 9.85% en 7 días. La posición está ligeramente a la baja (-0.61%), pero mantenemos la posición para capturar el rebote por mean reversion sin activar el stop-loss estricto.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD muestra un RSI de 32.5, acercándose a la zona de sobreventa profunda. Mantenemos la posición actual para acompañar el posible rebote técnico junto con Solana.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 12:20` | 🟢 BUY | `SOL-USD` | $3.42 | $108.91 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 27.1 y una caída acumulada ... |
| `2026-10-12 12:10` | 🟢 BUY | `SOL-USD` | $10.00 | $108.93 | SOL-USD se encuentra en una clara condición de sobreventa técnica con un RSI de 27.2 y una... |
| `2026-10-12 12:01` | 🟢 BUY | `SOL-USD` | $10.00 | $109.96 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 28.5 y una caída semanal de... |
| `2026-10-12 11:50` | 🟢 BUY | `SOL-USD` | $10.00 | $110.00 | SOL-USD presenta un RSI de 28.6 indicando sobreventa extrema y una caída acumulada semanal... |
| `2026-10-12 11:40` | 🔴 SELL | `SOL-USD` | $37.42 | $108.72 | Activación del stop-loss estricto debido a que la posición ha caído un -2.58%, rompiendo e... |

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
