# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 17:00:48`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.01 USD** | **$39.99 USD** | **$40.00 USD** | 🟢 **-0.00%** ($-0.00) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.369549 | $109.24 | $108.22 | $39.99 | 📉 -0.93% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un tono de corrección moderada, con criptomonedas como ETH-USD y SOL-USD en zonas de sobreventa técnica profunda (RSI de 32 y 26.3 respectivamente). Nuestra posición actual en SOL-USD registra una pequeña pérdida no realizada del -0.93%, manteniéndose muy por encima de nuestro límite de stop-loss estricto (-2.5% a -3.0%). Dado que el RSI de SOL-USD se encuentra en niveles extremos de sobreventa, mantenemos la posición para capturar el rebote técnico esperado."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): La posición actual en SOL-USD muestra un RSI de 26.3 indicando sobreventa extrema. La pérdida actual es de -0.93%, lo cual está dentro de los límites de tolerancia y lejos del stop-loss. Esperamos el rebote técnico para buscar un take-profit cercano al +2.5%.

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
