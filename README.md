# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 16:50:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.01 USD** | **$39.96 USD** | **$39.97 USD** | 🔴 **-0.07%** ($-0.03) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.369549 | $109.24 | $108.14 | $39.96 | 📉 -1.01% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra una corrección moderada con activos cripto y tecnológicos bajo presión a corto plazo. SOL-USD se encuentra en clara sobreventa técnica con un RSI de 26.2, lo cual activa nuestra estrategia de mean reversion para buscar un rebote rápido a pesar de la tendencia bajista actual. Mantenemos nuestra posición actual mientras evaluamos el comportamiento del precio."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición actual en SOL-USD registra una pérdida leve del -1.01%, muy lejos de nuestro stop-loss estricto de -2.5% a -3.0%. Con un RSI de 26.2 en zona de profunda sobreventa, el activo mantiene altas probabilidades de un rebote técnico inminente, por lo que decidimos mantener la posición para capturar el movimiento alcista.

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
