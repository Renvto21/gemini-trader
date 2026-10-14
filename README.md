# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-13 22:00:51`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$28.54 USD** | **$11.01 USD** | **$39.55 USD** | 🔴 **-1.12%** ($-0.45) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `ETH-USD` | 0.001993 | $2508.37 | $2505.59 | $4.99 | 📉 -0.11% | 4h 50m |
| `BTC-USD` | 0.000072 | $83128.62 | $83362.17 | $6.02 | 📈 +0.28% | 1h 0m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se mantiene abierto y operando en un rango estable con sesgo ligeramente positivo en 24 horas. BTC-USD y ETH-USD muestran signos de estabilización tras haber rebotado desde zonas de sobreventa previas, con RSI de 1 hora ubicándose en niveles neutrales saludables alrededor de 53-55. Los mercados tradicionales de Wall Street se encuentran cerrados, por lo que toda la atención táctica se centra en la gestión de las posiciones actuales en cripto."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 75%): BTC-USD se encuentra operando de manera estable con una pequeña ganancia del 0.28%. El RSI de 1h se sitúa en 53.0 y el cambio en 24h es positivo (+1.96%). Mantenemos la posición a la espera de que alcance el objetivo de take-profit del 2.0% al 3.5%.
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD muestra un rendimiento plano (-0.11%) tras casi 5 horas de holding. El RSI de 1h ha subido a 55.7 y el cambio de 24h es positivo (+2.51%). Mantenemos la posición ya que mantiene el impulso esperado hacia el objetivo de take-profit sin activar los límites de stop-loss.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones abiertas de BTC-USD y ETH-USD mientras evolucionan hacia nuestro objetivo de take-profit (+2.0% a +3.5%) o un RSI de 1H superior a 70. El stop-loss se mantiene estricto en -2.0% para proteger el capital. Preservaremos la liquidez actual por encima de $4.00 USD y evaluaremos la entrada en SOL-USD si su RSI diario de 28.1 confirma un rebote técnico más claro en el corto plazo."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **48** | 🎯 **45.8%** (22W / 12L / 14BE) | 🔴 **$-0.38 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-13 21:00` | 🟢 BUY | `BTC-USD` | $6.00 | $83128.62 | BTC-USD muestra un RSI de 1H en 31.7 aproximándose a niveles de sobreventa y un cambio pos... |
| `2026-10-13 19:40` | 🔴 SELL (-0.10$) | `SOL-USD` | $29.86 | $106.84 | SOL-USD lleva más de 5 horas de holding sin mostrar el rebote esperado, operando bajo la S... |
| `2026-10-13 17:10` | 🟢 BUY | `ETH-USD` | $5.00 | $2508.37 | ETH-USD se encuentra en zona de sobreventa técnica con un RSI de 35.9 y un cambio positivo... |
| `2026-10-13 17:00` | 🔴 SELL | `ETH-USD` | $9.67 | $2506.14 | ETH-USD ha registrado un rebote diario del 2.53% acercándose a una zona de neutralidad a c... |
| `2026-10-13 16:30` | 🟢 BUY | `ETH-USD` | $9.68 | $2507.92 | ETH-USD muestra un RSI de 35.8 en zona de fuerte sobreventa y un impulso alcista diario de... |

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
