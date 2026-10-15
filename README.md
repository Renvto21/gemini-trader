# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 15:50:54`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.26 USD** | **$34.44 USD** | **$38.71 USD** | 🔴 **-3.23%** ($-1.29) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.63 | $9.90 | 📉 -1.02% | 1d 5h |
| `MSFT` | 0.012146 | $535.17 | $540.34 | $6.56 | 📈 +0.97% | 5h 0m |
| `QQQ` | 0.013791 | $725.09 | $724.48 | $9.99 | 📉 -0.08% | 3h 30m |
| `NVDA` | 0.036812 | $217.32 | $217.10 | $7.99 | 📉 -0.10% | 3h 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sesgo bajista general bajo la media móvil de 20 periodos en varios activos clave, aunque con oportunidades de rebote por sobreventa extrema en el corto plazo. Los índices tecnológicos como QQQ y valores como NVDA registran RSI de 1 hora muy deprimidos (22.8 y 19.3 respectivamente), lo que anticipa un potencial rebote técnico inminente. MSFT se mantiene positivo y estable, mientras que las criptomonedas muestran estabilidad con un leve sesgo alcista diario."

**Operaciones del ciclo:**
- **[HOLD] QQQ** (Confianza: 80%): QQQ tiene un RSI de 1 hora en sobreventa extrema (22.8) y se encuentra en proceso de consolidación para un rebote técnico. Mantengo la posición respetando el stop-loss y esperando el objetivo de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener QQQ, NVDA, AAPL y vigilar MSFT de cerca. MSFT está registrando una ganancia cercana al +0.97%, por lo que si alcanza la zona objetivo de +2.0% a +3.5%, procederé a tomar ganancias para liberar liquidez. AAPL mantiene un rendimiento estable con un pequeño retroceso (-1.02%) pero sin romper el stop-loss estricto de -2.0%. Si QQQ y NVDA muestran señales de agotamiento en sus rebotes y no logran romper al alza en los siguientes ciclos, rotaré parte de ese capital hacia criptomonedas como ETH-USD o SOL-USD para aprovechar el mercado 24/7."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **57** | 🎯 **42.1%** (24W / 19L / 14BE) | 🔴 **$-1.12 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-15 12:50` | 🟢 BUY | `NVDA` | $8.00 | $217.32 | NVDA presenta un RSI de 1h en sobreventa extrema (21.5) con un inicio de recuperación en s... |
| `2026-10-15 12:20` | 🟢 BUY | `QQQ` | $10.00 | $725.09 | QQQ muestra un RSI de 1h en sobreventa extrema (28.7) cruzando al alza con un cambio posit... |
| `2026-10-15 12:10` | 🔴 SELL (+0.14$) | `ETH-USD` | $6.14 | $2417.73 | ETH-USD ha alcanzado un rendimiento del +2.33%, cumpliendo con el rango establecido para l... |
| `2026-10-15 11:50` | 🔴 SELL (+0.13$) | `SOL-USD` | $6.13 | $104.21 | SOL-USD ha alcanzado un rendimiento de +2.11%, cumpliendo con la regla de toma rápida de g... |
| `2026-10-15 10:50` | 🟢 BUY | `MSFT` | $6.50 | $535.17 | MSFT presenta un RSI de 1h ultra comprimido en sobreventa extrema (14.7) con un cambio pos... |

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
