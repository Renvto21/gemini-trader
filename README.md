# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 07:20:38`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.17 USD** | **$40.28 USD** | 🟢 **+0.69%** ($+0.28) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.53 | $20.09 | 📈 +0.47% |
| `ETH-USD` | 0.006448 | $2481.58 | $2492.77 | $16.07 | 📈 +0.45% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado general muestra un tono moderadamente alcista en los índices principales como SPY y QQQ, mientras que el sector tecnológico y de crecimiento presenta buenos rendimientos. En particular, MSFT ha entrado en territorio de sobrecompra técnica con un RSI de 72.3 tras una fuerte subida del 2.38%. Por otro lado, las criptomonedas continúan con caídas acumuladas en los últimos 7 días, destacando a SOL-USD y ETH-USD en niveles extremos de sobreventa con RSI de 22.4 y 26.0 respectivamente, lo cual activa nuestra estrategia de captura de rebotes por reversión a la media. Con una reserva de efectivo actual muy ajustada ($4.11 USD), mantenemos nuestras posiciones actuales en cripto esperando que materialicen el rebote técnico anticipado."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD se encuentra en un nivel de sobreventa extrema con un RSI de 22.4. Aunque registra una caída semanal del 9.87%, nuestra táctica agresiva busca cazar este tipo de rebotes técnicos. La posición actual se mantiene intacta para capturar el repunte inminente hacia la media.

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
