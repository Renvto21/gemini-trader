# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-14 13:50:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.31 USD** | **$19.96 USD** | **$39.26 USD** | 🔴 **-1.84%** ($-0.74) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $344.33 | $9.95 | 📉 -0.53% | 3h 0m |
| `SOL-USD` | 0.095511 | $104.70 | $104.79 | $10.01 | 📈 +0.09% | 1h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado se encuentra mayoritariamente con una tendencia bajista de corto plazo bajo sus SMA20, pero muestra señales tempranas de sobreventa profunda en varios activos, especialmente en criptomonedas como ETH-USD con un RSI de 1h en 24.3 y un cambio de 1h positivo. AAPL se mantiene relativamente estable con un RSI de 1h en 63.3 acercándose a la zona de toma de beneficios, mientras que SOL-USD muestra un leve impulso positivo con un RSI de 1h en 30.2."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 75%): AAPL muestra resiliencia con un RSI de 1h en 63.3 cerca de la zona de objetivo de salida. Se mantiene la posición para buscar la toma de beneficios si alcanza sobrecompra.
- **[HOLD] SOL-USD** (Confianza: 70%): SOL-USD presenta un cambio de 1h positivo de +1.0% y un RSI de 1h saliendo de la zona de sobreventa (30.2). Se retiene para permitir que el rebote técnico continúe.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener la posición en SOL-USD vigilando un incremento de su momentum alcista. Monitorear AAPL para asegurar beneficios si su RSI de 1h cruza el nivel de 70. Mantener liquidez disponible para evaluar una posible entrada táctica de rebote en ETH-USD si el cambio de 1h y el volumen confirman el giro alcista desde la sobreventa extrema."
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
