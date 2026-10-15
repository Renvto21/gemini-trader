# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 05:50:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$11.61 USD** | **$26.96 USD** | **$38.58 USD** | 🔴 **-3.56%** ($-1.42) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 19h 0m |
| `BTC-USD` | 0.000061 | $81640.68 | $81199.00 | $4.97 | 📉 -0.54% | 8h 40m |
| `ETH-USD` | 0.002539 | $2362.71 | $2370.65 | $6.02 | 📈 +0.34% | 4h 40m |
| `SOL-USD` | 0.058789 | $102.06 | $103.12 | $6.06 | 📈 +1.04% | 2h 30m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene operando 24/7 con un sesgo bajista generalizado en temporalidades diarias, aunque con oportunidades de rebote técnico de corto plazo. Los mercados tradicionales permanecen cerrados. Las posiciones en ETH-USD y SOL-USD muestran ligeras ganancias (+0.34% y +1.04% respectivamente), mientras que AAPL y BTC-USD registran retrocesos menores dentro del rango de tolerancia y con stop-loss protegido. Mantenemos la disciplina táctica sin realizar ventas prematuras ya que no se alcanzan aún los objetivos estrictos de take-profit ni se activan los stops."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición en SOL-USD presenta una ganancia de +1.04%, aproximándose al objetivo de take-profit. Se mantiene la posición a la espera de un impulso adicional de corto plazo para asegurar beneficios.
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD muestra estabilidad con una ligera ganancia de +0.34%. Esperando mayor momentum alcista intradía para buscar la toma de ganancias.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear de cerca a SOL-USD y ETH-USD para asegurar ganancias parciales o totales si alcanzan el rango objetivo de +2.0% a +3.5%. Mantener estricto control de stop-loss en -2.0% para AAPL y BTC-USD. Preservar la liquidez en efectivo respetando la reserva mínima operativa."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **54** | 🎯 **40.7%** (22W / 18L / 14BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-15 03:20` | 🟢 BUY | `SOL-USD` | $6.00 | $102.06 | SOL-USD muestra un RSI de 1h en 33.3 saliendo de zonas de compresión bajista, acompañado d... |
| `2026-10-15 01:10` | 🟢 BUY | `ETH-USD` | $6.00 | $2362.71 | ETH-USD presenta un RSI de 1h extremadamente bajo en 23.5 saliendo de sobreventa y un camb... |
| `2026-10-14 23:30` | 🔴 SELL (-0.30$) | `SOL-USD` | $9.70 | $101.32 | La posición en SOL-USD acumula una pérdida de -2.95%, acercándose al límite crítico y sin ... |
| `2026-10-14 23:30` | 🔴 SELL (-0.32$) | `ETH-USD` | $9.68 | $2340.86 | 🚨 STOP-LOSS AUTOMÁTICO (CIRCUIT BREAKER): Pérdida de -3.20% superó el límite de seguridad ... |
| `2026-10-14 21:10` | 🟢 BUY | `BTC-USD` | $5.00 | $81640.68 | BTC-USD presenta un RSI de 1h en 24.9 (sobreventa extrema) y liquidez disponible suficient... |

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
