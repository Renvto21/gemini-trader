# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 05:50:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$6.00 USD** | **$35.43 USD** | **$41.43 USD** | 🟢 **+3.58%** ($+1.43) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.272036 | $111.79 | $111.85 | $30.43 | 📈 +0.05% |
| `ETH-USD` | 0.001958 | $2553.65 | $2553.65 | $5.00 | 📈 +0.00% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo mixto con soporte general en los índices principales (QQQ, SPY alcistas), mientras que las criptomonedas y algunos activos tecnológicos experimentan correcciones temporales. Destaca ETH-USD con un RSI de 35.7 en zona de sobreventa técnica, ideal para una jugada de rebote agresivo por mean reversion. SOL-USD se mantiene lateral en cartera sin momentum fuerte, por lo que rotaremos parte de su capital para capturar la oportunidad en ETH."*

**Operaciones del ciclo:**
- **[SELL] SOL-USD** (Confianza: 85%): Liberamos una pequeña porción de SOL-USD para rescatar liquidez y financiar una entrada táctica en ETH-USD, aprovechando la rotación dinámica de capital en cripto.
- **[BUY] ETH-USD** (Confianza: 88%): ETH-USD presenta un RSI de 35.7 en clara zona de sobreventa técnica tras una caída semanal del -5.33%. Activamos una compra de alto impulso buscando un rebote rápido del 3% al 5%.

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
