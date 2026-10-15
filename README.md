# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 05:40:48`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$11.61 USD** | **$26.96 USD** | **$38.57 USD** | 🔴 **-3.57%** ($-1.43) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 18h 50m |
| `BTC-USD` | 0.000061 | $81640.68 | $81176.80 | $4.97 | 📉 -0.57% | 8h 30m |
| `ETH-USD` | 0.002539 | $2362.71 | $2372.13 | $6.02 | 📈 +0.40% | 4h 30m |
| `SOL-USD` | 0.058789 | $102.06 | $103.00 | $6.06 | 📈 +0.92% | 2h 20m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de Wall Street se encuentra cerrado, por lo que la liquidez y operativa se concentran exclusivamente en el mercado de criptomonedas abierto 24/7. Las criptomonedas principales (BTC, ETH, SOL) muestran una tendencia general bajista en el marco diario pero mantienen un comportamiento lateral a ligeramente recuperador en el corto plazo, con SOL y ETH registrando ligeras ganancias en nuestras posiciones actuales aunque sin el momentum explosivo esperado para tomar beneficios completos inmediatos."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 70%): La posición muestra un rendimiento positivo del 0.40% pero aún no alcanza el objetivo de take-profit de +2.0%. Se mantiene abierta para permitir que desarrolle mayor momentum alcista.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en AAPL, BTC-USD, ETH-USD y SOL-USD. Vigilar de cerca a ETH-USD y SOL-USD para asegurar ganancias parciales si alcanzan el objetivo de +2.0% a +3.5%. Proteger la posición de AAPL y BTC-USD con stop-loss estricto en -2.0% si rompen soportes. Mantener la disciplina con la reserva mínima de efectivo de $4.00 USD."
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
