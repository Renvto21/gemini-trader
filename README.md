# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 05:20:49`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.02 USD** | **$41.35 USD** | **$41.37 USD** | 🟢 **+3.44%** ($+1.37) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.316736 | $111.79 | $111.70 | $35.38 | 📉 -0.08% |
| `ETH-USD` | 0.002342 | $2562.29 | $2550.20 | $5.97 | 📉 -0.47% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones de sobreventa técnica con SOL-USD (RSI en 32.0) y ETH-USD (RSI en 35.3) operando cerca de soportes y con caídas recientes en los últimos 7 días. Ambas posiciones actuales se mantienen estables con pérdidas marginales, por lo que decidimos mantenerlas y acumular más en SOL-USD aprovechando la zona de sobreventa para capturar un rebote técnico inminente."*

**Operaciones del ciclo:**
- **[BUY] SOL-USD** (Confianza: 85%): SOL-USD se encuentra en clara zona de sobreventa con un RSI de 32 y una caída semanal de -7.52%. Esto representa una oportunidad ideal de mean reversion para cazar un rebote rápido, cumpliendo con la regla de aprovechar criptomonedas con RSI inferior a 38.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 05:20` | 🟢 BUY | `SOL-USD` | $4.00 | $111.70 | SOL-USD se encuentra en clara zona de sobreventa con un RSI de 32 y una caída semanal de -... |
| `2026-10-12 04:50` | 🟢 BUY | `ETH-USD` | $6.00 | $2562.29 | ETH-USD presenta condiciones ideales de sobreventa con un RSI de 36.9 y un descuento del 5... |
| `2026-10-12 04:30` | 🔴 SELL | `ETH-USD` | $10.02 | $2567.68 | Rotación activa de capital. ETH muestra una ganancia marginal del 0.23% sin momentum fuert... |
| `2026-10-12 03:40` | 🟢 BUY | `SOL-USD` | $4.00 | $112.34 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 29.5 y una caída semanal de... |
| `2026-10-12 03:20` | 🟢 BUY | `SOL-USD` | $2.92 | $112.10 | Aprovechamos la reserva de efectivo por encima del mínimo requerido ($4.00) para increment... |

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
