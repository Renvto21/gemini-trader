# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 18:00:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.01 USD** | **$40.03 USD** | **$40.03 USD** | 🟢 **+0.08%** ($+0.03) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.369549 | $109.24 | $108.31 | $40.03 | 📉 -0.85% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento mixto con ligera presión bajista en criptomonedas y tecnología de alto beta en las últimas 24 horas. Sin embargo, esto genera excelentes oportunidades de sobreventa técnica (mean reversion). SOL-USD se encuentra en una zona de sobreventa extrema con un RSI de 26.4, acumulando una pérdida de -0.85% en nuestra cartera actual. Dado que no ha alcanzado el stop-loss estricto del -3.0%, y basándonos en nuestra táctica agresiva de cazar rebotes en cripto con RSI inferior a 38, mantenemos la posición en SOL-USD esperando un rebote técnico inminente."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): La posición actual en SOL-USD tiene un rendimiento de -0.85%, muy lejos de nuestro stop-loss estricto de -3.0%. Con un RSI extremadamente bajo de 26.4, el activo está en zona de sobreventa profunda y maduro para un rebote técnico rápido. El efectivo disponible es casi nulo (0.01 USD), por lo que mantener la posición maximiza nuestra exposición al potencial rebote sin necesidad de liquidar con pérdidas menores.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 16:40` | 🟢 BUY | `SOL-USD` | $2.95 | $108.01 | Aprovechamos el capital liberado de Ethereum para incrementar la exposición en SOL-USD. Su... |
| `2026-10-12 16:40` | 🔴 SELL | `ETH-USD` | $2.95 | $2515.02 | Vendemos la posición completa en ETH-USD para liberar liquidez y concentrar el capital dis... |
| `2026-10-12 15:40` | 🟢 BUY | `SOL-USD` | $4.00 | $107.58 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 25.6 y una caída acumulada ... |
| `2026-10-12 12:20` | 🟢 BUY | `SOL-USD` | $3.42 | $108.91 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 27.1 y una caída acumulada ... |
| `2026-10-12 12:10` | 🟢 BUY | `SOL-USD` | $10.00 | $108.93 | SOL-USD se encuentra en una clara condición de sobreventa técnica con un RSI de 27.2 y una... |

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
