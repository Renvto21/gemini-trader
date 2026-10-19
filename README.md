# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 00:10:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.48 USD** | **$16.08 USD** | **$38.56 USD** | 🔴 **-3.59%** ($-1.44) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.003330 | $2402.76 | $2422.92 | $8.07 | 📈 +0.84% | 2h 49m |
| `SOL-USD` | 0.076111 | $105.11 | $105.31 | $8.02 | 📈 +0.19% | 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de Wall Street se encuentra cerrado por lo que el foco operativo se centra en el mercado cripto 24/7. ETH-USD y SOL-USD mantienen una ligera ganancia pero sin alcanzar el objetivo de take-profit del +2.0% requerido. El RSI de 1 hora de ambos activos se estabiliza alrededor de 52-58 sin sobrecompra crítica todavía, mientras que BTC-USD muestra un comportamiento lateral estable con sesgo positivo diario."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 70%): La posición en ETH-USD muestra una ganancia leve del +0.84% y un holding time de menos de 3 horas. El RSI de 1 hora está en 52.2, por lo que se mantiene abierta esperando alcanzar el rango objetivo de take-profit (+2.0% a +3.5%).
- **[HOLD] SOL-USD** (Confianza: 70%): La posición en SOL-USD registra un PnL positivo del +0.19% tras su reciente recompra. El RSI de 1 hora se sitúa en 58.3 y se mantiene la posición para capturar el rebote técnico hacia la zona de sobrecompra.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en ETH-USD y SOL-USD buscando alcanzar el take-profit entre +2.0 por ciento y +3.5 por ciento, o un RSI de 1 hora superior a 70. Mantener el stop-loss en -2.0 por ciento. La liquidez disponible es de $22.48 USD y se evaluará la apertura de una posición en BTC-USD si rompe los niveles actuales con mayor volumen y momentum."
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
