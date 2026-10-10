# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-09 23:20:38`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.20 USD** | **$40.31 USD** | 🟢 **+0.77%** ($+0.31) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.72 | $20.13 | 📈 +0.64% |
| `ETH-USD` | 0.006448 | $2481.58 | $2492.23 | $16.07 | 📈 +0.43% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento mixto con el sector tecnológico y SPY/QQQ manteniendo tendencias alcistas moderadas, mientras que las criptomonedas (SOL y ETH) han experimentado caídas semanales significativas pero presentan condiciones extremas de sobreventa con RSI en 21.7 y 26.7 respectivamente, lo cual activa nuestra estrategia de reverso a la media para cazar rebotes agresivos. Mantenemos nuestras posiciones actuales con pequeñas ganancias y conservamos la reserva mínima de liquidez de 4.11 USD, decidiendo mantener la cartera actual para permitir que el rebote técnico en SOL y ETH se desarrolle plenamente."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 88%): SOL se encuentra en una situación clara de sobreventa extrema con un RSI de 21.7 y una caída semanal del -8.3 por ciento. Mantenemos la posición para capturar el rebote técnico esperado hacia la resistencia inmediata, alineado con nuestra estrategia de cazar sobreventas en criptoactivos.
- **[HOLD] ETH-USD** (Confianza: 85%): ETH muestra un RSI de 26.7 y un descuento semanal del -7.26 por ciento. Aunque la tendencia es bajista a corto plazo, el nivel de sobreventa favorece un rebote inminente de mean reversion que nos permitirá asegurar ganancias rápidas.

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
