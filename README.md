# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 17:30:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.48 USD** | **$19.98 USD** | **$38.46 USD** | 🔴 **-3.86%** ($-1.54) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096209 | $103.94 | $104.04 | $10.01 | 📈 +0.10% | 7h 10m |
| `ETH-USD` | 0.004126 | $2423.75 | $2416.95 | $9.97 | 📉 -0.28% | 5h 40m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado por lo que la operativa se concentra exclusivamente en el mercado cripto (24/7). Las posiciones actuales en SOL-USD y ETH-USD muestran una consolidación lateral con bajo momentum tras varias horas abiertas, manteniendo variaciones cercanas al punto de equilibrio sin alcanzar las metas de take-profit ni activar los stops de protección. No hay señales claras de ruptura inminente en 1 hora, por lo que se mantiene la postura de espera."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 65%): La posición lleva varias horas abierta con un rendimiento plano (0.1%). Mantiene un RSI diario atractivo en sobreventa profunda (22.6), por lo que retenemos a la espera de que el rsi_1h supere la zona neutral de 50 para buscar el take-profit.
- **[HOLD] ETH-USD** (Confianza: 65%): La posición en ETH-USD muestra una leve pérdida del -0.28% pero se mantiene holgadamente por encima del stop-loss estricto de -2.0%. Esperamos que acompañe el rebote técnico diario (RSI diario de 28.3) en cuanto el mercado cripto recupere el momentum de corto plazo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos SOL-USD y ETH-USD en este ciclo mientras esperamos un incremento de volumen y una ruptura del rsi_1h por encima de 50 que active el impulso alcista hacia el objetivo de +2.0% o más. Si las posiciones continúan estancadas sin movimiento en las siguientes horas, rotaremos el capital hacia oportunidades con mayor volatilidad en cripto."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **65** | 🎯 **40.0%** (26W / 25L / 14BE) | 🔴 **$-1.41 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-17 11:50` | 🟢 BUY | `ETH-USD` | $10.00 | $2423.75 | ETH-USD presenta un RSI diario en niveles de sobreventa profunda (28.9) y un cambio positi... |
| `2026-10-17 10:20` | 🟢 BUY | `SOL-USD` | $10.00 | $103.94 | SOL-USD presenta un RSI diario en niveles de sobreventa extrema (22.5) y un cambio positiv... |
| `2026-10-17 04:30` | 🔴 SELL (+0.12$) | `SOL-USD` | $10.12 | $104.94 | SOL-USD ha alcanzado un RSI de 1 hora de 70.4, entrando en zona de sobrecompra, y acumula ... |
| `2026-10-17 04:00` | 🔴 SELL (+0.07$) | `ETH-USD` | $10.07 | $2429.64 | ETH-USD ha alcanzado un RSI de 1 hora de 73.3, entrando en zona de sobrecompra. Siguiendo ... |
| `2026-10-16 16:30` | 🟢 BUY | `ETH-USD` | $10.00 | $2412.98 | ETH-USD muestra un RSI diario en niveles de sobreventa extrema (30.3) y un cambio positivo... |

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
