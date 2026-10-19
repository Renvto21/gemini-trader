# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 01:20:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$30.48 USD** | **$8.06 USD** | **$38.53 USD** | 🔴 **-3.67%** ($-1.47) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.003330 | $2402.76 | $2419.35 | $8.06 | 📈 +0.69% | 4h 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de valores tradicional se encuentra completamente cerrado durante el fin de semana, por lo que toda la actividad se concentra exclusivamente en las criptomonedas (24/7). Observamos que los principales activos digitales como BTC-USD y SOL-USD muestran condiciones de sobrecompra en el marco temporal de 1 hora (RSI superior a 70), lo que sugiere un posible agotamiento del impulso alcista a muy corto plazo y una oportunidad inminente de toma de beneficios o corrección técnica. ETH-USD se mantiene en cartera con una ganancia moderada del +0.69% y un RSI de 1 hora en 65.7, acercándose a la zona objetivo para asegurar ganancias."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra un rendimiento positivo del +0.69% con un RSI de 1 hora en 65.7. Aunque nos acercamos a la zona objetivo de take-profit (+2.0% a +3.5%), aún no ha alcanzado el umbral crítico de sobrecompra (>70). Mantenemos la posición activa para maximizar el rebote técnico antes de asegurar ganancias.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos ETH-USD abierta pero monitorearemos de cerca su RSI de 1 hora. Si cruza los 70 puntos o alcanza el rango objetivo de ganancia del +2.0% al +3.5%, procederemos a vender inmediatamente para asegurar efectivo. Al tener activos tradicionales cerrados, la liquidez se mantendrá protegida y buscaremos reentrar en SOL-USD o BTC-USD una vez que sufran un retroceso técnico saludable que alivie sus indicadores de corto plazo."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **76** | 🎯 **42.1%** (32W / 29L / 15BE) | 🔴 **$-1.38 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-19 01:00` | 🔴 SELL (-0.00$) | `SOL-USD` | $8.00 | $105.08 | SOL-USD ha entrado en sobrecompra con un RSI de 1 hora en 72.7, cumpliendo estrictamente c... |
| `2026-10-18 23:20` | 🟢 BUY | `SOL-USD` | $8.00 | $105.11 | SOL-USD presenta un RSI diario en 21.8 (sobreventa extrema) y un momentum de 24 horas alci... |
| `2026-10-18 23:10` | 🔴 SELL (+0.17$) | `SOL-USD` | $8.17 | $105.19 | SOL-USD acumula una ganancia del +2.12%, cumpliendo con la regla de toma rápida de gananci... |
| `2026-10-18 21:20` | 🟢 BUY | `ETH-USD` | $8.00 | $2402.76 | ETH-USD muestra un RSI diario fuertemente sobrevendido en 23.2 y un cambio positivo en la ... |
| `2026-10-18 21:00` | 🔴 SELL (+0.16$) | `ETH-USD` | $8.16 | $2409.06 | ETH-USD ha alcanzado una ganancia del +2.03%, cumpliendo con la regla de toma rápida de ga... |

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
