# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-11 07:10:36`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$40.30 USD** | **$40.30 USD** | 🟢 **+0.75%** ($+0.30) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.330438 | $109.27 | $109.42 | $36.16 | 📈 +0.13% |
| `ETH-USD` | 0.001656 | $2499.59 | $2500.10 | $4.14 | 📈 +0.02% |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> *"El mercado muestra una divergencia interesante con el sector tecnológico y de índices tradicionales (QQQ, SPY, MSFT) manteniendo una tendencia alcista firme, mientras que las criptomonedas principales (SOL-USD y ETH-USD) se encuentran profundamente en territorio de sobreventa técnica (RSI de 21.3 y 28.2 respectivamente) debido a caídas recientes en los últimos 7 días. De acuerdo con nuestra estrategia agresiva de mean reversion y caza de rebotes, esto representa una oportunidad ideal de acumulación en los activos cripto sobrevendidos. Mantendremos nuestra posición en SOL-USD aprovechando su extrema sobreventa y decidiremos hacer una pequeña rotación o mantener las posiciones actuales si no hay efectivo libre, pero dado que tenemos 0 USD en efectivo y ambas posiciones cripto están planas (con un PnL cercano a 0%), mantendremos el portafjolio actual para no incurrir en comisiones ni perdernos el rebote inminente en SOL y ETH."*

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 88%): SOL-USD se encuentra en condición de sobreventa extrema con un RSI de 21.3 tras una caída semanal del -9.38%. El portafolio no cuenta con efectivo libre ($0.0) y la posición está prácticamente plana (+0.13%), por lo que vender ahora anularía la oportunidad de capturar el rebote técnico esperado hacia la media.

---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-11 05:00` | 🟢 BUY | `ETH-USD` | $4.14 | $2499.59 | ETH-USD presenta un RSI de 28.2, lo que indica una clara condición de sobreventa técnica t... |
| `2026-10-11 04:50` | 🟢 BUY | `SOL-USD` | $12.00 | $109.36 | Alta convicción en el rebote técnico de Solana tras una caída semanal del -9.43% y un RSI ... |
| `2026-10-11 04:50` | 🔴 SELL | `ETH-USD` | $16.12 | $2500.30 | Rotamos capital fuera de ETH-USD para asegurar una pequeña ganancia del +0.75% y liberar l... |
| `2026-10-11 03:20` | 🟢 BUY | `SOL-USD` | $12.00 | $109.35 | SOL-USD se encuentra en una situación de sobreventa técnica masiva con un RSI de 14 en 21.... |
| `2026-10-11 03:20` | 🔴 SELL | `MSFT` | $12.00 | $535.07 | MSFT ha entrado en zona de sobrecompra técnica con un RSI de 72.3. Aplicando la regla táct... |

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
