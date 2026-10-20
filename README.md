# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-20 05:30:48`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$0.00 USD** | **$38.47 USD** | **$38.47 USD** | 🔴 **-3.83%** ($-1.53) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `QQQ` | 0.013910 | $718.92 | $718.36 | $9.99 | 📉 -0.08% | 18h 50m |
| `ETH-USD` | 0.004178 | $2393.62 | $2381.92 | $9.95 | 📉 -0.49% | 16h 39m |
| `SOL-USD` | 0.096034 | $104.13 | $104.10 | $10.00 | 📉 -0.03% | 12h 50m |
| `BTC-USD` | 0.000105 | $81767.70 | $81388.75 | $8.53 | 📉 -0.46% | 12h 20m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de valores tradicional se encuentra cerrado, por lo que toda la actividad se concentra en los criptoactivos (abiertos 24/7). Las criptomonedas muestran un comportamiento lateral a ligeramente bajista en el corto plazo (cambios de 1 hora negativos), pero con indicadores de RSI diario en niveles de sobreventa profunda, manteniendo viva la tesis de un rebote técnico inminente. El portafolio actual se encuentra completamente invertido y con un PnL global ligeramente negativo (-3.83%), manteniéndose seguro dentro de los límites de riesgo sin haber tocado los stop-loss del -2.0%."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD muestra un RSI diario extremadamente bajo (21.2) que respalda la tesis de sobreventa y posible rebote, manteniendo una pérdida marginal de -0.03%. Mantenemos la posición a la espera de un impulso alcista que active el take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantendremos las posiciones actuales (QQQ, ETH-USD, SOL-USD, BTC-USD) ya que ninguna ha alcanzado el stop-loss del -2.0% ni el take-profit. Dado que el efectivo disponible es de $0.0 USD y la liquidez requerida es mínima, no realizaremos nuevas compras en este ciclo. Para el próximo ciclo, vigilaré de cerca el comportamiento de SOL-USD y ETH-USD: si el RSI de 1 hora supera los 60 con volumen incremental, buscaré realizar tomas parciales de beneficios; si alguna posición perfora los soportes y se acerca a una pérdida del -2.0%, procederé a vender inmediatamente para proteger el capital."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **77** | 🎯 **42.9%** (33W / 29L / 15BE) | 🔴 **$-1.29 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-19 23:00` | 🟢 BUY | `BTC-USD` | $4.00 | $81646.39 | BTC-USD presenta un RSI de 1 hora en 27.7, nivel de sobreventa profunda ideal para un rebo... |
| `2026-10-19 17:10` | 🟢 BUY | `BTC-USD` | $4.57 | $81874.05 | BTC-USD muestra señales de rebote técnico con un RSI de 1 hora en 31.1 recuperándose y un ... |
| `2026-10-19 16:40` | 🟢 BUY | `SOL-USD` | $10.00 | $104.13 | SOL-USD presenta un RSI diario extremo de 19.7, indicando condiciones de sobreventa profun... |
| `2026-10-19 12:51` | 🟢 BUY | `ETH-USD` | $10.00 | $2393.62 | ETH-USD presenta un RSI de 1 hora en 34.6, entrando en zona de sobreventa de corto plazo, ... |
| `2026-10-19 10:40` | 🟢 BUY | `QQQ` | $10.00 | $718.92 | QQQ muestra un fuerte momentum intradiario con un cambio de 1h del +1.28%, liderando el re... |

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
