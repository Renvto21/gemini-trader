# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 16:20:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.48 USD** | **$19.95 USD** | **$38.43 USD** | 🔴 **-3.93%** ($-1.57) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.096209 | $103.94 | $103.89 | $10.00 | 📉 -0.05% | 6h 0m |
| `ETH-USD` | 0.004126 | $2423.75 | $2413.48 | $9.96 | 📉 -0.42% | 4h 30m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "Los mercados tradicionales se encuentran cerrados, por lo que la liquidez activa se concentra en criptomonedas. Los activos SOL-USD y ETH-USD muestran una consolidación con ligeras variaciones negativas pero manteniendo niveles de sobreventa diaria atractivos para un rebote técnico. El volumen y el impulso de corto plazo se mantienen planos, sin señales inmediatas de ruptura al alza ni vulneración crítica de soportes."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición se mantiene estable con un PnL de -0.05% tras 6 horas de holding. El RSI diario se encuentra en niveles de sobreventa profunda (22.5) y el RSI de 1 hora (37.8) muestra potencial para un rebote alcista si se incrementa el volumen.
- **[HOLD] ETH-USD** (Confianza: 75%): La posición acumula una pérdida menor de -0.42% tras 4.5 horas. El contexto de RSI diario en 28.2 respalda la tesis de reversión a la media, por lo que se mantiene la posición esperando el impulso técnico.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones abiertas de SOL-USD y ETH-USD durante este ciclo ya que el PnL se mantiene controlado dentro de rangos aceptables y no se han activado los stop-loss de -2.0%. Monitorearemos de cerca el RSI de 1 hora en busca de un aumento de volumen que impulse los precios hacia el objetivo de ganancia de +2.0% a +3.5%. Si el impulso falla y se acercan al límite de pérdidas, procederemos a vender inmediatamente para proteger el capital."
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
