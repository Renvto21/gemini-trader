# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 06:50:39`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.42 USD** | **$38.47 USD** | 🔴 **-3.84%** ($-1.53) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $82118.98 | $10.12 | 📈 +1.17% | 11h 49m |
| `SOL-USD` | 0.097418 | $102.65 | $104.07 | $10.14 | 📈 +1.38% | 11h 39m |
| `ETH-USD` | 0.004193 | $2385.05 | $2424.11 | $10.16 | 📈 +1.64% | 11h 39m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene abierto y operando con un sesgo alcista moderado de corto plazo. Las posiciones actuales en BTC-USD, SOL-USD y ETH-USD muestran ganancias acumuladas entre +1.17% y +1.64%, acercándose de manera constante al objetivo de take-profit ubicado en el rango de +2.0% a +3.5%. Los indicadores RSI de 1 hora se sitúan en niveles saludables (50-64) sin entrar todavía en sobrecompra extrema, lo que sugiere que el impulso de rebote técnico aún tiene espacio para desarrollarse antes de liquidar."

**Operaciones del ciclo:**
- **[HOLD] BTC-USD** (Confianza: 80%): BTC-USD presenta una ganancia actual de +1.17% con un RSI de 1H en 64.6. El rebote técnico sigue activo pero aún no alcanza el objetivo de take-profit de +2.0% a +3.5%, por lo que se mantiene la posición para maximizar el tramo alcista.
- **[HOLD] SOL-USD** (Confianza: 80%): SOL-USD registra un beneficio de +1.38% y un RSI de 1H en 50.8. El precio muestra estabilidad y buen comportamiento dentro del canal de rebote esperado, por lo que conviene mantenerla abierta.
- **[HOLD] ETH-USD** (Confianza: 82%): ETH-USD lidera el rendimiento del portafolio con una ganancia de +1.64% y un RSI de 1H en 53.4. Está muy cerca de la zona óptima de toma de ganancias, por lo que se mantiene operando hasta concretar el take-profit.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones abiertas en BTC-USD, SOL-USD y ETH-USD durante este ciclo mientras continúan su aproximación al rango objetivo de take-profit (+2.0% a +3.5%) o alcanzan un RSI de 1H superior a 70. El stop-loss estricto se mantiene operando en -2.0% para proteger el capital. Si el momentum se desacelera o alguna posición retrocede hacia la zona de entrada, procederé a vender para asegurar beneficios o cortar pérdidas de inmediato."
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
