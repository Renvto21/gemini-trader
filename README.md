# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-09 19:10:55`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$35.93 USD** | **$40.04 USD** | 🟢 **+0.11%** ($+0.04) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $108.71 | $19.94 | 📉 -0.29% |
| `ETH-USD` | 0.006448 | $2481.58 | $2479.90 | $15.99 | 📉 -0.07% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado de criptomonedas muestra una fuerte presión bajista a corto plazo, llevando a activos clave como SOL y ETH a niveles de sobreventa extrema (RSI de 20.0 y 24.6 respectivamente). Mientras tanto, el sector tecnológico (QQQ, SPY, NVDA) mantiene una estructura alcista sobre la SMA20. Esta divergencia sugiere una oportunidad inminente de rebote técnico (Mean Reversion) en las criptomonedas. Con un efectivo de $4.11 (cerca de nuestro límite de reserva de $4.00), la estrategia óptima es mantener nuestras posiciones actuales de alta convicción para capturar la reversión alcista sin realizar ventas prematuras."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 90%): SOL-USD se encuentra en una condición de sobreventa extrema con un RSI de 20.0. A pesar de la tendencia bajista a corto plazo, el precio actual de $108.71 está muy cerca de nuestro precio promedio de compra ($109.02) con una pérdida mínima de -0.29%, muy lejos de nuestro stop-loss de -2.5%. Mantener la posición es clave para capturar el inminente rebote técnico por reversión a la media.
- **[HOLD] ETH-USD** (Confianza: 88%): ETH-USD presenta un RSI de 24.6, lo que indica una fuerte sobreventa en el gráfico diario. Con una pérdida latente de apenas -0.07%, no hay razón para ejecutar un stop-loss. Mantenemos la posición esperando un rebote rápido hacia la media móvil, buscando el objetivo de ganancia del +2.5% al +6%.

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
