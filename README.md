# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 15:20:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.57 USD** | **$20.01 USD** | **$38.58 USD** | 🔴 **-3.55%** ($-1.42) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $719.32 | $10.01 | 📈 +0.06% | 4h 39m |
| `ETH-USD` | 0.004178 | $2393.62 | $2395.45 | $10.01 | 📈 +0.08% | 2h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado se encuentra mayormente en un sesgo bajista de corto plazo (bajo SMA20) con una consolidación lateral en la última hora. Las criptomonedas muestran condiciones de sobreventa extrema en sus indicadores diarios, destacando SOL-USD y BTC-USD con RSI de 1 hora cercanos o por debajo de 35, lo que sugiere oportunidades potenciales de rebote técnico. En renta variable, QQQ y ETH-USD se mantienen en cartera con ganancias marginales planas tras varias horas sin lograr el momentum alcista esperado."

**Operaciones del ciclo:**
- **[HOLD] QQQ** (Confianza: 60%): La posición en QQQ lleva casi 4.5 horas abierta con una ganancia marginal del +0.06%. Aunque el momentum intradiario se ha desacelerado, se mantiene por encima del precio de entrada y lejos del stop-loss, por lo que retendremos la posición esperando el objetivo de take-profit.
- **[HOLD] ETH-USD** (Confianza: 60%): ETH-USD registra una pequeña ganancia del +0.08% tras 2.5 horas. El RSI de 1 hora está en 33.7, lo que indica que se mantiene en zona de soporte técnico. Daremos un ciclo más para que el rebote tome fuerza antes de considerar rotación de capital.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos nuestras posiciones en QQQ y ETH-USD por ahora, vigilando de cerca el nivel de stop-loss del -2.0% y esperando que alcancen el objetivo de take-profit entre +2.0% y +3.5%. Si QQQ o ETH-USD no muestran aceleración en el próximo ciclo, rotaremos capital hacia SOL-USD, que presenta un RSI diario muy deprimido de 19.2 listo para un rebote de reversión a la media. Mantendremos la liquidez en efectivo por encima de los $4.00 USD requeridos."
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
