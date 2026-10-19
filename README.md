# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 00:40:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.48 USD** | **$16.07 USD** | **$38.55 USD** | 🔴 **-3.63%** ($-1.45) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.003330 | $2402.76 | $2421.00 | $8.06 | 📈 +0.76% | 3h 19m |
| `SOL-USD` | 0.076111 | $105.11 | $105.20 | $8.01 | 📈 +0.09% | 1h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que la liquidez y operativa se concentran exclusivamente en el mercado cripto (24/7). ETH-USD y SOL-USD se mantienen dentro de la cartera mostrando estabilidad pero sin alcanzar aún la zona objetivo de take-profit (+2.0% a +3.5%) o sobrecompra en 1h (RSI > 70). Los indicadores de 1 hora muestran que los activos cripto mantienen un tono neutral a alcista moderado, con BTC consolidando sobre los 82k."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 70%): La posición mantiene un rendimiento positivo de +0.76% con un holding time moderado. Esperando que el precio continúe su impulso hacia el objetivo de take-profit del +2.0% o un RSI de 1h superior a 70.
- **[HOLD] SOL-USD** (Confianza: 70%): La posición se encuentra estable con una ganancia marginal de +0.09%. Se mantiene activa buscando el rebote técnico desde la sobreventa diaria extrema, respetando el stop-loss estricto.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener posiciones abiertas en ETH-USD y SOL-USD vigilando de cerca el take-profit entre +2.0% y +3.5% o si el RSI de 1 hora supera los 70 puntos. El stop-loss se mantiene estricto en -2.0%. La liquidez actual de 22.48 USD se mantendrá reservada hasta detectar un rompimiento de volumen en BTC-USD o una confirmación de rebote más clara."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **75** | 🎯 **42.7%** (32W / 29L / 14BE) | 🔴 **$-1.38 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-18 23:20` | 🟢 BUY | `SOL-USD` | $8.00 | $105.11 | SOL-USD presenta un RSI diario en 21.8 (sobreventa extrema) y un momentum de 24 horas alci... |
| `2026-10-18 23:10` | 🔴 SELL (+0.17$) | `SOL-USD` | $8.17 | $105.19 | SOL-USD acumula una ganancia del +2.12%, cumpliendo con la regla de toma rápida de gananci... |
| `2026-10-18 21:20` | 🟢 BUY | `ETH-USD` | $8.00 | $2402.76 | ETH-USD muestra un RSI diario fuertemente sobrevendido en 23.2 y un cambio positivo en la ... |
| `2026-10-18 21:00` | 🔴 SELL (+0.16$) | `ETH-USD` | $8.16 | $2409.06 | ETH-USD ha alcanzado una ganancia del +2.03%, cumpliendo con la regla de toma rápida de ga... |
| `2026-10-18 19:30` | 🟢 BUY | `SOL-USD` | $8.00 | $103.01 | SOL-USD presenta un RSI diario extremadamente bajo (16.5) y un RSI de 1h recuperándose has... |

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
