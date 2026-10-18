# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 11:30:41`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$28.37 USD** | **$9.93 USD** | **$38.30 USD** | 🔴 **-4.25%** ($-1.70) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.097172 | $102.91 | $102.18 | $9.93 | 📉 -0.71% | 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado accionario se encuentra cerrado durante el fin de semana, por lo que toda la liquidez y atención operativa se concentran en las criptomonedas (ABIERTO 24/7). Los activos digitales muestran un sesgo bajista moderado de corto plazo, pero presentan indicadores de RSI diario extremadamente deprimidos que sugieren oportunidades de reversión a la media (mean reversion)."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 80%): La posición en SOL-USD lleva un tiempo corto abierta (29 minutos) con una pérdida menor de -0.71%. El contexto de sobreventa profunda en el RSI diario (16.0) respalda mantener la tesis de rebote técnico. No se ha alcanzado el stop-loss del -2.0% ni el objetivo de take-profit, por lo que se mantiene la operación.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantengo la posición en SOL-USD con una leve pérdida actual de -0.71% tras 29 minutos. El RSI diario está profundamente sobrevendido en 16.0 y el RSI de 1H en 39.3. Mantendré el stop-loss estricto en -2.0% y buscaré un take-profit entre +2.0% y +3.5% en cuanto el impulso de 1H se torne alcista y supere los 55 puntos. En cuanto a ETH-USD, el RSI diario está en 22.0 y el RSI de 1H en 36.4, aproximándose a una zona ideal para considerar una entrada si muestra confirmación de giro."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **70** | 🎯 **41.4%** (29W / 27L / 14BE) | 🔴 **$-1.49 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-18 11:01` | 🟢 BUY | `SOL-USD` | $10.00 | $102.91 | SOL-USD muestra un RSI diario extremadamente bajo (16.4) en zona de sobreventa profunda y ... |
| `2026-10-18 08:00` | 🔴 SELL (+0.13$) | `ETH-USD` | $10.13 | $2415.11 | ETH-USD registra un RSI de 1H en 72.1 (sobrecompra) y una ganancia de +1.26%. Se procede a... |
| `2026-10-18 08:00` | 🔴 SELL (+0.12$) | `SOL-USD` | $10.12 | $103.84 | SOL-USD presenta un RSI de 1H en 67.6 acercándose a zona de sobrecompra con una ganancia d... |
| `2026-10-18 08:00` | 🔴 SELL (+0.10$) | `BTC-USD` | $10.08 | $81974.15 | BTC-USD ha alcanzado un RSI de 1H en 78.8 (sobrecompra profunda) tras el rebote esperado, ... |
| `2026-10-17 19:10` | 🟢 BUY | `ETH-USD` | $10.00 | $2385.05 | ETH-USD muestra un RSI de 1H en 29.0 (sobreventa profunda) combinado con un cambio de 1h p... |

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
