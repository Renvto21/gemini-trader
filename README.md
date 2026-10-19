# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 08:50:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$38.57 USD** | **$0.00 USD** | **$38.57 USD** | 🔴 **-3.59%** ($-1.43) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| *(Ninguna posición abierta - 100% en efectivo)* | - | - | - | - | - | - |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado accionario tradicional (SPY, QQQ, NVDA, MSFT, AAPL, GLD) se encuentra CERRADO. Nos enfocamos estrictamente en el mercado de criptomonedas (ABIERTO 24/7). Actualmente, los activos principales (ETH-USD, BTC-USD y SOL-USD) presentan un RSI de 1 hora en zona de sobrecompra superior a 70 (77.2 para ETH, 70.5 para BTC y 74.9 para SOL), lo que incumple nuestra regla de entrada por rebote técnico. Mantenemos el 100% de la cartera en efectivo ($38.57 USD) esperando una corrección intradiaria que sitúe el rsi_1h por debajo de 35."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 90%): El activo tiene el mercado abierto, pero su rsi_1h se encuentra en sobrecompra extrema (74.9), lo que imposibilita una entrada por rebote según nuestra estrategia de gestión de riesgo. Esperaremos una corrección intradiaria.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantenemos $38.57 USD en efectivo tras el ciclo anterior. El plan táctico para los siguientes ciclos consiste en vigilar de cerca a SOL-USD, ETH-USD y BTC-USD a la espera de un retroceso en el rsi_1h por debajo de 35 combinado con un cambio de momentum intradiario positivo para desplegar entre $8.00 y $10.00 USD en una entrada de alta convicción. No compramos con indicadores en sobrecompra."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **77** | 🎯 **42.9%** (33W / 29L / 15BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-19 01:50` | 🔴 SELL (+0.09$) | `ETH-USD` | $8.09 | $2428.97 | ETH-USD registra una ganancia acumulada y su RSI de 1 hora ha alcanzado 68.3, acercándose ... |
| `2026-10-19 01:00` | 🔴 SELL (-0.00$) | `SOL-USD` | $8.00 | $105.08 | SOL-USD ha entrado en sobrecompra con un RSI de 1 hora en 72.7, cumpliendo estrictamente c... |
| `2026-10-18 23:20` | 🟢 BUY | `SOL-USD` | $8.00 | $105.11 | SOL-USD presenta un RSI diario en 21.8 (sobreventa extrema) y un momentum de 24 horas alci... |
| `2026-10-18 23:10` | 🔴 SELL (+0.17$) | `SOL-USD` | $8.17 | $105.19 | SOL-USD acumula una ganancia del +2.12%, cumpliendo con la regla de toma rápida de gananci... |
| `2026-10-18 21:20` | 🟢 BUY | `ETH-USD` | $8.00 | $2402.76 | ETH-USD muestra un RSI diario fuertemente sobrevendido en 23.2 y un cambio positivo en la ... |

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
