# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 14:50:56`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.92 USD** | **$39.05 USD** | 🔴 **-2.38%** ($-0.95) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $339.83 | $9.98 | 📉 -0.24% | 2h 49m |
| `ETH-USD` | 0.004058 | $2452.17 | $2451.28 | $9.95 | 📉 -0.04% | 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sentimiento mixto con sesgo defensivo en renta variable (índices operando mayormente bajo su SMA20 a pesar de leves rebotes recientes), mientras que las criptomonedas como ETH-USD y SOL-USD mantienen un pulso positivo de corto plazo y acumulan retornos favorables en 24 horas. Mantenemos una postura táctica ágil, protegiendo posiciones con bajo momentum y preparándonos para capitalizar oportunidades en activos abiertos 24/7."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD fue comprado recientemente y muestra un comportamiento estable con momentum positivo de corto plazo (change_1h_pct positivo y rsi_1h saludable en 61.5). Se mantiene abierta buscando alcanzar el objetivo de take-profit.
- **[HOLD] AAPL** (Confianza: 60%): AAPL se encuentra ligeramente en negativo (-0.24%) pero dentro de márgenes aceptables de operación. Se vigilará estrictamente el nivel de stop-loss para evitar pérdidas mayores, manteniéndola temporalmente en cartera a la espera de una recuperación.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener ETH-USD con objetivo de take-profit entre +2.0% y +3.5% o si el RSI de 1 hora supera 70. Vigilar AAPL de cerca: si rompe a la baja el soporte o extiende pérdidas hacia el límite del stop-loss de -2.0%, proceder a liquidar para rotar capital hacia crypto de mayor inercia. Mantener la liquidez lista para reaccionar ante rupturas de momentum."
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
