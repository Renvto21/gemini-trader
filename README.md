# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 08:10:35`

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

> "El mercado tradicional (Wall Street) se encuentra cerrado, por lo que toda la atención y liquidez operativa debe concentrarse exclusivamente en el mercado de criptomonedas (abierto 24/7). Observamos que los principales activos digitales como SOL-USD y ETH-USD se encuentran en zonas de sobrecompra en el muy corto plazo (RSI de 1 hora en 75.2 y 77.5 respectivamente), a pesar de mantener un RSI diario en niveles de sobreventa profunda (21.1 y 25.7). No existen condiciones óptimas para una entrada inmediata en este ciclo, ya que buscamos retrocesos intradiarios que lleven el RSI de 1 hora por debajo de 35 antes de desplegar nuestro capital."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 50%): El RSI de 1 hora de SOL-USD se encuentra elevado en 75.2 (sobrecompra local), lo que descarta una compra en este momento. Esperamos un retroceso intradiario hacia soportes de corto plazo para buscar una entrada de alta convicción.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantenemos nuestros $38.57 USD en liquidez tras haber ejecutado con éxito las tomas de ganancias previas. El plan táctico para los siguientes ciclos consiste en vigilar de cerca a SOL-USD y ETH-USD para esperar una corrección intradiaria que hunda su RSI de 1 hora por debajo de 35. Cuando se produzca este retroceso, asignaremos entre $8.00 y $10.00 USD para capturar un rebote técnico rápido, estableciendo un take-profit estricto entre +2.5% y +3.5% o salida por sobrecompra."
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
