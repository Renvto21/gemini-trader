# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 14:00:47`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.31 USD** | **$19.97 USD** | **$39.28 USD** | 🔴 **-1.81%** ($-0.72) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $344.20 | $9.94 | 📉 -0.56% | 3h 10m |
| `SOL-USD` | 0.095511 | $104.70 | $104.96 | $10.02 | 📈 +0.25% | 1h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado se encuentra mayoritariamente bajo tendencia bajista en el corto plazo con varios activos probando soportes clave, aunque se observan oportunidades interesantes de rebote por sobreventa extrema en índices y criptomonedas. Los activos tecnológicos e intradiarios muestran leves intentos de estabilización."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 75%): AAPL mantiene una tendencia alcista saludable sobre la SMA20 con un RSI de 1h en 62.9, cerca de la zona de objetivo para asegurar beneficios. Mantenemos la posición actual mientras consolidamos las ganancias latentes.
- **[HOLD] SOL-USD** (Confianza: 70%): SOL-USD muestra signos incipientes de recuperación con un cambio de 1h positivo (+0.1%) tras salir de sobreventa extrema. Esperamos a que el momentum alcista se consolide para buscar un take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener la posición de SOL-USD vigilando un incremento de su momentum alcista y proteger AAPL ante cualquier cambio de tendencia. Monitorear el RSI de AAPL para asegurar beneficios si se acerca nuevamente a 70. Mantener liquidez disponible para evaluar posibles entradas en activos que confirmen giro alcista desde la sobreventa."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **51** | 🎯 **43.1%** (22W / 15L / 14BE) | 🔴 **$-0.59 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-14 12:30` | 🟢 BUY | `SOL-USD` | $10.00 | $104.70 | SOL-USD presenta un RSI de 1h en 29.2 saliendo de sobreventa extrema y un cambio de 1h pos... |
| `2026-10-14 11:20` | 🔴 SELL (-0.09$) | `BTC-USD` | $5.89 | $81874.95 | BTC-USD lleva más de 14 horas abierto con un PnL negativo persistente (-1.51%) y un RSI de... |
| `2026-10-14 10:50` | 🟢 BUY | `AAPL` | $10.00 | $346.15 | AAPL se encuentra con un excelente momentum alcista intradiario, un incremento de 1.4% en ... |
| `2026-10-14 10:10` | 🔴 SELL (-0.11$) | `SOL-USD` | $5.89 | $105.41 | La posición en SOL-USD acumula una pérdida cercana al -1.9%, rozando nuestro stop-loss est... |
| `2026-10-14 02:50` | 🔴 SELL (-0.01$) | `ETH-USD` | $4.99 | $2502.14 | ETH-USD lleva más de 9 horas de holding con PnL plano (-0.25%) y un RSI de 1H en 42.3 sin ... |

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
