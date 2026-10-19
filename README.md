# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 13:40:47`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.57 USD** | **$20.05 USD** | **$38.62 USD** | 🔴 **-3.46%** ($-1.38) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $721.07 | $10.03 | 📈 +0.30% | 3h 0m |
| `ETH-USD` | 0.004178 | $2393.62 | $2398.34 | $10.02 | 📈 +0.20% | 49m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado se encuentra mayormente estable con un sesgo lateral a la baja de corto plazo en los principales índices y criptomonedas. QQQ y ETH-USD muestran ganancias marginales (+0.3% y +0.2% respectivamente) sin alcanzar aún el objetivo de take-profit. Los indicadores de 1 hora se mantienen neutrales sin mostrar sobrecompra, por lo que optamos por mantener las posiciones actuales mientras desarrollan su momentum técnico."

**Operaciones del ciclo:**
- **[HOLD] QQQ** (Confianza: 75%): La posición mantiene una ganancia leve del +0.3% tras 3 horas abierta. El RSI de 1 hora se sitúa en 45.5 sin señales de debilidad extrema ni de sobrecompra, por lo que mantenemos la posición esperando el impulso hacia el objetivo de take-profit.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD registra un beneficio modesto del +0.2% con un RSI de 1 hora en 37.1 que muestra estabilidad. Mantenemos la posición activa para permitir que el rebote técnico desarrolle todo su potencial de corto plazo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones de QQQ y ETH-USD vigentes este ciclo. Seguiremos vigilando de cerca el RSI de 1 hora de ambos activos para asegurar beneficios si se acercan al rango de +2.0% a +3.5%, o para recortar si el soporte falla y se activa el stop-loss en -2.0%. Mantendremos la liquidez en reserva para capturar nuevas oportunidades si surge un fuerte impulso alcista."
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
