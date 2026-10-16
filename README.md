# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 23:20:48`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$14.17 USD** | **$24.59 USD** | **$38.76 USD** | 🔴 **-3.11%** ($-1.24) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $539.44 | $6.55 | 📈 +0.80% | 12h 30m |
| `QQQ` | 0.013791 | $725.09 | $728.00 | $10.04 | 📈 +0.40% | 11h 0m |
| `NVDA` | 0.036812 | $217.32 | $217.23 | $8.00 | 📉 -0.04% | 10h 30m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de Wall Street se encuentra cerrado actualmente, por lo que los precios de las acciones tradicionales están congelados. Las criptomonedas operan 24/7 y muestran un sesgo alcista moderado de corto plazo, con SOL-USD y ETH-USD acercándose a zonas de sobrecompra en el RSI de 1 hora tras rebotar desde soportes diarios. El portafolio mantiene posiciones en MSFT, QQQ y NVDA con rendimientos estables pero a la espera de la apertura de los mercados bursátiles para buscar objetivos de take-profit cercanos al +2.0% o aplicar stop-loss en caso de reversiones adversas."

**Operaciones del ciclo:**
- **[HOLD] MSFT** (Confianza: 70%): La posición en MSFT muestra una ganancia controlada del 0.8% con mercado cerrado. Se mantiene en espera de la apertura bursátil para buscar el objetivo de take-profit.
- **[HOLD] QQQ** (Confianza: 70%): QQQ se mantiene en cartera con ganancias mínimas mientras el mercado está cerrado. Se espera la apertura para evaluar la continuación del rebote técnico.
- **[HOLD] NVDA** (Confianza: 65%): NVDA opera con ligera pérdida controlada y mercado cerrado. Se mantiene la posición a la espera de la apertura para evaluar su soporte crítico o buscar salida si falla el momentum.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear la apertura de Wall Street para buscar take-profit en MSFT, QQQ y NVDA si alcanzan ganancias entre +2.0% y +3.5%. Vigilar el comportamiento de las criptomonedas (SOL-USD y ETH-USD) ante posibles correcciones técnicas para nuevas entradas de rebote. Mantener la disciplina de liquidez y rotar capital estancado si surge un momentum más fuerte en activos abiertos."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **58** | 🎯 **41.4%** (24W / 20L / 14BE) | 🔴 **$-1.22 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-15 16:20` | 🔴 SELL (-0.10$) | `AAPL` | $9.90 | $342.86 | AAPL lleva más de un día abierta (1d 5h) sin mostrar un momentum significativo ni alcanzar... |
| `2026-10-15 12:50` | 🟢 BUY | `NVDA` | $8.00 | $217.32 | NVDA presenta un RSI de 1h en sobreventa extrema (21.5) con un inicio de recuperación en s... |
| `2026-10-15 12:20` | 🟢 BUY | `QQQ` | $10.00 | $725.09 | QQQ muestra un RSI de 1h en sobreventa extrema (28.7) cruzando al alza con un cambio posit... |
| `2026-10-15 12:10` | 🔴 SELL (+0.14$) | `ETH-USD` | $6.14 | $2417.73 | ETH-USD ha alcanzado un rendimiento del +2.33%, cumpliendo con el rango establecido para l... |
| `2026-10-15 11:50` | 🔴 SELL (+0.13$) | `SOL-USD` | $6.13 | $104.21 | SOL-USD ha alcanzado un rendimiento de +2.11%, cumpliendo con la regla de toma rápida de g... |

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
