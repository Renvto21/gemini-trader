# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 11:20:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$3.08 USD** | **$37.20 USD** | **$40.27 USD** | 🟢 **+0.68%** ($+0.27) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.340197 | $109.29 | $109.34 | $37.20 | 📈 +0.04% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra una divergencia interesante: mientras los índices generales y tecnologias de gran capitalización como QQQ y SPY mantienen una tendencia alcista moderada, los activos cripto (especialmente SOL-USD y ETH-USD) se encuentran en condiciones extremas de sobreventa técnica con RSI de 21.2 y 28.2 respectivamente. Mantengo nuestra posición actual en SOL-USD ya que está en niveles ideales para un rebote de reversión a la media, y el efectivo actual está ligeramente por debajo de la reserva mínima pero la posición está estancada con ganancia marginal del 0.04%."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD presenta un RSI extremadamente bajo de 21.2, lo que indica una sobreventa severa y una alta probabilidad de un rebote técnico a corto plazo tal como dicta nuestra estrategia de Mean Reversion. Dado que nuestra PnL está plana (0.04%) y no ha tocado nuestro stop-loss estricto, mantenemos la posición para capturar el esperado impulso alcista.

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
