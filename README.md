# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 13:10:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.12 USD** | **$18.99 USD** | **$41.11 USD** | 🟢 **+2.78%** ($+1.11) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.170099 | $109.29 | $111.67 | $18.99 | 📈 +2.18% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento mixto con sesgo alcista moderado en los índices principales (SPY y QQQ con tendencias alcistas saludables). En el sector cripto, SOL-USD y ETH-USD muestran signos tempranos de recuperación tras una corrección de 7 días, con SOL-USD en fuerte sobreventa técnica (RSI 27.4) iniciando un rebote (P&L actual de +2.18%). ETH-USD se mantiene plano con un RSI en 32.6, mientras que MSFT muestra sobrecompra (RSI 72.3). La estrategia actual dicta mantener el momentum en SOL-USD que se acerca a la toma de ganancias, y liquidar posiciones sin impulso como ETH-USD para liberar efectivo y buscar mejores oportunidades."*

**Operaciones del ciclo:**
- **[SELL] ETH-USD** (Confianza: 85%): ETH-USD se encuentra estancado con un P&L cercano a 0% (-0.06%) y bajo tendencia bajista en SMA20. Aplicando la regla de rotación activa, liquidamos esta posición para liberar efectivo y financiar oportunidades de mayor impulso.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 13:10` | 🔴 SELL | `ETH-USD` | $9.99 | $2530.10 | ETH-USD se encuentra estancado con un P&L cercano a 0% (-0.06%) y bajo tendencia bajista e... |
| `2026-10-11 13:00` | 🟢 BUY | `ETH-USD` | $10.00 | $2531.65 | ETH-USD se encuentra en clara sobreventa técnica con un RSI de 32.8 y una fuerte caída sem... |
| `2026-10-11 13:00` | 🔴 SELL | `SOL-USD` | $19.02 | $111.81 | Tomamos beneficios de manera parcial en SOL-USD ya que la posición acumula una ganancia ce... |
| `2026-10-11 12:50` | 🔴 SELL | `ETH-USD` | $3.10 | $2526.95 | Vendemos la posición completa de ETH-USD para liberar capital en efectivo y aprovechar las... |
| `2026-10-11 12:10` | 🟢 BUY | `ETH-USD` | $3.08 | $2504.75 | ETH-USD se encuentra en un estado de sobreventa extrema con un RSI de 28.6 y una caída sem... |

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
