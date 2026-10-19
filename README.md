# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 12:30:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$28.57 USD** | **$10.07 USD** | **$38.63 USD** | 🔴 **-3.42%** ($-1.37) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $723.64 | $10.07 | 📈 +0.66% | 1h 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado se encuentra operando de forma mixta con sesgo neutral a bajista en temporalidades diarias. QQQ muestra un avance leve pero su momentum de 1 hora se ha aplanado (change_1h_pct -0.01% y rsi_1h en 51.0), situándose cerca de nuestra entrada con un pequeño beneficio acumulado del +0.66%. Las criptomonedas muestran signos de estabilización tras las ventas previas, con SOL-USD mostrando un ligero repunte intradiario, pero sin alcanzar aún los umbrales ideales de sobreventa extrema (< 35) para una entrada agresiva de rebote inmediato."

**Operaciones del ciclo:**
- **[HOLD] QQQ** (Confianza: 65%): La posición en QQQ lleva menos de 2 horas abierta y muestra una ganancia moderada de +0.66%. No ha alcanzado el objetivo de take-profit (+2.0% a +3.5%) ni ha roto el stop-loss estricto (-2.0%), por lo que se mantiene para permitir que el impulso se desarrolle según lo planificado.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos la posición actual en QQQ por el momento, vigilando de cerca si logra extender su ganancia hacia el rango objetivo de +2.0% a +3.5% para asegurar el take-profit, o si pierde soporte para activar nuestro stop-loss estricto en -2.0%. Dado que el holding time es bajo y no hay caídas abruptas ni sobrecompras críticas, conservaremos la liquidez en reserva para cazar oportunidades de rebote más agresivas en criptoactivos (como ETH-USD o SOL-USD) si el RSI de 1 hora desciende nuevamente a zonas de sobreventa."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **77** | 🎯 **42.9%** (33W / 29L / 15BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-19 10:40` | 🟢 BUY | `QQQ` | $10.00 | $718.92 | QQQ muestra un fuerte momentum intradiario con un cambio de 1h del +1.28%, liderando el re... |
| `2026-10-19 01:50` | 🔴 SELL (+0.09$) | `ETH-USD` | $8.09 | $2428.97 | ETH-USD registra una ganancia acumulada y su RSI de 1 hora ha alcanzado 68.3, acercándose ... |
| `2026-10-19 01:00` | 🔴 SELL (-0.00$) | `SOL-USD` | $8.00 | $105.08 | SOL-USD ha entrado en sobrecompra con un RSI de 1 hora en 72.7, cumpliendo estrictamente c... |
| `2026-10-18 23:20` | 🟢 BUY | `SOL-USD` | $8.00 | $105.11 | SOL-USD presenta un RSI diario en 21.8 (sobreventa extrema) y un momentum de 24 horas alci... |
| `2026-10-18 23:10` | 🔴 SELL (+0.17$) | `SOL-USD` | $8.17 | $105.19 | SOL-USD acumula una ganancia del +2.12%, cumpliendo con la regla de toma rápida de gananci... |

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
