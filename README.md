# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 16:00:57`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.86 USD** | **$38.99 USD** | 🔴 **-2.53%** ($-1.01) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $339.81 | $9.98 | 📉 -0.24% | 3h 59m |
| `ETH-USD` | 0.004058 | $2452.17 | $2436.29 | $9.89 | 📉 -0.65% | 2h 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un tono mixto con sesgo bajista en la mayoría de los activos principales bajo sus medias móviles de 20 periodos, aunque las criptomonedas continúan operando con estabilidad en fin de semana/horario continuo. Las posiciones actuales se mantienen estables con pérdidas mínimas que no activan el stop-loss estricto (-2%), mientras el RSI de 1 hora en ETH-USD se recupera favorablemente hacia 62.7."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD mantiene un buen comportamiento con un rsi_1h en 62.7 y un cambio de 24 horas positivo (+1.31%). Mantenemos la posición buscando capturar la continuación del rebote hacia la zona de take-profit.
- **[HOLD] AAPL** (Confianza: 75%): AAPL registra una ligera pérdida de -0.24% que se mantiene muy controlada. Esperaremos a la apertura y evolución de la sesión bursátil para evaluar si recupera momentum alcista sobre su tendencia diaria.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones de AAPL y ETH-USD activas ya que se encuentran dentro del rango de tolerancia de riesgo. Establecemos take-profit automático si ETH-USD o AAPL alcanzan rendimientos de +2.0% o un RSI de 1 hora superior a 70. Si alguna de las dos posiciones perfora el umbral de pérdida de -2.0%, procederemos a la venta inmediata para asegurar liquidez."
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
