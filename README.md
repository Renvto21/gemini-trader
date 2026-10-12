# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 06:50:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$37.28 USD** | **$41.28 USD** | 🟢 **+3.21%** ($+1.28) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.272036 | $111.79 | $111.35 | $30.29 | 📉 -0.39% |
| `ETH-USD` | 0.002742 | $2553.19 | $2549.37 | $6.99 | 📉 -0.15% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento mixto con el sector tech liderado por QQQ y SPY con tendencias alcistas saludables. Por otro lado, las criptomonedas se encuentran en zonas de sobreventa interesante (RSI de SOL-USD en 30.8 y ETH-USD en 35.1), lo cual representa una oportunidad táctica de rebote (mean reversion). Dado que mantenemos una reserva estricta de efectivo, decidimos mantener nuestras posiciones en cripto que están cerca de la zona de soporte para capturar el rebote inminente, operando bajo una postura de paciencia táctica sin sobrepasar el capital disponible."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 82%): SOL-USD se encuentra en clara sobreventa técnica con un RSI de 30.8 y una caída acumulada en 7 días de -7.81%. Mantenemos la posición para capturar el rebote alcista esperado hacia la media, sin realizar nuevas compras para respetar el límite de liquidez de efectivo.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 06:10` | 🟢 BUY | `ETH-USD` | $2.00 | $2552.03 | ETH-USD presenta un RSI de 35.5 en clara zona de sobreventa tras caídas semanales del -5.3... |
| `2026-10-12 05:50` | 🟢 BUY | `ETH-USD` | $5.00 | $2553.65 | ETH-USD presenta un RSI de 35.7 en clara zona de sobreventa técnica tras una caída semanal... |
| `2026-10-12 05:50` | 🔴 SELL | `SOL-USD` | $5.00 | $111.85 | Liberamos una pequeña porción de SOL-USD para rescatar liquidez y financiar una entrada tá... |
| `2026-10-12 05:30` | 🔴 SELL | `ETH-USD` | $5.98 | $2553.85 | Rotación activa de capital. ETH se encuentra estancado y bajo su SMA20 con un PnL de -0.33... |
| `2026-10-12 05:20` | 🟢 BUY | `SOL-USD` | $4.00 | $111.70 | SOL-USD se encuentra en clara zona de sobreventa con un RSI de 32 y una caída semanal de -... |

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
