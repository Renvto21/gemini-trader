# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 14:40:48`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.57 USD** | **$20.02 USD** | **$38.58 USD** | 🔴 **-3.55%** ($-1.42) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $719.28 | $10.01 | 📈 +0.05% | 4h 0m |
| `ETH-USD` | 0.004178 | $2393.62 | $2396.35 | $10.01 | 📈 +0.11% | 1h 49m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado se encuentra mayoritariamente con un sesgo bajista por debajo de las medias móviles de 20 periodos, pero con oportunidades latentes de rebote por sobreventa en criptomonedas y activos tecnológicos clave. Las posiciones actuales de QQQ y ETH-USD muestran una variación lateral leve, manteniendo un rendimiento cercano a cero mientras se espera la confirmación de volumen para un impulso alcista."

**Operaciones del ciclo:**
- **[HOLD] QQQ** (Confianza: 70%): La posición en QQQ lleva pocas horas abierta con una ganancia marginal del +0.05%. El RSI de 1 hora está en 44.4 y se mantiene dentro de los límites de riesgo aceptables, esperando el desarrollo del momentum intradiario.
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD se mantiene estable con una pequeña ganancia del +0.11%. Su RSI de 1 hora se encuentra en 37.5, recuperándose de la zona de sobreventa previa. Mantendremos la posición para capturar el rebote técnico esperado.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos QQQ y ETH-USD por el momento al estar estables, pero vigilaremos de cerca sus niveles de RSI de 1 hora y rentabilidad. Si ETH-USD o QQQ alcanzan el objetivo de take-profit entre +2.0% y +3.5%, o si su RSI de 1 hora supera los 65, procederemos a vender para asegurar ganancias. Mantendremos el efectivo restante de $18.57 USD a la espera de un gatillo más fuerte en SOL-USD o BTC-USD para desplegar capital."
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
