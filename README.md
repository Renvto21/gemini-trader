# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 16:30:49`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.57 USD** | **$20.03 USD** | **$38.60 USD** | 🔴 **-3.51%** ($-1.40) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $720.37 | $10.02 | 📈 +0.20% | 5h 50m |
| `ETH-USD` | 0.004178 | $2393.62 | $2396.29 | $10.01 | 📈 +0.11% | 3h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado se encuentra en un estado de consolidación bajista general, operando principalmente por debajo de sus medias móviles de 20 periodos. Las criptomonedas muestran signos de sobreventa extrema en marcos diarios (como SOL-USD y ETH-USD), mientras que los índices tradicionales (QQQ, SPY) se mantienen estables pero sin el impulso alcista necesario para generar ganancias rápidas en este momento."

**Operaciones del ciclo:**
- **[HOLD] QQQ** (Confianza: 75%): La posición en QQQ lleva pocas horas abierta con una ganancia marginal del +0.2%. Mantenemos la posición a la espera de que el momentum diario se consolide hacia el objetivo de take-profit.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra un RSI diario de 24.1, lo que respalda la tesis de rebote por sobreventa. Aunque el cambio de 1h es ligeramente negativo, se mantiene dentro del rango seguro antes del stop-loss.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales de QQQ y ETH-USD monitoreando de cerca el stop-loss en -2.0% y buscando un take-profit entre +2.0% y +3.5%. Estaremos atentos a un cambio de 1h positivo en SOL-USD para entrar en su inminente rebote por sobreventa extrema en el RSI diario (19.2). Conservaremos la liquidez mínima de reserva."
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
