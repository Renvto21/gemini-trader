# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 04:30:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$39.97 USD** | **$39.97 USD** | 🔴 **-0.09%** ($-0.03) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.295191 | $107.17 | $108.09 | $31.91 | 📈 +0.86% |
| `ETH-USD` | 0.003192 | $2506.03 | $2524.40 | $8.06 | 📈 +0.73% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un rebote técnico interesante en las principales criptomonedas tras caídas recientes de 7 días. Solana (SOL-USD) se encuentra en clara sobreventa con un RSI de 30.0 y un incremento del 2.4% en 24 horas, lo que valida nuestra tesis de rebote por mean reversion. Ethereum (ETH-USD) también muestra un repunte del 3.27% con un RSI de 37.6. Ambas posiciones en cartera muestran ganancias menores (+0.86% y +0.73%) pero aún no alcanzan el objetivo de take-profit del +2.5%. Dado que el capital está totalmente invertido y no hay suficiente liquidez para nuevas compras sin liquidar, y las posiciones actuales están consolidando su rebote técnico sin tocar stop-loss, la estrategia óptima es mantener (HOLD) para permitir que alcancen el objetivo de ganancia rápida."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): La posición tiene una ganancia actual de +0.86%. El RSI de 30.0 y el cambio de +2.4% en 24h confirman que el rebote técnico está en desarrollo. Mantenemos la posición para buscar el objetivo de take-profit superior al +2.5%.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH muestra un avance del 3.27% en 24h y un RSI saliendo de la zona de sobreventa (37.6). Se mantiene para capturar mayor recorrido alcista antes de ejecutar la toma de ganancias.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 02:30` | 🟢 BUY | `SOL-USD` | $4.00 | $108.19 | SOL-USD presenta un RSI extremadamente bajo de 26.3, lo que indica sobreventa técnica seve... |
| `2026-10-13 01:30` | 🟢 BUY | `SOL-USD` | $6.23 | $107.75 | SOL-USD se encuentra en una zona de sobreventa extrema con un RSI de 25.8 tras una caída s... |
| `2026-10-13 01:10` | 🟢 BUY | `ETH-USD` | $8.00 | $2506.03 | ETH-USD se encuentra en clara sobreventa técnica con un RSI de 31.1 tras una caída semanal... |
| `2026-10-13 01:10` | 🔴 SELL | `SOL-USD` | $16.14 | $107.57 | Vendemos parcialmente SOL-USD para liberar liquidez y poder financiar la entrada en ETH-US... |
| `2026-10-13 01:00` | 🟢 BUY | `SOL-USD` | $12.00 | $107.31 | Aprovechamos la sobreventa extrema de SOL-USD (RSI 25.3 y caída semanal de -11.16%) para i... |

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
