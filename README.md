# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 23:00:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.61 USD** | **$30.51 USD** | **$39.13 USD** | 🔴 **-2.18%** ($-0.87) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.193324 | $103.45 | $105.20 | $20.34 | 📈 +1.69% |
| `ETH-USD` | 0.004136 | $2417.81 | $2460.49 | $10.18 | 📈 +1.77% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto presenta condiciones extremas de sobreventa con RSI en niveles muy bajos (SOL en 23.2 y ETH en 28.4), lo que activa nuestra estrategia agresiva de caza de rebotes técnicos (Mean Reversion). Las posiciones actuales muestran ganancias moderadas (+1.69% y +1.77%) pero aún no alcanzan el objetivo estricto de take-profit del +2.5% o sobrecompra en RSI. Con un efectivo disponible de 8.61 USD y manteniendo nuestra reserva mínima, decidimos mantener la disciplina y esperar a que las posiciones actuales alcancen su objetivo de venta o busquen un rebalanceo táctico."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): La posición en SOL-USD muestra un rendimiento positivo de +1.69% tras el fuerte castigo del mercado. Aunque está en niveles profundos de sobreventa técnica, el precio aún no cruza el umbral del +2.5% para asegurar beneficios, por lo que mantenemos la posición para capturar el rebote completo.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD registra una ganancia actual de +1.77% operando con un RSI de 28.4. Mantenemos la posición activa para buscar la toma de ganancias cercana al +2.5% o la entrada en sobrecompra, optimizando la rotación de capital según las reglas tácticas.

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
