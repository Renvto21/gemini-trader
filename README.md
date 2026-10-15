# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 21:00:57`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$9.23 USD** | **$29.85 USD** | **$39.07 USD** | 🔴 **-2.31%** ($-0.93) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $341.27 | $9.86 | 📉 -1.41% | 10h 10m |
| `SOL-USD` | 0.095785 | $104.40 | $104.22 | $9.98 | 📉 -0.17% | 4h 30m |
| `ETH-USD` | 0.004135 | $2418.34 | $2419.74 | $10.01 | 📈 +0.06% | 2h 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que la liquidez activa se concentra exclusivamente en las criptomonedas (24/7). ETH-USD se mantiene estable con un leve repunte tras su sobreventa, mientras que SOL-USD muestra cierta indecisión con un cambio de 1h negativo menor. BTC-USD presenta un RSI de 1h en sobreventa extrema (27.7), lo que representa una potencial oportunidad de rebote técnico a corto plazo."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra un rendimiento positivo marginal y se mantiene dentro de los parámetros esperados para buscar el rebote técnico hacia el take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones abiertas de ETH-USD y SOL-USD vigilando de cerca sus objetivos de take-profit entre +2.0% y +3.5%. Evaluaremos la entrada en BTC-USD si su RSI de 1h se estabiliza y comienza a mostrar un cambio positivo. El stop-loss se mantiene estrictamente en -2.0% para todas las posiciones activas."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **52** | 🎯 **42.3%** (22W / 16L / 14BE) | 🔴 **$-0.67 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-14 19:00` | 🟢 BUY | `ETH-USD` | $10.00 | $2418.34 | ETH-USD presenta un RSI de 1h en 22.0 (sobreventa extrema) y un cambio de 1h que comienza ... |
| `2026-10-14 16:30` | 🟢 BUY | `SOL-USD` | $10.00 | $104.40 | SOL-USD presenta un RSI de 1h en 30.9 saliendo de la zona de compresión y un cambio positi... |
| `2026-10-14 15:20` | 🔴 SELL (-0.08$) | `SOL-USD` | $9.92 | $103.86 | SOL-USD lleva varias horas sin mostrar el rebote esperado, su RSI de 1h ha caído hasta 25.... |
| `2026-10-14 12:30` | 🟢 BUY | `SOL-USD` | $10.00 | $104.70 | SOL-USD presenta un RSI de 1h en 29.2 saliendo de sobreventa extrema y un cambio de 1h pos... |
| `2026-10-14 11:20` | 🔴 SELL (-0.09$) | `BTC-USD` | $5.89 | $81874.95 | BTC-USD lleva más de 14 horas abierto con un PnL negativo persistente (-1.51%) y un RSI de... |

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
