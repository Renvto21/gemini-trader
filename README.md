# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 22:50:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.61 USD** | **$30.45 USD** | **$39.07 USD** | 🔴 **-2.34%** ($-0.93) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.193324 | $103.45 | $104.94 | $20.29 | 📈 +1.44% |
| `ETH-USD` | 0.004136 | $2417.81 | $2458.00 | $10.17 | 📈 +1.66% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto presenta condiciones extremas de sobreventa con RSI de 22.9 en SOL-USD y 28.3 en ETH-USD, lo cual activa nuestra estrategia táctica de rebote por mean reversion. Nuestras posiciones actuales muestran pequeñas ganancias (1.44% y 1.66%) pero aún no alcanzan el objetivo de take-profit del 2.5%. Dado que tenemos liquidez limitada y buscamos capturar el fuerte rebote técnico inminente en cripto, mantendremos las posiciones actuales y esperaremos a que alcancen sus objetivos de ganancia."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD se encuentra en sobreventa extrema (RSI 22.9). Mantenemos la posición para capturar el rebote técnico inminente hacia la zona de take profit sin bloquear más capital.

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
