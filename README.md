# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 14:10:51`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.57 USD** | **$20.02 USD** | **$38.59 USD** | 🔴 **-3.53%** ($-1.41) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $719.43 | $10.01 | 📈 +0.07% | 3h 30m |
| `ETH-USD` | 0.004178 | $2393.62 | $2397.30 | $10.02 | 📈 +0.15% | 1h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado se encuentra en una fase de consolidación de corto plazo con sesgo bajista en el marco diario para la mayoría de los activos, mientras que el sentimiento intradía muestra pausas tras los recientes intentos de rebote técnico. Los índices y criptomonedas operan con ligeras variaciones negativas en la última hora, manteniendo la cautela y exigiendo un monitoreo estricto de los soportes."

**Operaciones del ciclo:**
- **[HOLD] QQQ** (Confianza: 60%): La posición muestra un rendimiento estable cercano al 0.07% con un holding time moderado. Se mantiene a la espera de un mayor impulso alcista para buscar el take-profit o proteger el capital si cede el soporte.
- **[HOLD] ETH-USD** (Confianza: 60%): ETH-USD se mantiene con una ganancia marginal del 0.15%. El RSI de 1 hora se sitúa en 37.9, por lo que conservamos la posición buscando un rebote adicional hacia la zona de sobrecompra para tomar beneficios.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales de QQQ y ETH-USD ya que se encuentran dentro del rango de tolerancia y sin romper los stop-loss de -2.0%. Estaremos vigilando el RSI de 1 hora para asegurar ganancias si alcanzan la zona de +2.0% a +3.5%, o recortar de inmediato si la tendencia se deteriora. Preservaremos la liquidez actual de $18.57 USD esperando una ruptura clara de momentum para desplegar nuevas entradas."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **77** | 🎯 **42.9%** (33W / 29L / 15BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-19 12:51` | 🟢 BUY | `ETH-USD` | $10.00 | $2393.62 | ETH-USD presenta un RSI de 1 hora en 34.6, entrando en zona de sobreventa de corto plazo, ... |
| `2026-10-19 10:40` | 🟢 BUY | `QQQ` | $10.00 | $718.92 | QQQ muestra un fuerte momentum intradiario con un cambio de 1h del +1.28%, liderando el re... |
| `2026-10-19 01:50` | 🔴 SELL (+0.09$) | `ETH-USD` | $8.09 | $2428.97 | ETH-USD registra una ganancia acumulada y su RSI de 1 hora ha alcanzado 68.3, acercándose ... |
| `2026-10-19 01:00` | 🔴 SELL (-0.00$) | `SOL-USD` | $8.00 | $105.08 | SOL-USD ha entrado en sobrecompra con un RSI de 1 hora en 72.7, cumpliendo estrictamente c... |
| `2026-10-18 23:20` | 🟢 BUY | `SOL-USD` | $8.00 | $105.11 | SOL-USD presenta un RSI diario en 21.8 (sobreventa extrema) y un momentum de 24 horas alci... |

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
