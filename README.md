# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 20:50:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.02 USD** | **$41.07 USD** | **$41.09 USD** | 🟢 **+2.73%** ($+1.09) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.296859 | $111.70 | $111.25 | $33.03 | 📉 -0.40% |
| `ETH-USD` | 0.003174 | $2520.20 | $2534.81 | $8.05 | 📈 +0.58% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra un sesgo alcista moderado en los principales índices como SPY y QQQ, mientras que el sector tecnológico presenta oportunidades selectivas. En criptomonedas, SOL-USD y ETH-USD muestran niveles extremos de sobreventa técnica (RSI de 26.1 y 33.3 respectivamente) tras caídas semanales, lo cual representa una clara oportunidad de rebote técnico por mean reversion. Dado que nuestro capital en efectivo es casi nulo (0.02 USD), es necesario retener nuestras posiciones actuales que están listas para rebotar y maximizar la exposición sin realizar ventas prematuras que interrumpan el momentum esperado."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 88%): SOL-USD se encuentra en una situación clásica de sobreventa extrema (RSI de 26.1) bajo la SMA20, lo que activa nuestra estrategia de cazar rebotes. Mantenemos la posición para capturar el movimiento alcista inminente hacia el objetivo del +3% al +5%.
- **[HOLD] ETH-USD** (Confianza: 82%): ETH-USD presenta un RSI de 33.3 con un rendimiento positivo diario del 1.23%, mostrando indicios iniciales de reversión alcista tras la caída semanal. Conservamos la posición para acompañar la recuperación del activo.

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
