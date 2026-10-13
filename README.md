# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 22:00:50`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.61 USD** | **$29.93 USD** | **$38.55 USD** | 🔴 **-3.64%** ($-1.45) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.193324 | $103.45 | $103.02 | $19.92 | 📉 -0.42% |
| `ETH-USD` | 0.004136 | $2417.81 | $2421.93 | $10.02 | 📈 +0.17% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones de sobreventa extrema lideradas por caídas recientes en SOL-USD (RSI de 21.3) y ETH-USD (RSI de 26.5), lo cual activa nuestra estrategia táctica de mean reversion para cazar rebotes técnicos rápidos. Mantenemos nuestras posiciones actuales dado que muestran un comportamiento defensivo razonable frente a la caída general, y utilizaremos el efectivo disponible para promediar o capturar un activo adicional con descuento."*

**Operaciones del ciclo:**
- **[BUY] SOL-USD** (Confianza: 88%): SOL-USD presenta un RSI extremadamente bajo de 21.3 tras una caída del -7.39% en 24 horas. Esta es una oportunidad clásica de sobreventa para capturar un rebote técnico rápido del 3% al 5% aprovechando la alta volatilidad, cumpliendo con la regla de alta convicción.

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
