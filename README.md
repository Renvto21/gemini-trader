# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 11:11:05`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$28.37 USD** | **$9.96 USD** | **$38.33 USD** | 🔴 **-4.17%** ($-1.67) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.097172 | $102.91 | $102.49 | $9.96 | 📉 -0.41% | 10m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "Los mercados tradicionales se encuentran cerrados durante el fin de semana, por lo que toda la actividad se concentra en los criptoactivos (abiertos 24/7). Los principales criptoactivos (BTC-USD, ETH-USD y SOL-USD) muestran una tendencia bajista de corto plazo por debajo de su SMA20, pero con indicadores de RSI diario extremadamente deprimidos (como el RSI diario de SOL en 16.2), lo que anticipa un potencial rebote por sobreventa extrema (mean reversion) en cuanto el impulso de 1 hora se torne positivo."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición en SOL-USD fue abierta recientemente (hace 10 minutos) con una ligera contracción temporal (-0.41%). El RSI diario está en niveles de sobreventa extrema (16.2), lo que respalda la tesis de rebote técnico. Dado que aún no se alcanza el stop-loss del -2.0% ni el objetivo de take-profit, se mantiene la posición para permitir que el momentum se desarrolle.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantengo mi posición actual en SOL-USD con una pérdida leve de -0.41% tras apenas 10 minutos de haber sido abierta. El RSI de 1 hora se sitúa en 41.7 y el cambio en 1 hora es ligeramente negativo (-0.31%), lo que indica que aún estamos consolidando la base del movimiento. Mantendré el stop-loss estricto a -2.0% y buscaré un take-profit rápido entre +2.0% y +3.5% en cuanto el RSI de 1 hora cruce por encima de 55 con volumen alcista. El efectivo restante se mantiene en reserva a la espera de una confirmación similar en ETH-USD."
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
