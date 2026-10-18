# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 12:10:34`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$18.37 USD** | **$19.93 USD** | **$38.30 USD** | 🔴 **-4.26%** ($-1.70) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `SOL-USD` | 0.097172 | $102.91 | $102.17 | $9.93 | 📉 -0.72% | 1h 9m |
| `ETH-USD` | 0.004205 | $2377.97 | $2377.36 | $10.00 | 📉 -0.03% | 9m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se encuentra abierto con un sesgo bajista generalizado pero mostrando indicios de consolidación y primeros intentos de rebote en marcos de tiempo de 1 hora. Los mercados tradicionales permanecen cerrados. SOL-USD y ETH-USD mantienen un RSI diario profundamente deprimido, lo que justifica sostener las posiciones actuales mientras muestran un momentum positivo incipiente en 1 hora."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 70%): La posición lleva poco más de una hora abierta con una pérdida marginal de -0.72%. El RSI diario está extremadamente bajo (16.0) y el RSI de 1 hora muestra estabilidad en 37.7 con cambio positivo, por lo que se mantiene buscando el rebote.
- **[HOLD] ETH-USD** (Confianza: 70%): La posición en ETH-USD fue abierta recientemente. Presenta un RSI diario en 22.0 y un RSI de 1 hora en 36.3 con un ligero cambio positivo de 0.13%, cumpliendo con la tesis de mean reversion por sobreventa.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantengo SOL-USD y ETH-USD esperando el desarrollo del rebote técnico. El objetivo de take-profit se mantiene entre +2.0% y +3.5% o salida si el RSI de 1 hora supera los 55-60 puntos. El stop-loss se mantiene estricto en -2.0% para proteger el capital. Mantendré la liquidez actual intacta hasta ver una confirmación más clara del impulso alcista."
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
