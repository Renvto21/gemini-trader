# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 06:00:50`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$6.00 USD** | **$35.38 USD** | **$41.38 USD** | 🟢 **+3.45%** ($+1.38) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.272036 | $111.79 | $111.69 | $30.38 | 📉 -0.09% |
| `ETH-USD` | 0.001958 | $2553.65 | $2550.71 | $4.99 | 📉 -0.12% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra condiciones de sobreventa técnica con SOL-USD (RSI en 32.0) y ETH-USD (RSI en 35.3) operando en rangos atractivos para un rebote por mean reversion. Mantengo mis posiciones actuales ya que están estables con ligeras pérdidas y operan cerca de soportes clave. Por otro lado, MSFT ha entrado en sobrecompra clara con un RSI de 72.3, pero nuestras operaciones se centran en maximizar el capital en cripto y activos de alta volatilidad. Dado que mantenemos una reserva de efectivo estricta de $6.00 USD (por encima del mínimo de $4.00 USD) y las posiciones actuales no han alcanzado los umbrales de stop-loss ni de take-profit significativo, la estrategia óptima en este ciclo es mantener (HOLD) para permitir que los rebotes técnicos en SOL y ETH se desarrollen según lo planeado."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD se encuentra en clara sobreventa técnica con un RSI de 32.0 y tras una caída semanal del -7.53%. Mantenemos la posición para capturar el rebote alcista inminente esperado por la estrategia de mean reversion.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD presenta un RSI de 35.3 y una caída semanal del -5.44%. Al igual que Solana, se mantiene dentro del portafolio esperando la recuperación técnica sin activar aún las reglas de stop-loss o take-profit.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 05:50` | 🟢 BUY | `ETH-USD` | $5.00 | $2553.65 | ETH-USD presenta un RSI de 35.7 en clara zona de sobreventa técnica tras una caída semanal... |
| `2026-10-12 05:50` | 🔴 SELL | `SOL-USD` | $5.00 | $111.85 | Liberamos una pequeña porción de SOL-USD para rescatar liquidez y financiar una entrada tá... |
| `2026-10-12 05:30` | 🔴 SELL | `ETH-USD` | $5.98 | $2553.85 | Rotación activa de capital. ETH se encuentra estancado y bajo su SMA20 con un PnL de -0.33... |
| `2026-10-12 05:20` | 🟢 BUY | `SOL-USD` | $4.00 | $111.70 | SOL-USD se encuentra en clara zona de sobreventa con un RSI de 32 y una caída semanal de -... |
| `2026-10-12 04:50` | 🟢 BUY | `ETH-USD` | $6.00 | $2562.29 | ETH-USD presenta condiciones ideales de sobreventa con un RSI de 36.9 y un descuento del 5... |

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
