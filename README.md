# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 23:30:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.25 USD** | **$38.29 USD** | 🔴 **-4.26%** ($-1.71) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81607.57 | $10.05 | 📈 +0.54% | 4h 29m |
| `SOL-USD` | 0.097418 | $102.65 | $103.63 | $10.10 | 📈 +0.95% | 4h 19m |
| `ETH-USD` | 0.004193 | $2385.05 | $2408.54 | $10.10 | 📈 +0.98% | 4h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene abierto y operando con estabilidad moderada. Las posiciones actuales muestran ganancias acumuladas cercanas al 1% pero aún no alcanzan el objetivo de take-profit óptimo del rango de +2.0% a +3.5%. Los mercados tradicionales permanecen cerrados. El RSI de 1 hora en los activos cripto se encuentra en zonas neutrales tras el rebote inicial, por lo que la mejor estrategia es mantener las posiciones vigentes y vigilar de cerca para asegurar ganancias o cortar pérdidas oportunamente."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): La posición en BTC-USD muestra un rendimiento positivo de 0.54% tras un tiempo de retención de más de 4 horas. El RSI de 1h se encuentra en 55.3 y el impulso se mantiene estable, por lo que es óptimo mantener a la espera del objetivo de take-profit entre +2.0% y +3.5%.
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD registra una ganancia del 0.95% con un RSI de 1h en 48.5. La posición evoluciona favorablemente dentro del rebote esperado; se mantiene en cartera para buscar el umbral de take-profit establecido.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD acumula un rendimiento positivo del 0.98% con un RSI de 1h en 43.8. La posición mantiene su tesis de recuperación técnica y se mantiene abierta para capturar mayores ganancias antes de realizar una rotación.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en BTC-USD, SOL-USD y ETH-USD. Monitorear el RSI de 1 hora y el avance de los precios para ejecutar take-profit tan pronto como las posiciones alcancen el rango de +2.0% a +3.5%, o activar el stop-loss estricto si alguna posición cae por debajo de -2.0%. Preservar la liquidez actual y evaluar posibles rotaciones de capital en los siguientes ciclos si el impulso se desacelera."
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
