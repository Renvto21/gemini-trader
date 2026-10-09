# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-09 20:51:22`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.11 USD** | **$36.07 USD** | **$40.18 USD** | 🟢 **+0.46%** ($+0.18) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.183448 | $109.02 | $109.23 | $20.04 | 📈 +0.19% |
| `ETH-USD` | 0.006448 | $2481.58 | $2487.17 | $16.04 | 📈 +0.23% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado de renta variable tradicional (QQQ, SPY, MSFT) muestra fortaleza alcista con MSFT entrando en zona de sobrecompra (RSI 72.3), mientras que el sector cripto continúa en niveles de sobreventa extrema tras correcciones semanales pronunciadas. SOL-USD (RSI 20.5) y ETH-USD (RSI 25.9) ofrecen configuraciones ideales de reversión a la media con signos tempranos de estabilización técnica. Con una liquidez actual de $4.11 USD que resguarda el colchón mínimo de seguridad de $4.00 USD, las posiciones existentes mantienen un ratio riesgo-beneficio asimétrico a favor del rebote esperado hacia los objetivos de +2.5% a +6.0%."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 88%): SOL-USD presenta un RSI 14 extremo de 20.5 en territorio de fuerte capitulación. La posición se encuentra en leve territorio positivo (+0.19%) y estructurándose para un rebote técnico rápido. Se mantiene para buscar el objetivo de toma de ganancias de +2.5% a +5.0% sin arriesgar capital prematuramente.
- **[HOLD] ETH-USD** (Confianza: 84%): ETH-USD muestra reversión incipiente (+0.62% 24h) tras tocar soporte con RSI de 25.9. Con el PnL actual en +0.23%, se mantiene la posición para capturar el impulso de mean reversion antes de ejecutar rotación de capital o toma de ganancias táctica.

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
