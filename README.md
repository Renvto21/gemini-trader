# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 01:10:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.38 USD** | **$38.42 USD** | 🔴 **-3.94%** ($-1.58) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81797.73 | $10.08 | 📈 +0.77% | 6h 9m |
| `SOL-USD` | 0.097418 | $102.65 | $104.21 | $10.15 | 📈 +1.52% | 5h 59m |
| `ETH-USD` | 0.004193 | $2385.05 | $2420.18 | $10.15 | 📈 +1.47% | 5h 59m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se encuentra activo 24/7 mientras que los mercados tradicionales están cerrados. Las posiciones actuales en BTC-USD, SOL-USD y ETH-USD muestran ganancias moderadas (entre +0.77% y +1.52%), acercándose gradualmente al objetivo de take-profit sin alcanzar aún el umbral crítico de sobrecompra en RSI de 1H (>70). Mantenemos las posiciones abiertas para permitir que el momentum continúe su desarrollo."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): La posición mantiene un rendimiento positivo de +0.77% y un RSI de 1H en 57.7, operando dentro del rango esperado para buscar el objetivo de take-profit.
- **[HOLD] SOL-USD** (Confianza: 80%): La posición muestra una ganancia de +1.52%, acercándose adecuadamente a nuestra meta de take-profit sin señales de agotamiento inmediato en el RSI de 1H.
- **[HOLD] ETH-USD** (Confianza: 80%): La posición registra un beneficio de +1.47% con un RSI de 1H en 48.3, consolidando el rebote técnico esperado desde la zona de sobreventa previa.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en BTC-USD, SOL-USD y ETH-USD. Monitorear los indicadores de 1H y vigilar si alguna posición alcanza el objetivo de take-profit (+2.0% a +3.5%) o si el RSI de 1H cruza 70 para asegurar ganancias en efectivo. Si el impulso se debilita o lateraliza sin alcanzar el objetivo, considerar la rotación de capital en el siguiente ciclo."
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
