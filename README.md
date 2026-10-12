# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-12 05:30:47`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$6.00 USD** | **$35.46 USD** | **$41.46 USD** | 🟢 **+3.65%** ($+1.46) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.316736 | $111.79 | $111.94 | $35.46 | 📈 +0.13% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo alcista moderado en índices principales como QQQ y SPY, mientras que las criptomonedas muestran signos de consolidación tras fuertes caídas semanales. SOL-USD y ETH-USD se encuentran en zonas de sobreventa técnica (RSI de 32.8 y 35.7 respectivamente), lo que activa nuestra estrategia de Mean Reversion para buscar rebotes rápidos. Dado que la liquidez en efectivo es casi nula y tenemos posiciones estancadas en SOL y ETH con ganancias y pérdidas mínimas, mantenemos la posición en SOL para aprovechar el rebote y rotamos fuera de ETH para reasignar capital hacia una oportunidad con mejor momento en el sector tecnológico o mantener una postura equilibrada."*

**Operaciones del ciclo:**
- **[SELL] ETH-USD** (Confianza: 82%): Rotación activa de capital. ETH se encuentra estancado y bajo su SMA20 con un PnL de -0.33%. Vendemos la totalidad de la posición para liberar liquidez y financiar oportunidades de mayor impulso en el mercado.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-12 05:30` | 🔴 SELL | `ETH-USD` | $5.98 | $2553.85 | Rotación activa de capital. ETH se encuentra estancado y bajo su SMA20 con un PnL de -0.33... |
| `2026-10-12 05:20` | 🟢 BUY | `SOL-USD` | $4.00 | $111.70 | SOL-USD se encuentra en clara zona de sobreventa con un RSI de 32 y una caída semanal de -... |
| `2026-10-12 04:50` | 🟢 BUY | `ETH-USD` | $6.00 | $2562.29 | ETH-USD presenta condiciones ideales de sobreventa con un RSI de 36.9 y un descuento del 5... |
| `2026-10-12 04:30` | 🔴 SELL | `ETH-USD` | $10.02 | $2567.68 | Rotación activa de capital. ETH muestra una ganancia marginal del 0.23% sin momentum fuert... |
| `2026-10-12 03:40` | 🟢 BUY | `SOL-USD` | $4.00 | $112.34 | SOL-USD se encuentra en clara sobreventa técnica con un RSI de 29.5 y una caída semanal de... |

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
