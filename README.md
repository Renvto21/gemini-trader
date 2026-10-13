# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 22:30:57`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.61 USD** | **$30.31 USD** | **$38.92 USD** | 🔴 **-2.69%** ($-1.08) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.193324 | $103.45 | $104.40 | $20.18 | 📈 +0.92% |
| `ETH-USD` | 0.004136 | $2417.81 | $2449.11 | $10.13 | 📈 +1.29% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto presenta una fuerte sobreventa técnica con SOL-USD (RSI 22.5) y ETH-USD (RSI 27.8) cayendo bruscamente, lo cual activa nuestra estrategia táctica de buscar rebotes en zonas extremas. Aunque nuestras posiciones actuales están ligeramente en positivo (+0.92% y +1.29%), aún no alcanzan la meta de take-profit del +2.5% pero muestran resiliencia frente a la caída general. Mantenemos liquidez y posiciones para capturar el rebote técnico inminente en cripto sin realizar nuevas compras en este ciclo exacto para proteger el efectivo."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): El RSI de 22.5 indica una sobreventa extrema ideal para un rebote de mean reversion. Aunque el precio ha retrocedido un 6.15% en 24h, mantenemos la posición para capturar el próximo impulso alcista hacia el objetivo de take-profit del 2.5%.
- **[HOLD] ETH-USD** (Confianza: 75%): Con un RSI de 27.8, ETH se encuentra en zona de sobreventa técnica. La posición actual muestra una ganancia leve de +1.29%; esperamos que continúe el rebote para asegurar ganancias cuando toque el umbral del 2.5% o superior.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 22:00` | 🟢 BUY | `SOL-USD` | $10.00 | $103.02 | SOL-USD presenta un RSI extremadamente bajo de 21.3 tras una caída del -7.39% en 24 horas.... |
| `2026-10-12 21:50` | 🟢 BUY | `ETH-USD` | $10.00 | $2417.81 | ETH-USD se encuentra en una profunda corrección con una caída de -4.61% en 24h y un RSI de... |
| `2026-10-12 21:40` | 🟢 BUY | `SOL-USD` | $10.00 | $103.89 | SOL-USD se encuentra en una situación clara de sobreventa extrema (RSI de 22.0) tras caer ... |
| `2026-10-12 21:30` | 🔴 SELL | `ETH-USD` | $11.71 | $2419.82 | La posición registra una pérdida del -2.44% bajo una tendencia bajista marcada y un RSI de... |
| `2026-10-12 21:30` | 🔴 SELL | `SOL-USD` | $22.91 | $103.78 | La posición ha acumulado una pérdida del -2.64%, acercándose peligrosamente al stop-loss e... |

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
