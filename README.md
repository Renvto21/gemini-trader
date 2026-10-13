# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 03:50:38`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$40.14 USD** | **$40.14 USD** | 🟢 **+0.35%** ($+0.14) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.295191 | $107.17 | $108.59 | $32.05 | 📈 +1.32% |
| `ETH-USD` | 0.003192 | $2506.03 | $2532.58 | $8.08 | 📈 +1.06% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo mixto con tendencia bajista temporal en cripto y activos de alta beta como SOL y ETH, donde SOL presenta un RSI de sobreventa extrema en 26.7 y ETH se encuentra en 32.9. La estrategia agresiva de rotación y captura de rebotes técnicos nos obliga a mantener posiciones y buscar oportunidades de entrada o asegurar beneficios según el comportamiento del precio."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): A pesar de la caída reciente de 24 horas y el RSI de 26.7 que indica sobreventa, la posición mantiene un rendimiento positivo de +1.32% y estamos cazando un rebote inminente por mean reversion sin necesidad de vender antes de alcanzar nuestro objetivo de take-profit.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH muestra un RSI de 32.9 acercándose a la zona de sobreventa con un rendimiento actual de +1.06%. Mantenemos la posición para capturar el rebote técnico hacia el objetivo de ganancia del +2.5%.

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
