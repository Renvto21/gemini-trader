# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-09 21:11:03`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.02 USD** | **$40.13 USD** | 🟢 **+0.33%** ($+0.13) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.00 | $20.00 | 📉 -0.02% |
| `ETH-USD` | 0.006448 | $2481.58 | $2485.34 | $16.02 | 📈 +0.15% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto presenta condiciones de sobreventa extrema técnica con SOL-USD (RSI 20.2) y ETH-USD (RSI 25.5) en zonas óptimas para una reversión a la media agresiva. Por otro lado, la renta variable tecnológica (QQQ, MSFT, NVDA) muestra signos de agotamiento y consolidación tras subidas previas con RSI elevado (>60). Con un efectivo libre disponible de $4.11 frente a la reserva mandatoria de $4.00, no hay liquidez suficiente para nuevas aperturas sin liquidar. Dado que ambas posiciones están prácticamente en punto de equilibrio y en el epicentro de la configuración de rebote, la estrategia óptima es mantener la exposición para capturar el impulso de rebote proyectado del +2% al +5%."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 88%): SOL se encuentra en niveles de sobreventa técnica extrema con RSI en 20.2. La posición está en precio de entrada (PnL -0.02%), sin activar stop-loss (-2.5%) ni take-profit (+2.5%). Mantenemos con alta convicción a la espera del rebote táctico.
- **[HOLD] ETH-USD** (Confianza: 85%): ETH muestra señales tempranas de estabilización (+0.54% en 24h) con RSI en 25.5, confirmando configuración de reversión alcista inminente. El PnL se mantiene neutral (+0.15%), por lo que conservamos la posición buscando el objetivo del +2.5% a +6%.

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
