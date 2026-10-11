# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 11:30:37`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$3.08 USD** | **$37.22 USD** | **$40.29 USD** | 🟢 **+0.73%** ($+0.29) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.340197 | $109.29 | $109.40 | $37.22 | 📈 +0.10% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra oportunidades claras de sobreventa extrema en criptomonedas clave como ETH-USD con un RSI de 28.4, mientras que SOL-USD se mantiene en sobreventa profunda (RSI de 21.3) pero sin momentum alcista inmediato. En el sector tecnológico, MSFT ha entrado en sobrecompra (RSI de 72.3) con un fuerte incremento diario del 2.38%. Dado que nuestra estrategia busca cazar rebotes y rotar capital con dinamismo, mantendremos nuestra posición en SOL-USD mientras consolida y aprovecharemos la oportunidad de extrema sobreventa en ETH-USD para capturar un rebote técnico rápido."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición en SOL-USD se mantiene cerca del precio de entrada (pnl de +0.1%) y aunque presenta un RSI extremadamente bajo de 21.3, no ha activado el stop-loss estricto ni muestra una caída profunda que obligue a salir. Esperaremos su consolidación para buscar una salida en ganancia.

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
