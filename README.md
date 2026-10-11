# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 11:40:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$3.08 USD** | **$37.25 USD** | **$40.32 USD** | 🟢 **+0.81%** ($+0.32) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.340197 | $109.29 | $109.49 | $37.25 | 📈 +0.18% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo alcista moderado en los índices tradicionales como QQQ y SPY, mientras que las criptomonedas como SOL-USD y ETH-USD se encuentran profundamente sobrevendidas con un RSI de 21.4 y 28.5 respectivamente, tras caídas semanales significativas. Nuestra posición actual en SOL-USD muestra un rendimiento plano (+0.18%) y el RSI extremadamente bajo sugiere una inminente oportunidad de rebote técnico (Mean Reversion) a pesar de estar bajo la SMA20. Mantendremos SOL-USD para capturar el rebote esperado hacia el objetivo del +2% al +6%, y dado que el efectivo disponible está ligeramente por debajo de la reserva mínima y no hay urgencia de stop-loss ni take-profit alcanzado, operaremos en modo HOLD para conservar la posición actual y permitir que madure."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 82%): La posición en SOL-USD se mantiene estable con un PnL de +0.18%. El RSI de 14 períodos se encuentra en un nivel extremadamente sobrevendido de 21.4, lo que incrementa fuertemente la probabilidad de un rebote técnico inminente hacia la zona de resistencia cercana. Dado que no ha alcanzado el stop-loss ni el take-profit, y operamos bajo una táctica agresiva de caza de rebotes, la estrategia óptima es retener la posición para capturar el movimiento alcista.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 11:00` | 🟢 BUY | `SOL-USD` | $12.00 | $109.33 | Aprovechamos la altísima sobreventa en SOL-USD (RSI de 21.2 y -9.46% en 7 días) para incre... |
| `2026-10-11 11:00` | 🔴 SELL | `ETH-USD` | $10.00 | $2499.66 | ETH-USD está estancado con un PnL cercano a 0% (-0.03%). Vendemos la posición completa par... |
| `2026-10-11 10:50` | 🟢 BUY | `ETH-USD` | $10.00 | $2500.42 | ETH-USD presenta un RSI de 28.2 en profunda sobreventa y una caída semanal del 7.77%, cump... |
| `2026-10-11 10:50` | 🔴 SELL | `SOL-USD` | $10.93 | $109.32 | Liberamos liquidez de SOL-USD que se encuentra estancada para aprovechar la oportunidad de... |
| `2026-10-11 10:20` | 🔴 SELL | `ETH-USD` | $4.15 | $2504.04 | Vendemos la posición completa en ETH-USD para liberar liquidez. Aunque tiene sobreventa, c... |

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
