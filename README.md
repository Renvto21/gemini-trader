# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 07:30:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$39.37 USD** | **$39.37 USD** | 🔴 **-1.58%** ($-0.63) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.295191 | $107.17 | $106.33 | $31.39 | 📉 -0.79% |
| `ETH-USD` | 0.003192 | $2506.03 | $2500.28 | $7.98 | 📉 -0.23% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado cripto muestra signos mixtos pero con fuerte sobreventa en Solana (SOL-USD con RSI en 25.2), lo cual representa una excelente oportunidad de rebote técnico (Mean Reversion) bajo nuestra estrategia agresiva. Ethereum (ETH-USD) también mantiene un RSI bajo en 35.0. No ejecutamos ventas ya que nuestras posiciones actuales no han alcanzado el take-profit y se mantienen estables buscando el rebote, optando por mantener el capital en juego en SOL."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 90%): SOL-USD se encuentra en condición de extrema sobreventa con un RSI de 25.2 y una caída semanal del 8.51%. Mantenemos la posición actual para cazar el rebote técnico agresivo hacia la zona de recuperación rápida.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 02:30` | 🟢 BUY | `SOL-USD` | $4.00 | $108.19 | SOL-USD presenta un RSI extremadamente bajo de 26.3, lo que indica sobreventa técnica seve... |
| `2026-10-13 01:30` | 🟢 BUY | `SOL-USD` | $6.23 | $107.75 | SOL-USD se encuentra en una zona de sobreventa extrema con un RSI de 25.8 tras una caída s... |
| `2026-10-13 01:10` | 🟢 BUY | `ETH-USD` | $8.00 | $2506.03 | ETH-USD se encuentra en clara sobreventa técnica con un RSI de 31.1 tras una caída semanal... |
| `2026-10-13 01:10` | 🔴 SELL | `SOL-USD` | $16.14 | $107.57 | Vendemos parcialmente SOL-USD para liberar liquidez y poder financiar la entrada en ETH-US... |
| `2026-10-13 01:00` | 🟢 BUY | `SOL-USD` | $12.00 | $107.31 | Aprovechamos la sobreventa extrema de SOL-USD (RSI 25.3 y caída semanal de -11.16%) para i... |

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
