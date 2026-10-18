# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 22:30:45`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.21 USD** | **$38.26 USD** | 🔴 **-4.36%** ($-1.74) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81505.28 | $10.04 | 📈 +0.41% | 3h 29m |
| `SOL-USD` | 0.097418 | $102.65 | $103.54 | $10.09 | 📈 +0.87% | 3h 19m |
| `ETH-USD` | 0.004193 | $2385.05 | $2404.79 | $10.08 | 📈 +0.83% | 3h 19m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene operando 24/7 mientras los mercados tradicionales están cerrados. Las posiciones actuales en BTC-USD, SOL-USD y ETH-USD muestran ligeras ganancias marginales (entre +0.41% y +0.87%), consolidándose tras los rebotes desde zonas de sobreventa. Los indicadores técnicos de 1 hora muestran que la presión compradora es moderada y el impulso debe ser vigilado de cerca para asegurar ganancias si se alcanza el rango objetivo de +2.0% a +3.5%."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): BTC-USD mantiene un rendimiento positivo de +0.41% y un RSI de 1H en 50.8. El precio se consolida constructivamente por encima del precio de entrada, por lo que se mantiene la posición a la espera de alcanzar el objetivo de take-profit del 2.0%.
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD muestra la mayor ganancia actual en cartera con un +0.87% y un RSI de 1H en 37.0. Se mantiene la posición para permitir que el momentum continúe hacia el rango de toma de beneficios.
- **[HOLD] ETH-USD** (Confianza: 80%): ETH-USD registra una ganancia de +0.83% con un RSI de 1H en 32.9. La tendencia de corto plazo se estabiliza tras el rebote, por lo que se decide mantener para buscar mayores beneficios antes de rotar capital.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas en BTC-USD, SOL-USD y ETH-USD mientras evolucionen favorablemente. Vigilar la zona de RSI 1H hacia la sobrecompra (>70) o los objetivos de ganancia de +2.0% a +3.5% para ejecutar tomas de beneficio parciales o totales. Mantener el stop-loss estricto en caso de que el precio revierta y rompa soportes de corto plazo, protegiendo el capital ante cualquier giro bajista repentino."
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
