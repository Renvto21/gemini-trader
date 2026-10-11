# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 18:50:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.02 USD** | **$36.82 USD** | **$40.84 USD** | 🟢 **+2.09%** ($+0.84) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.260810 | $111.80 | $110.44 | $28.80 | 📉 -1.22% |
| `ETH-USD` | 0.003174 | $2520.20 | $2524.08 | $8.01 | 📈 +0.15% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado general muestra un tono alcista moderado con SPY y QQQ operando por encima de sus medias móviles y con RSI neutrales alrededor de 55-57. En el sector cripto, SOL-USD y ETH-USD presentan condiciones extremas de sobreventa técnica con RSI de 23.4 y 31.7 respectivamente, tras caídas semanales significativas. Esto activa nuestra estrategia táctica de mean reversion y búsqueda de rebotes rápidos. Dado que nuestra liquidez actual es baja y estamos cerca de los límites de stop-loss en SOL-USD (-1.22%) sin llegar a la ruptura fatal de -2.5%, y con ETH-USD plano, decidimos mantener nuestras posiciones actuales para permitir el rebote esperado desde zona de sobreventa extrema, sin realizar nuevas compras al encontrarnos sin capital libre adicional."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD se encuentra en clara sobreventa con un RSI de 23.4 tras una caída semanal del 8.54%. A pesar de estar en -1.22% de PnL, aún no ha tocado nuestro stop-loss estricto de -2.5%. Las condiciones técnicas de sobreventa extrema sugieren un rebote inminente, por lo que mantenemos la posición para capturar el movimiento alcista.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD muestra un RSI de 31.7, también en zona de sobreventa técnica, operando con un PnL marginalmente positivo del 0.15%. Mantenemos la posición aprovechando el soporte actual para buscar un impulso alcista hacia la resistencia inmediata.

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
