# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 20:40:38`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$9.23 USD** | **$29.88 USD** | **$39.11 USD** | 🔴 **-2.23%** ($-0.89) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 9h 49m |
| `SOL-USD` | 0.095785 | $104.40 | $104.23 | $9.98 | 📉 -0.16% | 4h 9m |
| `ETH-USD` | 0.004135 | $2418.34 | $2416.09 | $9.99 | 📉 -0.09% | 1h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado accionario tradicional (SPY, QQQ, NVDA, AAPL) se encuentra cerrado, por lo que la liquidez activa se concentra en las criptomonedas. En el sector cripto, BTC-USD, ETH-USD y SOL-USD se mantienen en tendencias bajistas de corto plazo bajo la SMA20, pero con indicadores de RSI de 1 hora en niveles de compresión o sobreventa (ETH-USD en 22.7, SOL-USD en 33.6). Nuestras posiciones actuales en cripto se mantienen estables con pérdidas mínimas y dentro del margen de tolerancia antes de un posible rebote de reversión a la media."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD muestra un RSI de 1h en 33.6 manteniéndose cerca de la zona de rebote técnico. La pérdida actual es marginal (-0.16%) y mantenemos la posición abierta para capturar el impulso alcista esperado en la reversión a la media.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas de AAPL, SOL-USD y ETH-USD mientras monitoreamos de cerca los gráficos de 1 hora. El efectivo disponible actual es de $9.23 USD. Establecer objetivos de Take-Profit en +2.5% para SOL-USD y ETH-USD, y estar preparados para cortar pérdidas si el RSI de 1h de cripto rompe nuevos mínimos o si las posiciones superan el límite de tolerancia del -2.0%. En cuanto abra el mercado tradicional, reevaluar AAPL."
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
