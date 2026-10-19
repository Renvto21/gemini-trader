# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 00:20:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.48 USD** | **$16.07 USD** | **$38.55 USD** | 🔴 **-3.62%** ($-1.45) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.003330 | $2402.76 | $2422.46 | $8.07 | 📈 +0.82% | 2h 59m |
| `SOL-USD` | 0.076111 | $105.11 | $105.17 | $8.00 | 📈 +0.06% | 1h 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se encuentra abierto con un sentimiento moderadamente alcista en los rebotes de corto plazo, destacando que los activos tradicionales (Wall Street) permanecen cerrados. Las posiciones actuales en ETH-USD y SOL-USD muestran ligeras ganancias pero se mantienen por debajo del objetivo del +2.0 por ciento, con un RSI de 1 hora acercándose a zonas de atención cercanas a la sobrecompra sin haber cruzado aún el umbral de 70."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD mantiene una ganancia actual de +0.82 por ciento tras casi tres horas de mantener la posición. El RSI de 1 hora está en 59.2, acercándose al objetivo de sobrecompra (>70) sin activar señales de salida o stop-loss. Se mantiene para buscar el take-profit.
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD se encuentra estable con una pequeña ganancia del +0.06 por ciento y un RSI de 1 hora en 65.9. El momentum alcista se mantiene intacto dentro del rango esperado, por lo que se conserva la posición buscando alcanzar el objetivo de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en ETH-USD y SOL-USD vigilando de cerca el take-profit entre +2.0 por ciento y +3.5 por ciento o un RSI de 1 hora superior a 70. Mantener estricto el stop-loss en -2.0 por ciento. La liquidez actual de 22.48 USD se mantendrá a la espera de una mayor confirmación de volumen en BTC-USD o de la apertura de los mercados tradicionales para buscar rotaciones tácticas."
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
