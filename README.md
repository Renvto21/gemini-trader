# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-17 19:30:48`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.02 USD** | **$38.06 USD** | 🔴 **-4.85%** ($-1.94) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81186.71 | $10.00 | 📈 +0.02% | 30m |
| `SOL-USD` | 0.097418 | $102.65 | $102.69 | $10.00 | 📈 +0.04% | 20m |
| `ETH-USD` | 0.004193 | $2385.05 | $2387.25 | $10.01 | 📈 +0.09% | 20m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado tradicional se encuentra cerrado, por lo que toda la atención y liquidez operativa se centra exclusivamente en los activos cripto que operan 24/7. Las posiciones actuales en BTC-USD, SOL-USD y ETH-USD muestran ligeras ganancias iniciales tras haber capturado los rebotes desde zonas de sobreventa en gráficos de 1 hora. El momentum se mantiene constructivo pero bajo vigilancia estricta debido a la tendencia general bajista en el marco diario."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 75%): La posición muestra un rendimiento estable de +0.02% con un holding time de 29 minutos. El RSI de 1h se encuentra recuperándose hacia 38.0, por lo que mantenemos la posición buscando el objetivo de take-profit entre +2.0% y +3.5%.
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD registra una ganancia de +0.04% con un holding time de 20 minutos. El cambio de 1h es positivo (+0.54%) y mantiene la estructura para buscar una extensión del rebote técnico.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD presenta una ganancia actual de +0.09% tras 20 minutos de ejecución. Continuamos dentro de la operación esperando que el momentum alcista de corto plazo impulse el precio hacia nuestra zona de salida.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales (BTC-USD, SOL-USD, ETH-USD) permitiendo que evolucionen hacia el objetivo de take-profit entre +2.0% y +3.5%. Activar el stop-loss de forma inmediata si alguna posición perfora el -2.0%. La liquidez se mantiene en mínimos ($8.05 USD) con exposición total en criptomonedas. En el siguiente ciclo evaluaremos rotar capital si el impulso se desacelera o si alcanzamos las metas de beneficio."
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
