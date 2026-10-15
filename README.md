# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 08:20:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$11.61 USD** | **$26.86 USD** | **$38.47 USD** | 🔴 **-3.82%** ($-1.53) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 21h 30m |
| `BTC-USD` | 0.000061 | $81640.68 | $80906.78 | $4.96 | 📉 -0.90% | 11h 10m |
| `ETH-USD` | 0.002539 | $2362.71 | $2359.60 | $5.99 | 📉 -0.13% | 7h 10m |
| `SOL-USD` | 0.058789 | $102.06 | $102.16 | $6.01 | 📈 +0.10% | 5h 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un sentimiento predominantemente bajista en el corto plazo con la mayoría de los activos cotizando por debajo de su SMA20. Los activos de Wall Street se encuentran cerrados, por lo que toda la atención táctica se centra en los mercados de criptomonedas (BTC-USD, ETH-USD y SOL-USD), los cuales operan 24/7. Las criptomonedas muestran signos de consolidación tras las recientes caídas, con rebotes técnicos potenciales pero aún sin la fuerza suficiente para consolidar una tendencia alcista firme."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 65%): La posición en ETH-USD se mantiene estable con una pérdida marginal de -0.13% tras 7 horas de apertura. El RSI de 1h se sitúa en 33.4 y mantiene una estructura de compresión a la espera de un impulso alcista que active la zona de beneficios.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales en AAPL, BTC-USD, ETH-USD y SOL-USD ya que se encuentran dentro de rangos tolerables de pérdida sin romper soportes críticos. Monitorearemos de cerca el comportamiento de ETH-USD y SOL-USD en busca de un aumento en el volumen y un RSI de 1h superior a 50 que confirme el take-profit entre +2.0% y +3.5%. Si alguna posición perfora el -2.0%, procederemos a la ejecución del stop-loss para proteger el capital. La liquidez en efectivo se mantiene en reserva para futuras oportunidades ante la apertura de los mercados tradicionales."
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
