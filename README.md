# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 16:01:11`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.57 USD** | **$20.02 USD** | **$38.59 USD** | 🔴 **-3.53%** ($-1.41) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $719.72 | $10.01 | 📈 +0.11% | 5h 20m |
| `ETH-USD` | 0.004178 | $2393.62 | $2396.00 | $10.01 | 📈 +0.10% | 3h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado se encuentra mayormente lateral a bajista en el corto plazo, con índices y criptomonedas consolidando cerca de soportes. QQQ y ETH-USD muestran ganancias marginales pero sin el impulso necesario para alcanzar el take-profit. BTC-USD y SOL-USD se mantienen en zonas de sobreventa extrema en marcos diarios y de 1 hora, ideales para vigilar un rebote técnico inminente."

**Operaciones del ciclo:**
- **[HOLD] QQQ** (Confianza: 60%): La posición en QQQ mantiene una pequeña ganancia del +0.11% tras 5 horas de holding. Aunque el momentum de corto plazo es moderado, nos mantenemos dentro del plan esperando que alcance el objetivo de take-profit del +2.0% o un corte defensivo si rompe soportes.
- **[HOLD] ETH-USD** (Confianza: 60%): ETH-USD muestra estabilidad con una ganancia marginal del +0.10%. Esperamos que la zona de sobreventa en el RSI diario impulse un rebote más fuerte en las próximas horas hacia el rango de take-profit establecido.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones abiertas en QQQ y ETH-USD monitoreando de cerca el stop-loss del -2.0% y esperando un take-profit entre +2.0% y +3.5%. Dado que SOL-USD muestra un RSI diario de 19.1 y un RSI de 1 hora de 30.6, lo mantendremos en estricta vigilancia para una posible entrada agresiva en el próximo ciclo si el cambio de 1h se torna positivo. Preservaremos la liquidez actual cumpliendo con el colchón mínimo de efectivo."
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
