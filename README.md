# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 22:00:49`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$22.31 USD** | **$16.12 USD** | **$38.43 USD** | 🔴 **-3.92%** ($-1.57) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.077662 | $103.01 | $104.21 | $8.09 | 📈 +1.16% | 2h 30m |
| `ETH-USD` | 0.003330 | $2402.76 | $2411.27 | $8.03 | 📈 +0.35% | 40m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado por lo que la liquidez opera en criptomonedas 24/7. SOL-USD y ETH-USD muestran estabilidad con ligeras ganancias pero sin alcanzar todavía la zona objetivo de take-profit entre +2.0% y +3.5%. Mantenemos las posiciones activas mientras esperamos una aceleración del momentum en 1h."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición en SOL-USD muestra un PnL positivo del +1.16% tras 2.5 horas de holding. El RSI de 1h se encuentra en 52.3 y el precio se mantiene estable. Mantenemos la posición buscando alcanzar el take-profit entre +2.0% y +3.5%.
- **[HOLD] ETH-USD** (Confianza: 75%): La posición en ETH-USD registra una ganancia del +0.35% con un tiempo de holding de 40 minutos. El RSI de 1h está en 48.6. Esperamos la continuación del impulso alcista para asegurar ganancias parciales o totales al llegar al rango objetivo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos SOL-USD y ETH-USD en cartera esperando que alcancen el objetivo de take-profit (+2.0% a +3.5%) o que el RSI de 1h supere los 70 puntos para asegurar beneficios. El stop-loss se mantiene estricto en -2.0% para proteger el capital. No abrimos nuevas posiciones para respetar la reserva de liquidez y permitir que las operaciones actuales desarrollen su potencial."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **74** | 🎯 **41.9%** (31W / 29L / 14BE) | 🔴 **$-1.55 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-18 21:20` | 🟢 BUY | `ETH-USD` | $8.00 | $2402.76 | ETH-USD muestra un RSI diario fuertemente sobrevendido en 23.2 y un cambio positivo en la ... |
| `2026-10-18 21:00` | 🔴 SELL (+0.16$) | `ETH-USD` | $8.16 | $2409.06 | ETH-USD ha alcanzado una ganancia del +2.03%, cumpliendo con la regla de toma rápida de ga... |
| `2026-10-18 19:30` | 🟢 BUY | `SOL-USD` | $8.00 | $103.01 | SOL-USD presenta un RSI diario extremadamente bajo (16.5) y un RSI de 1h recuperándose has... |
| `2026-10-18 19:10` | 🔴 SELL (+0.17$) | `SOL-USD` | $8.17 | $102.92 | SOL-USD ha alcanzado un rendimiento de +2.07% cumpliendo con nuestra regla de toma rápida ... |
| `2026-10-18 18:40` | 🟢 BUY | `ETH-USD` | $8.00 | $2361.22 | ETH-USD muestra un RSI diario deprimido en 21.5 y un RSI de 1 hora que se recupera a 34.3 ... |

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
