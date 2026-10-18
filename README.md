# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 23:40:40`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.25 USD** | **$38.30 USD** | 🔴 **-4.25%** ($-1.70) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81617.02 | $10.05 | 📈 +0.55% | 4h 39m |
| `SOL-USD` | 0.097418 | $102.65 | $103.64 | $10.10 | 📈 +0.96% | 4h 29m |
| `ETH-USD` | 0.004193 | $2385.05 | $2409.30 | $10.10 | 📈 +1.02% | 4h 29m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado de criptomonedas se mantiene abierto y operando con ligera estabilidad tras el rebote técnico inicial. Las posiciones actuales en BTC-USD, SOL-USD y ETH-USD muestran ganancias moderadas entre +0.55% y +1.02%, acercándose gradualmente a la zona objetivo de take-profit (+2.0% a +3.5%). Los mercados tradicionales están cerrados, por lo que toda la atención y liquidez se concentra en mantener y gestionar los activos cripto activos."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): La posición en BTC-USD muestra un rendimiento positivo de +0.55% y un RSI de 1H en 55.5. Se mantiene abierta buscando alcanzar el rango de take-profit de +2.0% a +3.5%.
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD registra una ganancia de +0.96% con un RSI de 1H en 48.6. El rebote técnico sigue su curso esperado, por lo que se mantiene la posición para asegurar el objetivo de beneficios.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD lidera el portafolio con un avance de +1.02% y un RSI de 1H en 44.2. Se retiene la posición a la espera de completar el tramo alcista hacia la zona de take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas en BTC-USD, SOL-USD y ETH-USD mientras continúen con tendencia alcista de corto plazo. Vigilar de cerca el RSI de 1 hora y el avance de precios; si alguna posición alcanza el rango de ganancia de +2.0% a +3.5% o su RSI cruza 70, ejecutar SELL para asegurar beneficios y liberar capital. Si el momentum se desacelera sin llegar al objetivo, preparar una rotación hacia nuevas oportunidades."
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
