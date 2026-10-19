# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 02:10:43`

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

> "El mercado accionario tradicional (MSFT, NVDA, AAPL, SPY, QQQ, GLD) se encuentra cerrado, por lo que toda la liquidez activa debe centrarse en los activos cripto disponibles 24/7 (SOL-USD, BTC-USD, ETH-USD). Actualmente, tanto SOL-USD (RSI 1H en 72.1) como BTC-USD (RSI 1H en 74.9) y ETH-USD (RSI 1H en 66.0) mantienen un sesgo alcista de corto plazo pero se encuentran en zonas de sobrecompra o acercándose a ellas, manteniendo la disciplina de esperar correcciones profundas intradiarias para activar compras por reversión a la media."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 50%): El activo se encuentra en sobrecompra intradiaria con un RSI de 1 hora en 72.1. Esperamos pacientemente a que el RSI caiga por debajo de 35 para ejecutar una compra de alto impulso.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantenemos $38.57 USD en efectivo tras haber asegurado ganancias previas. Los activos cripto siguen con RSI de 1 hora elevados (>65), por lo que aún no se activan las condiciones óptimas de entrada en sobreventa (<35). Mantendremos la paciencia táctica y esperaremos un retroceso claro en SOL-USD o BTC-USD para desplegar de $8.00 a $10.00 USD buscando un nuevo rebote técnico agresivo."
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
