# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 15:50:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.57 USD** | **$20.04 USD** | **$38.60 USD** | 🔴 **-3.49%** ($-1.40) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $719.50 | $10.01 | 📈 +0.08% | 5h 10m |
| `ETH-USD` | 0.004178 | $2393.62 | $2400.54 | $10.03 | 📈 +0.29% | 2h 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sentimiento mixto con sesgo bajista general en temporalidades diarias, ya que la mayoría de los activos operan por debajo de sus SMA20. Sin embargo, en el corto plazo (1 hora), se observan condiciones interesantes de sobreventa extrema en criptomonedas como BTC-USD y SOL-USD, abriendo ventanas tácticas para la caza de rebotes (mean reversion). Las posiciones actuales en cartera (QQQ y ETH-USD) se mantienen estables pero sin la aceleración esperada, acumulando ganancias mínimas que no alcanzan el objetivo de take-profit."

**Operaciones del ciclo:**
- **[HOLD] QQQ** (Confianza: 60%): La posición se mantiene estable con una pequeña ganancia del +0.08% tras 5 horas abierta. No ha alcanzado el objetivo de take-profit ni ha activado el stop-loss, por lo que se mantiene en seguimiento para rotación si surge un momentum más fuerte.
- **[HOLD] ETH-USD** (Confianza: 65%): ETH-USD muestra un rendimiento positivo del +0.29% con un RSI de 1h en 37.5 saliendo de la zona de sobreventa. Se mantiene abierta buscando alcanzar el rango de take-profit del +2.0% al +3.5%.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones en QQQ y ETH-USD por ahora mientras monitoreamos de cerca los niveles de stop-loss del -2.0% y buscamos un take-profit entre +2.0% y +3.5%. Dado que BTC-USD presenta un RSI de 1 hora en 31.8 y un RSI diario en 35.0 en zona de sobreventa, mantendremos este activo en la mira para una potencial entrada agresiva en el próximo ciclo si el cambio de 1h se acelera al alza, utilizando la liquidez disponible manteniendo el colchón mínimo de efectivo."
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
