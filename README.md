# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 15:40:55`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.87 USD** | **$39.00 USD** | 🔴 **-2.51%** ($-1.00) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $340.11 | $9.98 | 📉 -0.16% | 3h 39m |
| `ETH-USD` | 0.004058 | $2452.17 | $2436.76 | $9.89 | 📉 -0.63% | 1h 49m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado actual muestra un tono predominantemente bajista en marco diario para la mayoría de los activos tecnológicos y criptomonedas, aunque se mantienen oportunidades de rebote técnico de corto plazo. Los índices principales operan con leves variaciones horarias negativas, mientras que las criptomonedas y activos en cartera se mantienen estables dentro de los umbrales de tolerancia de riesgo permitidos antes de activar stops."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 70%): AAPL mantiene una pérdida muy leve de -0.16% tras casi 4 horas de holding y se encuentra sobre su media móvil diaria, por lo que se mantiene en cartera a la espera de un rebote más claro.
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD registra una ligera pérdida de -0.63%, operando dentro del rango de tolerancia y con un RSI de 1 hora saludable en 57.5, manteniendo el potencial de continuar su recuperación diaria.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones vigentes de AAPL y ETH-USD ya que no han alcanzado el stop-loss estricto del -2.0% y sus métricas de tendencia se mantienen operables. Monitorearemos de cerca su comportamiento en el siguiente ciclo; si alguna rompe el soporte o se estanca, procederemos a liquidar inmediatamente para liberar liquidez hacia oportunidades de mayor impulso."
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
