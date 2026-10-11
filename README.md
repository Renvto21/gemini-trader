# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 19:20:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.02 USD** | **$37.00 USD** | **$41.02 USD** | 🟢 **+2.55%** ($+1.02) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.260810 | $111.80 | $111.04 | $28.96 | 📉 -0.68% |
| `ETH-USD` | 0.003174 | $2520.20 | $2531.63 | $8.04 | 📈 +0.45% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado general muestra un tono mixto con sesgo alcista moderado en los índices (SPY y QQQ sobre la SMA20). En el sector cripto, SOL-USD y ETH-USD se encuentran en condiciones claras de sobreventa técnica (RSI de 25.4 y 32.8 respectivamente) tras caídas semanales significativas, lo que activa nuestra estrategia de captura de rebotes por reversión a la media. Mantendremos las posiciones actuales ya que muestran señales de estabilización en 24 horas y el efectivo disponible está en los mínimos operativos permitidos."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 82%): SOL-USD presenta un RSI muy deprimido en 25.4, lo que indica sobreventa extrema y un potencial rebote técnico inminente. La pérdida actual es marginal (-0.68%) y se mantiene dentro de los límites de tolerancia, por lo que retener la posición aprovecha la alta volatilidad para buscar la recuperación.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 18:20` | 🟢 BUY | `ETH-USD` | $8.00 | $2520.20 | ETH-USD presenta un RSI de 31.1 y una caída acumulada del 7.04% en los últimos 7 días, sit... |
| `2026-10-11 17:50` | 🔴 SELL | `ETH-USD` | $12.02 | $2536.22 | ETH-USD se encuentra estancado con una ganancia mínima de +0.19% y bajo una tendencia baji... |
| `2026-10-11 17:40` | 🟢 BUY | `SOL-USD` | $4.00 | $111.14 | SOL-USD se encuentra en una clara condición de sobreventa técnica con un RSI de 25.7 y una... |
| `2026-10-11 14:10` | 🟢 BUY | `SOL-USD` | $5.16 | $111.90 | SOL-USD presenta un RSI de 28.2 indicando sobreventa clara tras una caída semanal del 7.33... |
| `2026-10-11 14:00` | 🟢 BUY | `SOL-USD` | $10.00 | $112.02 | SOL-USD se encuentra en clara sobreventa tecnica con un RSI de 28.5 tras una caida semanal... |

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
