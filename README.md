# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 06:30:50`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$11.61 USD** | **$26.94 USD** | **$38.55 USD** | 🔴 **-3.63%** ($-1.45) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 19h 40m |
| `BTC-USD` | 0.000061 | $81640.68 | $81148.18 | $4.97 | 📉 -0.60% | 9h 20m |
| `ETH-USD` | 0.002539 | $2362.71 | $2367.87 | $6.01 | 📈 +0.22% | 5h 20m |
| `SOL-USD` | 0.058789 | $102.06 | $102.84 | $6.05 | 📈 +0.76% | 3h 10m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene operando 24/7 con una ligera consolidación bajista, mientras que los activos tradicionales de Wall Street permanecen cerrados. Nuestras posiciones en ETH-USD y SOL-USD muestran ligeras ganancias marginales, pero el momentum se ha desacelerado levemente. Mantenemos la disciplina táctica sin forzar salidas anticipadas dado que las pérdidas están controladas y no se ha alcanzado ningún stop-loss, pero vigilamos de cerca los niveles de RSI y la evolución del precio."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD muestra una ganancia leve del +0.22% y se mantiene operando dentro de la zona esperada tras salir de sobreventa. No hay motivos para vender aún, mantenemos la posición buscando el objetivo de take-profit del +2%.
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD registra un rendimiento positivo de +0.76% con un RSI de 1h recuperándose. Mantenemos la posición para capturar el rebote técnico hacia la zona objetivo de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear activamente las posiciones abiertas en ETH-USD y SOL-USD para asegurar beneficios si alcanzan el rango objetivo de +2.0% a +3.5%. El stop-loss se mantiene estricto en -2.0% para proteger el capital. Mantener liquidez en reserva y esperar la apertura de los mercados bursátiles tradicionales para evaluar oportunidades en tech (AAPL, NVDA)."
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
