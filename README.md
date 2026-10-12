# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 22:40:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$5.01 USD** | **$36.15 USD** | **$41.16 USD** | 🟢 **+2.90%** ($+1.16) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.289416 | $111.58 | $111.36 | $32.23 | 📉 -0.20% |
| `ETH-USD` | 0.001542 | $2542.73 | $2539.55 | $3.92 | 📉 -0.13% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones de sobreventa extrema, destacando SOL-USD con un RSI de 26.5 y ETH-USD con RSI de 34.0, ideales para nuestra estrategia de rebotes técnicos (mean reversion). Mantenemos nuestras posiciones actuales esperando el rebote alcista, mientras que en el sector tecnológico observamos a MSFT en sobrecompra (RSI 72.3), pero al no estar en cartera y priorizando el despliegue del capital en nuestros activos cripto con descuento, mantenemos una postura de retención y observación sin realizar ventas anticipadas de nuestras posiciones que tienen pérdidas mínimas (-0.2% y -0.13%)."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 85%): SOL-USD se encuentra en una clara sobreventa técnica con un RSI de 26.5, cumpliendo perfectamente con nuestra regla de cazar rebotes. El rendimiento de 24 horas ya muestra un leve repunte (+1.21%). Mantenemos la posición para capturar el objetivo de +2% a +6% de ganancia rápida.

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
