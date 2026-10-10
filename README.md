# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 04:00:49`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.21 USD** | **$40.32 USD** | 🟢 **+0.80%** ($+0.32) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.80 | $20.14 | 📈 +0.71% |
| `ETH-USD` | 0.006448 | $2481.58 | $2492.12 | $16.07 | 📈 +0.42% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento mixto con sesgo alcista moderado en el sector tecnológico y el S&P 500 (SPY y QQQ con RSI neutrales/alcistas). Destaca MSFT con un fuerte impulso diario (+2.38%) y RSI en sobrecompra (72.3). En el sector cripto, SOL-USD y ETH-USD presentan condiciones extremas de sobreventa con RSI de 22.0 y 26.7 respectivamente, lo cual activa nuestras reglas tácticas de mean reversion (cazar rebotes). Dado que nuestras posiciones actuales en SOL y ETH están estancadas con ganancias mínimas (< 1%) y el efectivo disponible es bajo (4.11 USD), optamos por mantenerlas firmemente a la espera del rebote técnico agresivo, ya que el riesgo bajista está controlado y la sobreventa sugiere una recuperación inminente."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD se encuentra en una situación clara de sobreventa extrema con un RSI de 22.0 tras una caída semanal del -8.23%. Mantenemos la posición actual para capitalizar el rebote técnico esperado, acorde con nuestra estrategia de mean reversion, sin realizar nuevas compras por el límite de liquidez en efectivo.
- **[HOLD] ETH-USD** (Confianza: 82%): ETH-USD registra un RSI de 26.7 y una caída semanal del -7.26%. Mantenemos la posición ya que las condiciones técnicas de sobreventa indican una alta probabilidad de un rebote a corto plazo hacia nuestra zona de take-profit.

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
