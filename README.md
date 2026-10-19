# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-19 18:21:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.00 USD** | **$34.65 USD** | **$38.64 USD** | 🔴 **-3.39%** ($-1.36) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 7h 41m |
| `ETH-USD` | 0.004178 | $2393.62 | $2401.73 | $10.03 | 📈 +0.34% | 5h 30m |
| `SOL-USD` | 0.096034 | $104.13 | $104.62 | $10.05 | 📈 +0.47% | 1h 40m |
| `BTC-USD` | 0.000056 | $81874.05 | $81971.54 | $4.58 | 📈 +0.12% | 1h 10m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "Los mercados tradicionales (Wall Street) permanecen cerrados, concentrando toda la actividad en el sector cripto. Bitcoin, Ethereum y Solana muestran señales de estabilización y rebote técnico incipiente: sus RSI de 1 hora continúan recuperándose (35.7 en BTC, 38.2 en ETH y 41.2 en SOL) con variaciones intradiarias positivas en la última hora (+0.07%, +0.16% y +0.18% respectivamente). El soporte macro en gráficos diarios (RSI diario sobrevendido) está conteniendo la caída, dando espacio a una extensión del rebote hacia las medias móviles de corto plazo."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 85%): La posición en ETH-USD avanza favorablemente (+0.34%) con RSI 1h escalando a 38.2 tras el soporte en sobreventa diaria extrema (24.3). El efectivo está en su mínimo de reserva ($4.00) y el rebote técnico se está desplegando conforme a la estrategia, por lo que se mantiene la posición buscando el objetivo de toma de ganancias de +2.0% a +3.5%.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener posiciones activas en ETH-USD, SOL-USD y BTC-USD mientras se consolida la recuperación técnica. QQQ permanece congelado por mercado cerrado. Metas de salida rápida (Take-Profit): +2.0% a +3.5% en cada posición cripto o RSI 1H > 70. Nivel de Stop-Loss preventivo fijado estrictamente en -2.0% desde el precio de entrada. Si en los próximos 2 ciclos ETH o BTC no logran acelerar por encima de +1.0% o pierden el momentum horario, se considerará rotar capital para liberar liquidez hacia el activo de mayor fuerza relativa (actualmente SOL)."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **77** | 🎯 **42.9%** (33W / 29L / 15BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-19 17:10` | 🟢 BUY | `BTC-USD` | $4.57 | $81874.05 | BTC-USD muestra señales de rebote técnico con un RSI de 1 hora en 31.1 recuperándose y un ... |
| `2026-10-19 16:40` | 🟢 BUY | `SOL-USD` | $10.00 | $104.13 | SOL-USD presenta un RSI diario extremo de 19.7, indicando condiciones de sobreventa profun... |
| `2026-10-19 12:51` | 🟢 BUY | `ETH-USD` | $10.00 | $2393.62 | ETH-USD presenta un RSI de 1 hora en 34.6, entrando en zona de sobreventa de corto plazo, ... |
| `2026-10-19 10:40` | 🟢 BUY | `QQQ` | $10.00 | $718.92 | QQQ muestra un fuerte momentum intradiario con un cambio de 1h del +1.28%, liderando el re... |
| `2026-10-19 01:50` | 🔴 SELL (+0.09$) | `ETH-USD` | $8.09 | $2428.97 | ETH-USD registra una ganancia acumulada y su RSI de 1 hora ha alcanzado 68.3, acercándose ... |

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
