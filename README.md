# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 10:30:48`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.17 USD** | **$34.51 USD** | **$38.67 USD** | 🔴 **-3.31%** ($-1.33) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $541.72 | $6.58 | 📈 +1.22% | 23h 40m |
| `QQQ` | 0.013791 | $725.09 | $725.04 | $10.00 | 📉 -0.01% | 22h 10m |
| `NVDA` | 0.036812 | $217.32 | $215.52 | $7.93 | 📉 -0.83% | 21h 40m |
| `ETH-USD` | 0.002855 | $2451.90 | $2459.25 | $7.02 | 📈 +0.30% | 5h 59m |
| `SOL-USD` | 0.028214 | $106.33 | $105.40 | $2.97 | 📉 -0.87% | 5h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado muestra un comportamiento mixto con Wall Street abierto. Las acciones tecnológicas como NVDA y QQQ presentan debilidad a corto plazo, destacando el RSI de 1 hora de NVDA en 21.2 (sobreventa extrema). Las criptomonedas se mantienen estables con un sesgo lateral tras las últimas correcciones. Nuestro portafolio se mantiene disciplinado gestionando de cerca las posiciones vigentes."

**Operaciones del ciclo:**
- **[HOLD] MSFT** (Confianza: 80%): MSFT muestra un rendimiento positivo constante (+1.22%) con tendencia alcista sólida sobre la SMA20 y un RSI diario elevado. Mantenemos la posición para capturar una mayor expansión hacia el objetivo de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales de MSFT, QQQ, NVDA, ETH-USD y SOL-USD ya que ninguna ha alcanzado el stop-loss estricto de -2.0% ni el take-profit del rango +2.0% a +3.5%. Vigilaré de cerca a MSFT para asegurar beneficios si se acerca al objetivo superior, y estaré atento a NVDA dado su RSI de 1h en sobreventa extrema para evaluar un posible rebalanceo si el momentum se invierte."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **58** | 🎯 **41.4%** (24W / 20L / 14BE) | 🔴 **$-1.22 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-16 05:10` | 🟢 BUY | `SOL-USD` | $3.00 | $106.33 | SOL-USD presenta un RSI diario en zona de sobreventa extrema (29.0) y un cambio positivo e... |
| `2026-10-16 04:30` | 🟢 BUY | `ETH-USD` | $7.00 | $2451.90 | Aprovechamos la liquidez disponible sobre la reserva mínima ($14.17 vs $4.00 requeridos) p... |
| `2026-10-15 16:20` | 🔴 SELL (-0.10$) | `AAPL` | $9.90 | $342.86 | AAPL lleva más de un día abierta (1d 5h) sin mostrar un momentum significativo ni alcanzar... |
| `2026-10-15 12:50` | 🟢 BUY | `NVDA` | $8.00 | $217.32 | NVDA presenta un RSI de 1h en sobreventa extrema (21.5) con un inicio de recuperación en s... |
| `2026-10-15 12:20` | 🟢 BUY | `QQQ` | $10.00 | $725.09 | QQQ muestra un RSI de 1h en sobreventa extrema (28.7) cruzando al alza con un cambio posit... |

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
