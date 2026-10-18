# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 13:20:48`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.37 USD** | **$19.84 USD** | **$38.21 USD** | 🔴 **-4.47%** ($-1.79) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.097172 | $102.91 | $101.84 | $9.90 | 📉 -1.04% | 2h 19m |
| `ETH-USD` | 0.004205 | $2377.97 | $2364.72 | $9.94 | 📉 -0.56% | 1h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto mantiene una tendencia bajista de corto plazo pero opera en niveles de sobreventa diarios extremadamente profundos (RSI diario de SOL en 15.8 y ETH en 21.6). Los mercados tradicionales (Wall Street) se encuentran cerrados, por lo que toda la atención táctica se centra en gestionar las posiciones abiertas en criptomonedas buscando el rebote técnico por reversión a la media."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): La posición lleva poco tiempo abierta (2h 19m) con una pérdida leve de -1.04%. El RSI diario se encuentra en una sobreventa extrema (15.8), lo que sugiere un alto potencial de rebote técnico (Mean Reversion) en cuanto el impulso de corto plazo se torne positivo. Se mantiene la posición respetando el plan táctico.
- **[HOLD] ETH-USD** (Confianza: 75%): La posición en ETH-USD registra una pérdida menor de -0.56% con un holding time de 1h 19m. El contexto diario muestra un RSI en 21.6, indicando condiciones óptimas para un rebote inminente. Se mantiene la posición a la espera de la recuperación del impulso de 1 hora.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas de SOL-USD y ETH-USD ya que se encuentran en zonas de soporte macro (sobreventa extrema en gráficos diarios). Monitorear de cerca el RSI de 1 hora: si el RSI cruza por encima de 50-55 y las posiciones alcanzan una ganancia de +2.0% a +3.5%, ejecutar la toma de beneficios. Mantener estricto el stop-loss en -2.0% para proteger el capital ante cualquier extensión bajista adicional."
---

### 📈 Rendimiento Histórico & Estadísticas Quant

| Operaciones Cerradas | Tasa de Acierto (Win Rate) | Beneficio Realizado | Mejor Trade | Peor Trade |
| :---: | :---: | :---: | :---: | :---: |
| **70** | 🎯 **41.4%** (29W / 27L / 14BE) | 🔴 **$-1.49 USD** | 🏆 `+$0.56 (+2.8%) en SOL-USD` | 🛡️ `$-0.97 (-2.5%) en SOL-USD` |
---

### 📜 Últimos Movimientos

| Fecha | Acción | Activo | Monto | Precio | Motivo |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `2026-10-18 12:00` | 🟢 BUY | `ETH-USD` | $10.00 | $2377.97 | ETH-USD presenta un RSI diario extremadamente bajo en 22.0 y un RSI de 1 hora saliendo de ... |
| `2026-10-18 11:01` | 🟢 BUY | `SOL-USD` | $10.00 | $102.91 | SOL-USD muestra un RSI diario extremadamente bajo (16.4) en zona de sobreventa profunda y ... |
| `2026-10-18 08:00` | 🔴 SELL (+0.13$) | `ETH-USD` | $10.13 | $2415.11 | ETH-USD registra un RSI de 1H en 72.1 (sobrecompra) y una ganancia de +1.26%. Se procede a... |
| `2026-10-18 08:00` | 🔴 SELL (+0.12$) | `SOL-USD` | $10.12 | $103.84 | SOL-USD presenta un RSI de 1H en 67.6 acercándose a zona de sobrecompra con una ganancia d... |
| `2026-10-18 08:00` | 🔴 SELL (+0.10$) | `BTC-USD` | $10.08 | $81974.15 | BTC-USD ha alcanzado un RSI de 1H en 78.8 (sobrecompra profunda) tras el rebote esperado, ... |

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
