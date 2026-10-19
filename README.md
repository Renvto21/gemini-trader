# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 23:10:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$30.48 USD** | **$8.08 USD** | **$38.56 USD** | 🔴 **-3.60%** ($-1.44) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.003330 | $2402.76 | $2426.49 | $8.08 | 📈 +0.99% | 1h 49m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene abierto y operando en un sesgo alcista de corto plazo dentro de una tendencia macro bajista. SOL-USD muestra un rendimiento positivo con una ganancia del +2.12%, alcanzando el objetivo táctico de toma de ganancias. ETH-USD muestra un rendimiento del +0.99%. Los mercados tradicionales permanecen cerrados, por lo que toda la atención táctica se centra en la rotación y el aseguramiento de beneficios en criptomonedas."

**Operaciones del ciclo:**
- **[SELL] SOL-USD** (Confianza: 90%): SOL-USD acumula una ganancia del +2.12%, cumpliendo con la regla de toma rápida de ganancias (+2.0% a +3.5%). Se procede a vender la totalidad de la posición para asegurar el capital en efectivo y rotarlo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "SOL-USD ha alcanzado el objetivo de ganancia (+2.12%); procederé a vender el total de la posición para asegurar beneficios y liberar liquidez. Mantendré ETH-USD buscando que alcance el rango objetivo de +2.0% a +3.5% o que su RSI de 1h se acerque a la zona de sobrecompra para realizar la toma de ganancias. Vigilar posibles puntos de entrada en BTC-USD si se presenta una confirmación de rebote."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **75** | 🎯 **42.7%** (32W / 29L / 14BE) | 🔴 **$-1.38 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-18 23:10` | 🔴 SELL (+0.17$) | `SOL-USD` | $8.17 | $105.19 | SOL-USD acumula una ganancia del +2.12%, cumpliendo con la regla de toma rápida de gananci... |
| `2026-10-18 21:20` | 🟢 BUY | `ETH-USD` | $8.00 | $2402.76 | ETH-USD muestra un RSI diario fuertemente sobrevendido en 23.2 y un cambio positivo en la ... |
| `2026-10-18 21:00` | 🔴 SELL (+0.16$) | `ETH-USD` | $8.16 | $2409.06 | ETH-USD ha alcanzado una ganancia del +2.03%, cumpliendo con la regla de toma rápida de ga... |
| `2026-10-18 19:30` | 🟢 BUY | `SOL-USD` | $8.00 | $103.01 | SOL-USD presenta un RSI diario extremadamente bajo (16.5) y un RSI de 1h recuperándose has... |
| `2026-10-18 19:10` | 🔴 SELL (+0.17$) | `SOL-USD` | $8.17 | $102.92 | SOL-USD ha alcanzado un rendimiento de +2.07% cumpliendo con nuestra regla de toma rápida ... |

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
