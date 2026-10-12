# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 22:00:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$5.01 USD** | **$36.20 USD** | **$41.21 USD** | 🟢 **+3.03%** ($+1.21) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.289416 | $111.58 | $111.53 | $32.28 | 📉 -0.05% |
| `ETH-USD` | 0.001542 | $2542.73 | $2542.93 | $3.92 | 📈 +0.01% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo alcista moderado en índices tradicionales como QQQ y SPY, mientras que las criptomonedas (SOL y ETH) muestran condiciones de sobreventa técnica con RSI en niveles de 27.0 y 34.5 respectivamente, lo cual presenta una oportunidad ideal para buscar un rebote por mean reversion. El portafolio actual está completamente invertido (liquidez casi en cero) y las posiciones en SOL y ETH se encuentran estancadas cerca del 0% de PnL. Rotaremos una parte pequeña para liberar efectivo y cumplir con la estrategia."*

**Operaciones del ciclo:**
- **[SELL] ETH-USD** (Confianza: 85%): Vendemos parcialmente la posición en ETH-USD para liberar efectivo y cumplir con la regla de reserva mínima de liquidez, permitiendo capitalizar la fuerte sobreventa en SOL-USD y mantener rotación dinámica en el portafolio.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 22:00` | 🔴 SELL | `ETH-USD` | $5.00 | $2542.93 | Vendemos parcialmente la posición en ETH-USD para liberar efectivo y cumplir con la regla ... |
| `2026-10-11 21:50` | 🟢 BUY | `ETH-USD` | $8.92 | $2542.73 | ETH-USD está en condiciones de clara sobreventa técnica (RSI de 34.5) tras una caída seman... |
| `2026-10-11 21:50` | 🔴 SELL | `SOL-USD` | $8.93 | $111.63 | Liberamos una fracción de la posición en SOL-USD que se encuentra estancada con rendimient... |
| `2026-10-11 21:20` | 🟢 BUY | `SOL-USD` | $4.24 | $111.11 | Aprovechamos el capital liberado para incrementar la exposición en SOL-USD. Se encuentra e... |
| `2026-10-11 21:20` | 🔴 SELL | `ETH-USD` | $4.24 | $2534.63 | Vendemos la totalidad de la posición en ETH-USD (valorada en aproximadamente 4.24 USD) par... |

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
