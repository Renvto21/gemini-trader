# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 03:00:46`

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

> "El mercado de Wall Street se encuentra cerrado, por lo que toda la atención se centra exclusivamente en las criptomonedas (24/7). Observamos que SOL-USD, BTC-USD y ETH-USD han tenido un fuerte impulso alcista en las últimas 24 horas y sus indicadores de RSI de 1 hora se encuentran en zona de sobrecompra clara (SOL-USD en 76.1, BTC-USD en 80.7 y ETH-USD en 74.5). No hay puntos de entrada atractivos para compra en este momento ya que los precios están extendidos a corto plazo, y no tenemos posiciones abiertas que gestionar."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): El activo muestra un RSI de 1 hora en 76.1 (sobrecompra). Aunque su RSI diario está en sobreventa (23.1), el momento actual a corto plazo es de extensión alcista y no ofrece un punto de entrada óptimo para un rebote inmediato. Mantenemos liquidez a la espera de un retroceso.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantenemos el efectivo de $38.57 USD intacto. El mercado cripto está sobrecomprado a corto plazo (RSI 1H > 70 en los principales activos). Esperaremos pacientemente a que se produzca una corrección intradiaria o un enfriamiento que devuelva el RSI de 1 hora de SOL-USD o ETH-USD por debajo de 35. En cuanto se presente esa oportunidad de mean reversion, desplegaremos entre $8.00 y $10.00 USD buscando un rebote rápido con objetivo de take-profit del +2.5%."
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
