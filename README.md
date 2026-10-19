# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 21:10:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$30.31 USD** | **$8.08 USD** | **$38.39 USD** | 🔴 **-4.02%** ($-1.61) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.077662 | $103.01 | $104.04 | $8.08 | 📈 +1.00% | 1h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se mantiene abierto y operando con un sesgo alcista moderado de corto plazo, con SOL-USD mostrando un rendimiento positivo actual del +1.0% y un RSI de 1h en 51.2, consolidando su recuperación tras el rebote inicial. Los mercados tradicionales permanecen cerrados por fin de semana. Mantenemos una postura táctica en cripto para capitalizar posibles extensiones del movimiento alcista."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición en SOL-USD acumula un rendimiento del +1.0% con un holding time de menos de 2 horas. El RSI de 1h se encuentra estable en 51.2 y el precio actual evoluciona favorablemente hacia nuestro objetivo de take-profit entre +2.0% y +3.5%, por lo que decidimos mantenerla activa.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Bitácora de ciclo: SOL-USD se mantiene en cartera con una ganancia actual de +1.0%, todavía por debajo del objetivo de take-profit de +2.0% a +3.5%. Mantendremos la posición vigilando de cerca que el RSI de 1h continúe al alza o alcance la zona de sobrecompra superior a 70 para ejecutar la venta. El efectivo disponible se mantiene en reserva táctica esperando nuevas señales o confirmaciones de impulso en activos 24/7."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **74** | 🎯 **41.9%** (31W / 29L / 14BE) | 🔴 **$-1.55 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-18 21:00` | 🔴 SELL (+0.16$) | `ETH-USD` | $8.16 | $2409.06 | ETH-USD ha alcanzado una ganancia del +2.03%, cumpliendo con la regla de toma rápida de ga... |
| `2026-10-18 19:30` | 🟢 BUY | `SOL-USD` | $8.00 | $103.01 | SOL-USD presenta un RSI diario extremadamente bajo (16.5) y un RSI de 1h recuperándose has... |
| `2026-10-18 19:10` | 🔴 SELL (+0.17$) | `SOL-USD` | $8.17 | $102.92 | SOL-USD ha alcanzado un rendimiento de +2.07% cumpliendo con nuestra regla de toma rápida ... |
| `2026-10-18 18:40` | 🟢 BUY | `ETH-USD` | $8.00 | $2361.22 | ETH-USD muestra un RSI diario deprimido en 21.5 y un RSI de 1 hora que se recupera a 34.3 ... |
| `2026-10-18 17:00` | 🟢 BUY | `SOL-USD` | $8.00 | $100.83 | SOL-USD muestra un RSI diario extremadamente deprimido en 15.3 y un RSI de 1 hora en 23.4 ... |

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
