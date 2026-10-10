# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 07:40:37`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.15 USD** | **$40.26 USD** | 🟢 **+0.65%** ($+0.26) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.45 | $20.08 | 📈 +0.39% |
| `ETH-USD` | 0.006448 | $2481.58 | $2492.52 | $16.07 | 📈 +0.44% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo alcista moderado en los índices tradicionales (SPY, QQQ) y acciones de gran capitalización como MSFT, la cual ha entrado en zona de sobrecompra técnica con un RSI de 72.3. Por otro lado, las criptomonedas continúan con caídas semanales acumuladas pero presentan condiciones extremas de sobreventa con RSI profundamente deprimidos (SOL-USD en 22.1 y ETH-USD en 26.0), lo cual activa nuestra estrategia táctica de mean reversion para capturar un rebote inminente. Dado que nuestras posiciones actuales en SOL-USD y ETH-USD apenas muestran ganancias marginales (+0.39% y +0.44%) sin la fuerza de impulso esperada, y manteniendo una liquidez muy ajustada, la estrategia dicta mantener ambas posiciones actuales ya que están muy cerca de la zona de entrada original y no han tocado los stop-loss, esperando el rebote técnico."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD se encuentra en un estado crítico de sobreventa con un RSI de 22.1 tras una caída semanal del -9.94%. Aunque el rendimiento actual es plano (+0.39%), las reglas operativas de mean reversion respaldan mantener la posición para capturar el rebote técnico hacia el objetivo del +2% al +6%, sin activar el stop-loss ya que la pérdida está contenida.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD registra un RSI de 26.0 reflejando una fuerte sobreventa tras el retroceso semanal. La posición se mantiene intacta con un PnL positivo moderado (+0.44%), esperando el impulso alcista típico de reversión a la media en activos de alta beta.

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
