# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-10 05:50:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.22 USD** | **$40.33 USD** | 🟢 **+0.82%** ($+0.33) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.82 | $20.15 | 📈 +0.73% |
| `ETH-USD` | 0.006448 | $2481.58 | $2492.72 | $16.07 | 📈 +0.45% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento mixto con el sector tecnológico y los índices principales (QQQ, SPY) registrando tendencias alcistas estables, mientras que las criptomonedas (SOL-USD y ETH-USD) se encuentran en condiciones de sobreventa extrema (RSI de 23.4 y 26.0 respectivamente), lo cual presenta una oportunidad ideal de rebote técnico (Mean Reversion). Dado que el efectivo disponible es de apenas $4.11 USD y las posiciones actuales aún no alcanzan el objetivo de take-profit del +2.5% ni han roto el stop-loss, mantendremos la postura en nuestra cartera actual para permitir que madure el rebote esperado en cripto."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD muestra un RSI de sobreventa extrema en 23.4 tras una caída semanal del 9.63%. Estamos posicionados con una pequeña ganancia del 0.73% y mantenemos la operación para capturar el rebote técnico hacia la zona de resistencia superior.
- **[HOLD] ETH-USD** (Confianza: 82%): ETH-USD presenta un RSI en 26.0, reflejando condiciones similares de sobreventa. Mantenemos la posición actual para aprovechar la recuperación esperada en el sector cripto, manteniendo bajo control el riesgo con nuestro plan táctico.

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
