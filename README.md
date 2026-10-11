# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 20:00:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.02 USD** | **$40.98 USD** | **$41.00 USD** | 🟢 **+2.49%** ($+1.00) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.296859 | $111.70 | $110.96 | $32.94 | 📉 -0.66% |
| `ETH-USD` | 0.003174 | $2520.20 | $2531.39 | $8.04 | 📈 +0.44% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sentimiento mixto con sesgo alcista en indices tech y moderacion en criptomonedas. SOL-USD presenta un RSI extremadamente sobrevendido de 25.1, ideal para aplicar la estrategia de rebote por reversion a la media (mean reversion). ETH-USD se mantiene estable sin alcanzar aun la toma de beneficios del +2.5% ni activar el stop loss, por lo que se mantiene en cartera a la espera de mayor impulso alcista."*

**Operaciones del ciclo:**
- **[BUY] SOL-USD** (Confianza: 90%): SOL-USD se encuentra en una clara condicion de sobreventa tecnica profunda con un RSI de 25.1 tras una caida semanal del -8.11%. Cumple perfectamente con la regla de cazar rebotes en cripto de alta volatilidad para capturar un movimiento rapido al alza utilizando la liquidez disponible.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 20:00` | 🟢 BUY | `SOL-USD` | $4.00 | $110.96 | SOL-USD se encuentra en una clara condicion de sobreventa tecnica profunda con un RSI de 2... |
| `2026-10-11 18:20` | 🟢 BUY | `ETH-USD` | $8.00 | $2520.20 | ETH-USD presenta un RSI de 31.1 y una caída acumulada del 7.04% en los últimos 7 días, sit... |
| `2026-10-11 17:50` | 🔴 SELL | `ETH-USD` | $12.02 | $2536.22 | ETH-USD se encuentra estancado con una ganancia mínima de +0.19% y bajo una tendencia baji... |
| `2026-10-11 17:40` | 🟢 BUY | `SOL-USD` | $4.00 | $111.14 | SOL-USD se encuentra en una clara condición de sobreventa técnica con un RSI de 25.7 y una... |
| `2026-10-11 14:10` | 🟢 BUY | `SOL-USD` | $5.16 | $111.90 | SOL-USD presenta un RSI de 28.2 indicando sobreventa clara tras una caída semanal del 7.33... |

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
