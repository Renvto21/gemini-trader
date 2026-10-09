# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-09 19:41:24`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.08 USD** | **$40.19 USD** | 🟢 **+0.47%** ($+0.19) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.22 | $20.04 | 📈 +0.18% |
| `ETH-USD` | 0.006448 | $2481.58 | $2487.94 | $16.04 | 📈 +0.26% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones de sobreventa extrema con SOL-USD en RSI 20.4 y ETH-USD en RSI 26.0, mientras que BTC-USD empieza a liderar una tímida recuperación (+1.09% 24h). El sector tecnológico estadounidense (QQQ, SPY) mantiene sesgo alcista moderado con MSFT en sobrecompra (RSI 72.3). Con una liquidez actual de $4.11 USD justo sobre el umbral de reserva mínima obligatoria ($4.00 USD), el portafolio está óptimamente posicionado en los activos con mayor potencial de rebote elástico (mean reversion)."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 88%): SOL se encuentra en niveles de sobreventa severa con un RSI de 20.4. La posición se mantiene prácticamente en punto de equilibrio (+0.18%). Mantener es la táctica correcta para capturar el rebote proyectado de +2% a +5% antes de aplicar take-profit.
- **[HOLD] ETH-USD** (Confianza: 85%): ETH muestra señales iniciales de giro alcista diario (+0.65%) con RSI profundamente comprimido en 26.0. Dado que la liquidez disponible ($4.11 USD) coincide con la reserva mínima requerida, mantenemos la posición esperando la aceleración del impulso para toma rápida de ganancias.

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
