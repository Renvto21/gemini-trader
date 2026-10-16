# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-16 10:40:59`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$4.17 USD** | **$34.40 USD** | **$38.56 USD** | 🔴 **-3.59%** ($-1.44) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `MSFT` | 0.012146 | $535.17 | $535.80 | $6.51 | 📈 +0.12% | 23h 50m |
| `QQQ` | 0.013791 | $725.09 | $722.34 | $9.96 | 📉 -0.38% | 22h 20m |
| `NVDA` | 0.036812 | $217.32 | $215.65 | $7.94 | 📉 -0.77% | 21h 50m |
| `ETH-USD` | 0.002855 | $2451.90 | $2457.89 | $7.02 | 📈 +0.24% | 6h 9m |
| `SOL-USD` | 0.028214 | $106.33 | $105.28 | $2.97 | 📉 -0.99% | 5h 30m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado accionario muestra una tendencia general de debilidad con varios índices y tecnológicas operando bajo su SMA20, destacando caídas moderadas en QQQ y NVDA. Las criptomonedas se mantienen operativas 24/7 con un comportamiento lateral a ligeramente bajista, aunque con indicadores de sobreventa diarios interesantes en activos como SOL-USD y ETH-USD. La liquidez actual se encuentra casi totalmente invertida cumpliendo con la regla de mantener el mínimo de efectivo."

**Operaciones del ciclo:**
- **[HOLD] NVDA** (Confianza: 75%): La posición se encuentra con una pérdida leve (-0.77%) y un RSI de 1h extremadamente bajo (21.4), lo que sugiere un posible rebote inminente por mean reversion. Mantenemos la posición vigilando de cerca el stop-loss.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales de MSFT, QQQ, NVDA, ETH-USD y SOL-USD ya que ninguna ha alcanzado el stop-loss estricto de -2.0% ni el take-profit del rango +2.0% a +3.5%. NVDA presenta un RSI de 1h en sobreventa extrema (21.4), por lo que evaluaremos su rebote en el próximo ciclo; si el momentum sigue sin reaccionar o se profundiza la pérdida hacia el -2.0%, ejecutaremos la venta para proteger capital."
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
