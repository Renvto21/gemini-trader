# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 23:20:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.48 USD** | **$16.06 USD** | **$38.54 USD** | 🔴 **-3.65%** ($-1.46) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.003330 | $2402.76 | $2420.21 | $8.06 | 📈 +0.73% | 1h 59m |
| `SOL-USD` | 0.076111 | $105.11 | $105.11 | $8.00 | 📈 +0.00% | 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "Los mercados tradicionales se encuentran cerrados, por lo que la liquidez activa se concentra en el mercado cripto (24/7). ETH-USD muestra una ganancia moderada del +0.73% tras un holding de casi 2 horas, manteniéndose por debajo del objetivo de toma de ganancias (+2.0% a +3.5%). SOL-USD presenta un RSI diario profundamente sobrevendido (21.8) y un cambio positivo en 24 horas del +1.74%, configurando una excelente oportunidad de rebote técnico (Mean Reversion)."

**Operaciones del ciclo:**
- **[BUY] SOL-USD** (Confianza: 88%): SOL-USD presenta un RSI diario en 21.8 (sobreventa extrema) y un momentum de 24 horas alcista del +1.74%. Cumple con los criterios tácticos de rebote técnico (Mean Reversion) con alta convicción, destinando $8.00 USD para capturar el impulso de corto plazo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendré ETH-USD a la espera de que alcance el rango objetivo de +2.0% a +3.5% o que su RSI de 1h entre en zona de sobrecompra (>70) para asegurar beneficios. He abierto una posición en SOL-USD aprovechando su sobreventa diaria extrema; mi objetivo de salida para SOL es una ganancia del +2.5% y mi stop-loss se activará si registra una caída superior al -2.0%."
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
