# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 01:30:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.36 USD** | **$38.40 USD** | 🔴 **-3.99%** ($-1.60) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81802.67 | $10.08 | 📈 +0.78% | 6h 29m |
| `SOL-USD` | 0.097418 | $102.65 | $104.06 | $10.14 | 📈 +1.37% | 6h 19m |
| `ETH-USD` | 0.004193 | $2385.05 | $2418.76 | $10.14 | 📈 +1.41% | 6h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se mantiene abierto y operando con un sesgo lateral a ligeramente alcista tras el rebote inicial. Nuestras posiciones en BTC-USD, SOL-USD y ETH-USD muestran ganancias moderadas entre 0.78% y 1.41%, acercándose a la zona de objetivo pero sin alcanzar aún el umbral de take-profit óptimo (+2.0% a +3.5%) o sobrecompra en RSI de 1H (>70). Los mercados tradicionales permanecen cerrados. Mantendremos el enfoque en las criptomonedas y dejaremos correr las posiciones actuales mientras mantengan el impulso."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 75%): La posición muestra un rendimiento positivo de 0.78% y un RSI de 1H en 57.9. Aún no alcanza el objetivo de take-profit de +2.0% a +3.5%, por lo que mantenemos para permitir un mayor recorrido alcista.
- **[HOLD] SOL-USD** (Confianza: 75%): La posición se encuentra con una ganancia del 1.37% y un RSI de 1H en 48.9. El impulso se mantiene estable y esperamos a que alcance la zona de toma de beneficios.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD registra una ganancia del 1.41% con un RSI de 1H en 47.8. La posición sigue bajo control táctico sin señales de reversión bajista inmediata.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en BTC-USD, SOL-USD y ETH-USD durante este ciclo. Continuar vigilando los indicadores de 1H y el RSI de corto plazo. Si alguna posición alcanza una ganancia entre +2.0% y +3.5%, o el RSI de 1H supera 70, procederemos a vender para asegurar beneficios y acumular efectivo. No se detectan nuevas oportunidades de entrada con alta convicción en este momento, por lo que priorizamos la gestión de riesgo de las posiciones abiertas."
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
