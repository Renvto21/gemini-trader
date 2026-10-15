# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 05:31:00`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$11.61 USD** | **$26.96 USD** | **$38.57 USD** | 🔴 **-3.58%** ($-1.43) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 18h 40m |
| `BTC-USD` | 0.000061 | $81640.68 | $81199.52 | $4.97 | 📉 -0.54% | 8h 20m |
| `ETH-USD` | 0.002539 | $2362.71 | $2371.57 | $6.02 | 📈 +0.37% | 4h 20m |
| `SOL-USD` | 0.058789 | $102.06 | $102.98 | $6.05 | 📈 +0.90% | 2h 10m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que la liquidez activa se concentra en las criptomonedas (BTC-USD, ETH-USD, SOL-USD). A pesar de un sesgo bajista general en el gráfico diario, nuestras posiciones recientes muestran ligeras ganancias y se mantienen estables dentro de los rangos operativos esperados. No hay activación de take-profit todavía, ya que las ganancias están por debajo del rango óptimo de +2.0% a +3.5%, y los stop-losses se mantienen seguros."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD muestra un rendimiento positivo de +0.37% tras el rebote reciente. Se mantiene la posición en espera de alcanzar el objetivo de take-profit de +2.0% o un RSI de 1h en zona de sobrecompra (>70).

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en AAPL, BTC-USD, ETH-USD y SOL-USD. Monitorear de cerca ETH-USD y SOL-USD para asegurar ganancias parciales o totales si alcanzan el objetivo de +2.0% a +3.5%. Proteger la posición con stop-loss estricto a -2.0% en caso de pérdida de soporte. Mantener la disciplina con la reserva mínima de efectivo."
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
