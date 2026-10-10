# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 08:20:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.15 USD** | **$40.26 USD** | 🟢 **+0.66%** ($+0.26) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.44 | $20.08 | 📈 +0.38% |
| `ETH-USD` | 0.006448 | $2481.58 | $2493.34 | $16.08 | 📈 +0.47% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo mixto con criptomonedas fuertemente sobrevendidas tras caídas semanales importantes, destacando SOL-USD con un RSI de 22.0 y ETH-USD con 26.1, lo cual representa una oportunidad clara de rebote técnico (mean reversion). En el sector tecnológico y general, QQQ y SPY mantienen una tendencia alcista saludable, mientras que MSFT ha entrado en sobrecompra técnica con un RSI de 72.3. Nuestra cartera actual mantiene posiciones estancadas en SOL y ETH con pequeñas ganancias, pero la sobreventa extrema en cripto sugiere mantener o buscar oportunidades con descuento, mientras nos mantenemos cerca de nuestra reserva mínima de efectivo."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD presenta condiciones de sobreventa extrema con un RSI de 22.0 tras una caída semanal del -9.95%. Aunque el precio actual muestra un momentum de recuperación muy ligero, mantenemos la posición para capturar el rebote técnico agresivo esperado en cripto hacia la zona de take-profit.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD se encuentra en una situación similar a SOL, con un RSI de 26.1 indicando sobreventa profunda. La posición actual está en terreno ligeramente positivo y la estrategia de momentum nos exige retener el activo para aprovechar la reversión a la media en el corto plazo.

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
