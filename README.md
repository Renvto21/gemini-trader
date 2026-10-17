# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 19:50:42`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.12 USD** | **$38.16 USD** | 🔴 **-4.59%** ($-1.84) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81343.83 | $10.02 | 📈 +0.21% | 49m |
| `SOL-USD` | 0.097418 | $102.65 | $103.19 | $10.05 | 📈 +0.53% | 39m |
| `ETH-USD` | 0.004193 | $2385.05 | $2395.17 | $10.04 | 📈 +0.42% | 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado accionario tradicional (SPY, QQQ, NVDA, AAPL, MSFT) se encuentra cerrado, por lo que toda la actividad se concentra en el mercado de criptomonedas (BTC-USD, ETH-USD, SOL-USD), que opera 24/7. Las posiciones actuales muestran ligeras recuperaciones con un P&L positivo menor al +1.0% (BTC-USD +0.21%, SOL-USD +0.53%, ETH-USD +0.42%). Los indicadores RSI de 1 hora se mantienen en rangos estables sin alcanzar aún la zona de sobrecompra (>70) para la toma de ganancias, y ninguna posición ha activado el stop-loss de -2.0%. El momentum inicial de rebote continúa su curso con cambios de 1 hora positivos en todos los criptoactivos en cartera."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): La posición muestra un rendimiento positivo de +0.21% y un RSI de 1H en 43.2. El rebote técnico continúa en desarrollo y aún no alcanza el objetivo de take-profit ni activa el stop-loss.
- **[HOLD] SOL-USD** (Confianza: 80%): La posición registra una ganancia de +0.53% con un RSI de 1H en 37.0 y un cambio positivo de 1H de 1.03%. Se mantiene para buscar el objetivo de take-profit.
- **[HOLD] ETH-USD** (Confianza: 80%): La posición se mantiene estable con un P&L de +0.42% y un RSI de 1H en 34.8. El precio respeta el soporte y continúa el movimiento alcista de corto plazo.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales (BTC-USD, SOL-USD, ETH-USD) a la espera de que alcancen el objetivo de take-profit entre +2.0% y +3.5% o que el RSI de 1H cruce hacia sobrecompra (>70). El stop-loss se mantiene estricto en -2.0% para proteger el capital. No se realizan nuevas compras en este ciclo debido a que la liquidez disponible es baja y se prioriza vigilar la evolución de las posiciones abiertas."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **67** | 🎯 **38.8%** (26W / 27L / 14BE) | 🔴 **$-1.84 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-17 19:10` | 🟢 BUY | `ETH-USD` | $10.00 | $2385.05 | ETH-USD muestra un RSI de 1H en 29.0 (sobreventa profunda) combinado con un cambio de 1h p... |
| `2026-10-17 19:10` | 🟢 BUY | `SOL-USD` | $10.00 | $102.65 | SOL-USD presenta un RSI de 1H en 31.5 saliendo de zona de sobreventa estricta y un cambio ... |
| `2026-10-17 19:00` | 🟢 BUY | `BTC-USD` | $10.00 | $81170.65 | BTC-USD muestra un RSI de 1H saliendo de niveles bajos (37.5) con un cambio positivo de 0.... |
| `2026-10-17 18:40` | 🔴 SELL (-0.22$) | `ETH-USD` | $9.78 | $2370.09 | La posición acumula una pérdida de -2.21%, excediendo el umbral de stop-loss del -2.0%. El... |
| `2026-10-17 18:40` | 🔴 SELL (-0.21$) | `SOL-USD` | $9.79 | $101.78 | La posición ha alcanzado una pérdida de -2.08%, rompiendo el límite de stop-loss estricto ... |

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
