# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 15:20:49`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.90 USD** | **$39.02 USD** | 🔴 **-2.45%** ($-0.98) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $340.10 | $9.98 | 📉 -0.16% | 3h 19m |
| `ETH-USD` | 0.004058 | $2452.17 | $2442.83 | $9.91 | 📉 -0.38% | 1h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sesgo de consolidación con la mayoría de los activos tradicionales y criptomonedas operando con ligeras variaciones negativas en la última hora, aunque mantienen un tono constructivo en las últimas 24 horas. Los índices principales y las criptomonedas como ETH-USD y SOL-USD presentan condiciones de soporte diario interesantes, aunque la falta de momentum fuerte de corto plazo exige paciencia y estricta gestión de riesgo."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 60%): AAPL se mantiene estable con una pérdida marginal del -0.16%, por debajo del umbral de stop-loss y con un holding time moderado. Esperaremos a que desarrolle mayor momentum o alcance niveles objetivos antes de tomar acción.
- **[HOLD] ETH-USD** (Confianza: 65%): ETH-USD muestra un rendimiento positivo en 24 horas (+1.58%) a pesar de la ligera corrección horaria. Su rsi_daily en zona de soporte sugiere potencial alcista continuo, por lo que se mantiene en cartera esperando el objetivo de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones de AAPL y ETH-USD por ahora, monitoreando de cerca su evolución. Para el siguiente ciclo, si ETH-USD o AAPL muestran debilidad adicional o se acercan al nivel de stop-loss del -2.0%, procederemos a liquidarlas inmediatamente para liberar capital. Si alcanzan la zona de take-profit entre +2.0% y +3.5%, aseguraremos ganancias de inmediato."
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
