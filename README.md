# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 16:40:49`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.82 USD** | **$38.95 USD** | 🔴 **-2.63%** ($-1.05) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $339.05 | $9.95 | 📉 -0.47% | 4h 39m |
| `ETH-USD` | 0.004058 | $2452.17 | $2432.28 | $9.87 | 📉 -0.81% | 2h 49m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general muestra una tendencia mixta con sesgo bajista en la mayoría de los índices principales bajo la SMA20, mientras que las criptomonedas operan de manera estable en 24/7. AAPL y ETH-USD muestran ligeras pérdidas por debajo del -1%, pero sin romper el umbral crítico de stop-loss del -2%. Mantendremos las posiciones vigentes mientras se consolida el precio."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 80%): AAPL mantiene una pérdida pequeña de -0.47% con un holding time de más de 4 horas, pero el precio se mantiene relativamente estable sobre su soporte técnico macro. No amerita cortar la pérdida aún.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD registra una leve corrección de -0.81%, operando en el mercado 24/7. El RSI diario se encuentra en niveles bajos (28.4) lo que sugiere potencial de rebote inminente. Mantendremos la posición esperando el impulso alcista.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear AAPL y ETH-USD. Si AAPL o ETH-USD extienden sus pérdidas acercándose al límite de -2.0%, procederé a vender inmediatamente para proteger el capital. Si alguna de las dos muestra un repunte hacia el take-profit del +2.0%, tomaré ganancias para rotar efectivo."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **82** | 🎯 **43.9%** (36W / 31L / 15BE) | 🔴 **$-0.79 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-20 13:51` | 🟢 BUY | `ETH-USD` | $9.95 | $2452.17 | ETH-USD muestra un excelente impulso de corto plazo con change_1h_pct positivo (+0.55%) y ... |
| `2026-10-20 13:51` | 🔴 SELL (-0.05$) | `GLD` | $9.95 | $377.90 | GLD se encuentra estancado con un rendimiento ligeramente negativo (-0.47%) y un rsi_1h de... |
| `2026-10-20 12:01` | 🟢 BUY | `GLD` | $10.00 | $379.70 | GLD presenta un RSI de 1 hora en 31.4, acercándose a la zona ideal de sobreventa para acti... |
| `2026-10-20 12:01` | 🟢 BUY | `AAPL` | $10.00 | $340.64 | AAPL se encuentra en tendencia alcista diaria con un RSI de 1 hora en 33.1 (cercano a sobr... |
| `2026-10-20 11:10` | 🔴 SELL (+0.12$) | `BTC-USD` | $8.69 | $82949.93 | BTC-USD muestra un RSI de 1 hora en 72.2 (sobrecompra) y un rendimiento positivo de +1.45%... |

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
