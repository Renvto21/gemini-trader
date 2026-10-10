# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 03:00:49`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.29 USD** | **$40.41 USD** | 🟢 **+1.01%** ($+0.41) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $110.09 | $20.20 | 📈 +0.98% |
| `ETH-USD` | 0.006448 | $2481.58 | $2496.89 | $16.10 | 📈 +0.62% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento mixto con el sector tecnológico y los índices principales (QQQ, SPY) con tendencias alcistas estables, mientras que las criptomonedas (SOL-USD y ETH-USD) continúan mostrando condiciones de sobreventa extrema con un RSI de 23.0 y 27.5 respectivamente, tras caídas semanales cercanas al 7-8%. Mantenemos nuestras posiciones en cripto esperando un rebote técnico inminente de mean-reversion, y dado que nuestro efectivo actual es de $4.11 USD (cumpliendo con la reserva mínima de $4.00 USD), no realizaremos nuevas compras ni ventas en este ciclo, optando por un HOLD estratégico."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD se encuentra en un estado de sobreventa extrema con un RSI de 23.0. Aunque presenta una tendencia bajista a corto plazo, el potencial de un rebote técnico rápido hacia la media es alto. Nuestra posición actual tiene un PnL positivo del 0.98% y preferimos mantenerla para capturar el movimiento alcista proyectado sin sobrepasar el efectivo mínimo.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD muestra un RSI de 27.5, indicando clara sobreventa tras caídas recientes. La posición actual genera una ganancia moderada del 0.62% y se encuentra alineada con nuestra táctica agresiva de cazar rebotes en cripto, por lo que mantenemos el activo esperando mayor impulso.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-09 19:00` | 🟢 BUY | `ETH-USD` | $5.00 | $2482.07 | ETH-USD se encuentra en una zona de sobreventa extrema con un RSI de 25.0. Utilizando el c... |
| `2026-10-09 19:00` | 🔴 SELL | `NVDA` | $4.99 | $229.28 | Rotación activa de capital. NVDA se encuentra estancada con un rendimiento de -0.16% y un ... |
| `2026-10-09 18:50` | 🟢 BUY | `SOL-USD` | $5.00 | $108.91 | Oportunidad de alta convicción por sobreventa extrema. SOL-USD tiene un RSI de 20.2 tras u... |
| `2026-10-09 18:50` | 🔴 SELL | `QQQ` | $5.00 | $751.27 | Rotación de capital activo. QQQ se encuentra estancado con rendimiento plano (-0.06%) y si... |
| `2026-10-09 18:40` | 🟢 BUY | `SOL-USD` | $5.00 | $109.02 | SOL-USD está extremadamente sobrevendido con un RSI de 20.3. Ejecutamos una compra agresiv... |

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
