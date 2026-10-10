# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-09 22:32:06`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.12 USD** | **$40.23 USD** | 🟢 **+0.57%** ($+0.23) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.41 | $20.07 | 📈 +0.36% |
| `ETH-USD` | 0.006448 | $2481.58 | $2488.50 | $16.04 | 📈 +0.28% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado de renta variable tecnológica (QQQ, NVDA, MSFT) muestra señales de consolidación y niveles de RSI elevados, mientras que el sector cripto se encuentra en una fase extrema de sobreventa técnica tras fuertes correcciones semanales. Específicamente, SOL-USD (RSI 20.6) y ETH-USD (RSI 26.1) presentan condiciones óptimas de reversión a la media (Mean Reversion). Dado que ya poseemos exposición total en ambos activos adquiridos en mínimos recientes y el efectivo restante ($4.11 USD) cumple con la reserva mínima de liquidez ($4.00 USD), la estrategia óptima es mantener posiciones a la espera de la expansión de volatilidad hacia nuestros objetivos de toma de ganancias (+2.5% a +6%)."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 88%): SOL-USD registra un RSI extremadamente deprimido de 20.6 y una caída semanal acumulada de -8.55%. La posición actual mantiene un PnL positivo (+0.36%) y está perfectamente ubicada para capturar el rebote técnico rápido. No ha alcanzado el umbral de toma de ganancias (+2.5%) ni ha roto soportes para stop-loss (-2.5%), por lo que se mantiene para maximizar el retorno del rebote.
- **[HOLD] ETH-USD** (Confianza: 84%): ETH-USD muestra divergencia positiva en 24h (+0.67%) con un RSI profundamente sobrevendido en 26.1. La posición se encuentra en verde (+0.28%) y con fuerte potencial de mean reversion hacia su media móvil de corto plazo. Se mantiene la posición intacta respetando la disciplina de no cortar prematuramente las ganancias antes del objetivo del +2.5%.

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
