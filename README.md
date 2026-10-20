# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 15:50:57`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$19.12 USD** | **$19.86 USD** | **$38.98 USD** | 🔴 **-2.54%** ($-1.02) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.029357 | $340.64 | $340.07 | $9.98 | 📉 -0.17% | 3h 49m |
| `ETH-USD` | 0.004058 | $2452.17 | $2433.97 | $9.88 | 📉 -0.74% | 1h 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sesgo general bajista en marcos diarios, con la mayoría de los activos operando por debajo de sus medias móviles de 20 periodos. Sin embargo, en el corto plazo (1 hora), la renta variable de EE. UU. (como AAPL) se mantiene estable, mientras que las criptomonedas registran ligeras correcciones horarias tras intentos de rebote previos. Mantenemos una actitud de vigilancia estricta sobre las posiciones actuales de AAPL y ETH-USD, evaluando su comportamiento dinámico para evitar pérdidas mayores al 2.0% y asegurar liquidez si el impulso decae."

**Operaciones del ciclo:**
- **[HOLD] AAPL** (Confianza: 60%): AAPL mantiene una tendencia alcista diaria sobre su SMA20 y una pérdida marginal controlada (-0.17%). No ha alcanzado el stop-loss operativo y su comportamiento se mantiene dentro del rango esperado para un rebote.
- **[HOLD] ETH-USD** (Confianza: 60%): ETH-USD registra una leve corrección horaria, pero su RSI diario se encuentra en niveles de sobreventa extrema (28.6), lo que mantiene intacta la tesis de un potencial rebote por reversión a la media (mean reversion).

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones abiertas de AAPL y ETH-USD por este ciclo. Establecemos un stop-loss estricto operativo en -1.5% a -2.0% para ambas posiciones. Si ETH-USD o AAPL pierden tracción o el RSI de 1 hora perfora soportes clave, procederemos a la venta inmediata para rescatar efectivo y buscar activos con mayor momentum alcista."
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
