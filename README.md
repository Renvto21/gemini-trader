# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 09:40:44`

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

> "El mercado de Wall Street se encuentra cerrado, por lo que toda la atención se centra exclusivamente en las criptomonedas (BTC-USD, SOL-USD, ETH-USD) que operan 24/7. Actualmente, ETH-USD presenta un RSI de 1 hora en 71.5 (sobrecompra) tras un rebote técnico, mientras que BTC y SOL muestran valores de RSI de 1 hora cercanos a 67-68 con un impulso positivo de corto plazo, pero sin la sobreventa extrema previa (<35) necesaria para ejecutar nuevas entradas seguras bajo nuestra estrategia de Mean Reversion. Con $38.57 USD en efectivo, mantenemos la paciencia táctica esperando un retroceso que nos permita cazar una nueva oportunidad de alto valor."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): No hay posiciones abiertas en este momento. El RSI de 1 hora de SOL-USD se encuentra en 67.4 y subiendo, lo que descarta una entrada por sobreventa (<35). Mantenemos la liquidez en efectivo esperando un retroceso táctico.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantenemos el 100% del capital ($38.57 USD) en efectivo debido a que los activos cripto disponibles se encuentran en zonas neutrales o de sobrecompra en el RSI de 1 hora (67-71). El plan táctico para los siguientes ciclos es esperar a que se produzca una corrección intradiaria que hunda el RSI de 1 hora por debajo de 35 en SOL-USD o BTC-USD para desplegar entre $6.00 y $8.00 USD en una jugada de rebote, buscando un take-profit rápido del 2.5% o salida si el RSI cruza 70."
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
