# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-09 15:21:31`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$20.00 USD** | **$4.00 USD** | **$16.11 USD** | **$20.11 USD** | 🟢 **+0.54%** ($+0.11) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.017822 | $336.67 | $335.63 | $5.98 | 📉 -0.31% |
| `SPY` | 0.006458 | $774.29 | $778.47 | $5.03 | 📈 +0.54% |
| `GLD` | 0.013253 | $377.27 | $384.85 | $5.10 | 📈 +2.01% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un comportamiento mixto. Los índices tradicionales como el SPY y QQQ mantienen una tendencia alcista saludable con RSIs moderados. Las criptomonedas (ETH, SOL) presentan condiciones de fuerte sobreventa (RSI < 30) pero con tendencias bajistas marcadas, lo que sugiere precaución. MSFT se encuentra en territorio de sobrecompra (RSI 72). Con un efectivo actual de $4.00 USD, estamos muy cerca del límite mínimo de reserva de $3.00 USD. Por lo tanto, la estrategia más prudente en este ciclo es mantener nuestras posiciones actuales (HOLD) para preservar la liquidez y observar la evolución de los activos en cartera."*

**Operaciones del ciclo:**
- **[HOLD] SPY** (Confianza: 90%): SPY mantiene una tendencia alcista sólida sobre la SMA20 y un RSI saludable de 55.5. No hay razones para vender y no disponemos de suficiente efectivo libre para incrementar la posición de forma segura.
- **[HOLD] AAPL** (Confianza: 85%): AAPL se encuentra en tendencia alcista con un RSI cómodo de 46.2. Aunque presenta una leve pérdida latente del 0.31%, el activo está bien posicionado para recuperarse.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-08 15:41` | 🟢 BUY | `GLD` | $5.00 | $377.27 | GLD presenta un RSI de 27.3, lo que indica condiciones de sobreventa extrema en un activo ... |
| `2026-10-08 15:23` | 🟢 BUY | `SPY` | $5.00 | $774.29 | SPY presenta una tendencia alcista sólida sobre su SMA20 y un RSI de 62.1, lo que indica q... |
| `2026-10-07 23:09` | 🟢 BUY | `AAPL` | $6.00 | $336.67 | AAPL es la opción más equilibrada del mercado actual: mantiene una tendencia alcista confi... |

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
