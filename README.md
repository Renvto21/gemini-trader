# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 16:20:52`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.81 USD** | **$38.94 USD** | 🔴 **-2.66%** ($-1.06) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $338.93 | $9.95 | 📉 -0.50% | 4h 19m |
| `ETH-USD` | 0.004058 | $2452.17 | $2430.29 | $9.86 | 📉 -0.89% | 2h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado general muestra una ligera corrección en el corto plazo con la mayoría de los activos tecnológicos y criptomonedas operando bajo sus medias móviles de 20 periodos en gráfico diario. Sin embargo, los mercados cripto permanecen abiertos 24/7 ofreciendo la mayor flexibilidad táctica. Nuestras posiciones actuales en AAPL y ETH-USD se mantienen estables dentro de márgenes manejables de pérdida, sin haber alcanzado el stop-loss estricto del -2.0%. Mantendremos la calma y daremos espacio a ETH-USD para consolidar su tendencia alcista de 24 horas, mientras que AAPL se mantiene vigilada de cerca por su RSI de 1 hora en niveles bajos."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra un rendimiento positivo en 24 horas (+1.06%) a pesar de un pequeño retroceso en la última hora. El holding time actual es de 2h 29m, por lo que debemos darle más tiempo para que desarrolle el rebote técnico esperado sin precipitar una venta anticipada.
- **[HOLD] AAPL** (Confianza: 70%): AAPL se encuentra con un pequeño retroceso (-0.5%), pero su tendencia diaria sigue siendo alcista sobre la SMA20 y su RSI de 1 hora está en 34.2, cerca de la zona de sobreventa. Mantendremos la posición para buscar el rebote técnico hacia nuestros objetivos de ganancia.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales (AAPL y ETH-USD) evaluando su comportamiento durante las próximas horas. Vigilar el RSI de 1 hora de AAPL para detectar un rebote técnico hacia la zona de take-profit (+2.0%) o cortar pérdidas si el precio rompe soportes clave por debajo del -2.0%. Mantener la liquidez actual disponible para reaccionar ante cualquier volatilidad inminente en los mercados de criptomonedas."
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
