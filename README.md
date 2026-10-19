# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 23:00:47`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.31 USD** | **$16.20 USD** | **$38.51 USD** | 🔴 **-3.72%** ($-1.49) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.077662 | $103.01 | $104.80 | $8.14 | 📈 +1.74% | 3h 30m |
| `ETH-USD` | 0.003330 | $2402.76 | $2421.51 | $8.06 | 📈 +0.78% | 1h 40m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado por fin de semana, por lo que toda la actividad se concentra exclusivamente en el mercado de criptomonedas (24/7). SOL-USD muestra un rendimiento positivo con una ganancia actual de +1.74%, acercándose al rango objetivo de take-profit. ETH-USD registra un +0.78% y mantiene una estructura de rebote técnico favorable desde niveles diarios sobrevendidos. Bitcoin (BTC-USD) muestra estabilidad y un ligero impulso alcista en las últimas 24 horas."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD acumula una ganancia del +1.74%, muy cerca de la banda objetivo de take-profit (+2.0% a +3.5%). Mantiene un RSI de 1h saludable en 55.9, por lo que se mantiene la posición para asegurar el objetivo en el próximo ciclo.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD presenta una ganancia actual del +0.78% con un holding time de 1h 40m. El RSI diario se mantiene bajo, sugiriendo potencial alcista adicional en el rebote técnico hacia la zona de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en SOL-USD y ETH-USD mientras continúan su camino hacia la zona de take-profit (+2.0% a +3.5%). Monitorear de cerca SOL-USD ya que se encuentra muy cerca del objetivo de ganancia para ejecutar venta parcial o total y asegurar capital. Si el RSI de 1h se eleva a sobrecompra (>70), realizar la venta inmediatamente para liberar liquidez."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **74** | 🎯 **41.9%** (31W / 29L / 14BE) | 🔴 **$-1.55 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-18 21:20` | 🟢 BUY | `ETH-USD` | $8.00 | $2402.76 | ETH-USD muestra un RSI diario fuertemente sobrevendido en 23.2 y un cambio positivo en la ... |
| `2026-10-18 21:00` | 🔴 SELL (+0.16$) | `ETH-USD` | $8.16 | $2409.06 | ETH-USD ha alcanzado una ganancia del +2.03%, cumpliendo con la regla de toma rápida de ga... |
| `2026-10-18 19:30` | 🟢 BUY | `SOL-USD` | $8.00 | $103.01 | SOL-USD presenta un RSI diario extremadamente bajo (16.5) y un RSI de 1h recuperándose has... |
| `2026-10-18 19:10` | 🔴 SELL (+0.17$) | `SOL-USD` | $8.17 | $102.92 | SOL-USD ha alcanzado un rendimiento de +2.07% cumpliendo con nuestra regla de toma rápida ... |
| `2026-10-18 18:40` | 🟢 BUY | `ETH-USD` | $8.00 | $2361.22 | ETH-USD muestra un RSI diario deprimido en 21.5 y un RSI de 1 hora que se recupera a 34.3 ... |

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
