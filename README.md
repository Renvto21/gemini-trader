# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 16:00:55`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.26 USD** | **$34.49 USD** | **$38.75 USD** | 🔴 **-3.13%** ($-1.25) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.48 | $9.89 | 📉 -1.06% | 1d 5h |
| `MSFT` | 0.012146 | $535.17 | $540.48 | $6.56 | 📈 +0.99% | 5h 10m |
| `QQQ` | 0.013791 | $725.09 | $725.88 | $10.01 | 📈 +0.11% | 3h 40m |
| `NVDA` | 0.036812 | $217.32 | $217.78 | $8.02 | 📈 +0.21% | 3h 10m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de valores se mantiene abierto con un sesgo mixto a bajista en tendencia general, aunque se observan oportunidades interesantes de rebote por sobreventa en activos tecnológicos como QQQ y NVDA, cuyos indicadores de RSI en 1 hora muestran niveles de sobreventa extrema. Por otro lado, los criptoactivos como ETH y SOL muestran un RSI de 1 hora elevado en zona de sobrecompra, sugiriendo cautela antes de nuevas entradas en ese sector."

**Operaciones del ciclo:**
- **[HOLD] QQQ** (Confianza: 80%): QQQ mantiene un RSI de 1h en 25.8 (sobreventa extrema) y muestra un pequeño cambio positivo en 1h. Aunque la tendencia diaria es bajista, el potencial de rebote técnico a corto plazo justifica mantener la posición abierta para capturar la recuperación.
- **[HOLD] NVDA** (Confianza: 80%): NVDA presenta un RSI de 1h de 22.3 con un inicio de recuperación en su cambio de 1h (+0.31%). El activo se encuentra en zona de rebote técnico inminente tras una caída semanal fuerte, por lo que se mantiene la posición para buscar el objetivo de ganancia.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en QQQ, NVDA, MSFT y AAPL mientras desarrollan su momentum técnico. MSFT está cerca de registrar ganancias y evaluaré tomar beneficios si alcanza el rango de +2.0% a +3.5%. QQQ y NVDA muestran un RSI de 1h muy deprimido, por lo que mantendré los ojos puestos en una posible confirmación de rebote alcista en los próximos ciclos. Mantendré la liquidez actual intacta ($4.26 USD) esperando una oportunidad de alta convicción."
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
