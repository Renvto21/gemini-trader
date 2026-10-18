# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 21:40:44`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.15 USD** | **$38.20 USD** | 🔴 **-4.50%** ($-1.80) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81389.69 | $10.03 | 📈 +0.27% | 2h 39m |
| `SOL-USD` | 0.097418 | $102.65 | $103.28 | $10.06 | 📈 +0.61% | 2h 29m |
| `ETH-USD` | 0.004193 | $2385.05 | $2400.44 | $10.06 | 📈 +0.65% | 2h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se encuentra abierto 24/7 con un sesgo lateral a bajista de corto plazo, donde BTC-USD, ETH-USD y SOL-USD muestran ligeros retrocesos en la última hora tras su intento inicial de rebote. Los mercados tradicionales están cerrados. Las posiciones actuales muestran ganancias muy modestas (entre +0.27% y +0.65%), aún por debajo del objetivo de take-profit del +2.0%. Mantendremos la paciencia y las posiciones abiertas mientras el RSI de 1H se mantenga en niveles constructivos sin romper soportes críticos."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 70%): La posición muestra un rendimiento positivo del +0.27% tras casi 2.5 horas abierta. El RSI de 1H está en 41.5 y no ha alcanzado el objetivo de take-profit del +2.0%, ni ha tocado el stop-loss. Mantenemos la posición esperando mayor expansión de volumen.
- **[HOLD] SOL-USD** (Confianza: 70%): La posición registra un beneficio actual de +0.61%. A pesar de una ligera contracción de 1H (-0.56%), se mantiene dentro del rango esperado de consolidación y lejos del stop-loss. Esperamos continuidad en el rebote técnico.
- **[HOLD] ETH-USD** (Confianza: 70%): ETH-USD mantiene una ganancia de +0.65%. El RSI de 1H está en 31.1, lo cual sugiere soporte continuo tras el rebote inicial. Sostenemos la posición buscando la zona del +2.0% para asegurar beneficios.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en BTC-USD, SOL-USD y ETH-USD. Monitorear de cerca el RSI de 1H y la evolución de los precios. Objetivo de take-profit entre +2.0% y +3.5% o RSI de 1H superior a 70. Stop-loss estricto en -2.0% o si el momentum decae bruscamente. Mantener la liquidez actual intacta hasta ver una confirmación de ruptura o un nuevo punto de entrada de alta convicción."
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
