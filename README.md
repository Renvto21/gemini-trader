# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 08:40:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$11.61 USD** | **$26.92 USD** | **$38.53 USD** | 🔴 **-3.68%** ($-1.47) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 21h 50m |
| `BTC-USD` | 0.000061 | $81640.68 | $81079.54 | $4.97 | 📉 -0.69% | 11h 30m |
| `ETH-USD` | 0.002539 | $2362.71 | $2367.43 | $6.01 | 📈 +0.20% | 7h 30m |
| `SOL-USD` | 0.058789 | $102.06 | $102.60 | $6.03 | 📈 +0.53% | 5h 20m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene abierto 24/7 con ligeros intentos de recuperación en SOL-USD y ETH-USD, mientras que los activos tradicionales de Wall Street permanecen cerrados. El portafolio muestra una ligera recuperación en las posiciones abiertas de criptomonedas, con ganancias pequeñas pero estables. Mantendremos la disciplina operativa, dejando que las criptomonedas capturen el impulso actual y protegiendo el capital ante cualquier giro negativo."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD muestra un comportamiento estable con una pequeña ganancia del 0.2% y un RSI de 1h en recuperación. Mantenemos la posición para buscar el objetivo de take-profit entre +2.0% y +3.5%.
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD presenta un avance positivo del 0.53% con un RSI de 1h subiendo hacia 39.1. Se mantiene en cartera esperando la extensión del rebote técnico.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear de cerca ETH-USD y SOL-USD en busca de un aumento en el RSI de 1h por encima de 50 para asegurar beneficios parciales entre el +2.0% y +3.5%. Mantener los stop-loss estrictos al -2.0% en todas las posiciones abiertas y preservar la liquidez mínima requerida. No se ejecutarán nuevas compras en este ciclo debido a que los mercados tradicionales están cerrados y la liquidez se concentra en optimizar las posiciones actuales."
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
