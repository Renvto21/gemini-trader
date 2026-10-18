# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 01:40:43`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.31 USD** | **$38.36 USD** | 🔴 **-4.10%** ($-1.64) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81730.00 | $10.07 | 📈 +0.69% | 6h 39m |
| `SOL-USD` | 0.097418 | $102.65 | $103.86 | $10.12 | 📈 +1.18% | 6h 29m |
| `ETH-USD` | 0.004193 | $2385.05 | $2415.44 | $10.13 | 📈 +1.27% | 6h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se mantiene operando 24/7 mientras los mercados tradicionales permanecen cerrados. Las posiciones actuales en BTC-USD, SOL-USD y ETH-USD muestran ligeras ganancias entre +0.69% y +1.27%, pero el impulso de corto plazo en 1H se ha moderado ligeramente con RSI de 1H estabilizándose por debajo de 60 y pequeños cambios negativos en la última hora. Dado que aún no alcanzan la meta de take-profit de +2.0% a +3.5%, mantenemos las posiciones bajo estrecha vigilancia mientras conservamos el efectivo disponible."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 75%): La posición muestra una ganancia actual de +0.69% tras casi 7 horas de tenencia. El RSI de 1H está en 55.9 y se mantiene dentro de los parámetros esperados de consolidación, por lo que se mantiene la posición en busca del objetivo de take-profit de +2.0%.
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD registra una ganancia del +1.18% con un RSI de 1H en 47.5. Aunque el cambio de la última hora es ligeramente negativo, el precio se mantiene estable y cerca de la zona objetivo para asegurar ganancias parciales o totales al llegar a +2%.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD presenta una ganancia de +1.27% y un RSI de 1H en 46.6. La posición avanza favorablemente desde el rebote inicial, por lo que se decide mantener para permitir que continúe hacia la meta de take-profit establecida.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Monitorear de cerca las posiciones abiertas (BTC-USD, SOL-USD, ETH-USD) buscando alcanzar el objetivo de take-profit entre +2.0% y +3.5% o una sobrecompra de RSI 1H > 70 para asegurar beneficios. Mantener los stop-loss estrictos por debajo de -2.0%. Si el momentum se desacelera por completo y no se logra el objetivo en los próximos ciclos, evaluar rotación de capital hacia nuevas oportunidades de rebote."
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
