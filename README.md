# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-15 08:10:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$11.61 USD** | **$26.86 USD** | **$38.47 USD** | 🔴 **-3.83%** ($-1.53) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | 0.028889 | $346.15 | $342.96 | $9.91 | 📉 -0.92% | 21h 20m |
| `BTC-USD` | 0.000061 | $81640.68 | $80822.82 | $4.95 | 📉 -1.00% | 11h 0m |
| `ETH-USD` | 0.002539 | $2362.71 | $2360.98 | $6.00 | 📉 -0.07% | 7h 0m |
| `SOL-USD` | 0.058789 | $102.06 | $102.14 | $6.00 | 📈 +0.08% | 4h 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, limitando la operativa al sector cripto (24/7). Las criptomonedas principales (BTC-USD, ETH-USD y SOL-USD) muestran consolidación tras caídas recientes, con los RSI de 1 hora recuperándose ligeramente de zonas de compresión pero sin un impulso alcista fuerte todavía. Mantenemos la cautela y conservamos las posiciones abiertas con estricto apego a los niveles de stop-loss y take-profit."

**Operaciones del ciclo:**
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD se mantiene estable con un PnL neutral (-0.07%) tras 7 horas abierto. El RSI de 1h se encuentra en 33.7, consolidando cerca de la zona de rebote esperada. Mantengo la posición esperando el impulso hacia el take-profit.
- **[HOLD] SOL-USD** (Confianza: 70%): SOL-USD muestra un comportamiento similar, operando con un PnL de 0.0% tras casi 5 horas. El RSI de 1h está en 36.3. Mantengo la posición a la espera de confirmación de tendencia.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener la vigilancia sobre ETH-USD y SOL-USD. Si ninguna de las dos rompe al alza hacia el objetivo de take-profit (+2% a +3.5%) o si por el contrario perforan los soportes amenazando el stop-loss del -2%, procederé a la venta inmediata. Mantener la liquidez actual intacta hasta la apertura de Wall Street, momento en el cual evaluaré la rotación de AAPL si no muestra fuerza alcista adicional."
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
