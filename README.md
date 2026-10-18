# 🤖 Gemini Autonomous Trader

> **Estado:** 🟢 Activo en la Nube | **Última revisión:** `2026-10-18 01:00:46`

---

### 📊 Resumen del Portafolio

| Capital Inicial | Efectivo Libre | Valor en Activos | Balance Total | Rendimiento |
| :---: | :---: | :---: | :---: | :---: |
| **$40.00 USD** | **$8.05 USD** | **$30.41 USD** | **$38.46 USD** | 🔴 **-3.86%** ($-1.54) |

---

### 💼 Posiciones Actuales

| Activo | Acciones | Precio Compra | Precio Actual | Valor Total | PnL % | Tiempo Abierta |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `BTC-USD` | 0.000123 | $81170.65 | $81848.67 | $10.08 | 📈 +0.84% | 6h 0m |
| `SOL-USD` | 0.097418 | $102.65 | $104.39 | $10.17 | 📈 +1.70% | 5h 50m |
| `ETH-USD` | 0.004193 | $2385.05 | $2422.71 | $10.16 | 📈 +1.58% | 5h 50m |

---

### 🧠 Último Análisis de Gemini (Ciclo Reciente)

> "El mercado cripto se mantiene abierto 24/7 con un comportamiento lateral pero positivo tras el rebote inicial. Las posiciones actuales en BTC-USD, SOL-USD y ETH-USD muestran ganancias moderadas (entre +0.84% y +1.70%), aproximándose al umbral objetivo de take-profit, aunque aún sin alcanzar el rango óptimo de +2.0% a +3.5% o niveles de sobrecompra extrema en el RSI de 1H. Los mercados tradicionales están cerrados, por lo que toda la atención táctica se centra en la gestión de las criptomonedas abiertas."

**Operaciones del ciclo:**
- **[HOLD] SOL-USD** (Confianza: 75%): SOL-USD muestra un PnL positivo de +1.70% y un RSI de 1H en 51.5. Está cerca de la zona de take-profit objetivo (+2.0% a +3.5%), por lo que se prefiere mantener la posición abierta a la espera de una mayor expansión del impulso alcista antes de ejecutar la venta.
- **[HOLD] ETH-USD** (Confianza: 75%): ETH-USD registra un PnL de +1.58% con un RSI de 1H en 49.3. La posición evoluciona favorablemente dentro del plan de rebote técnico, por lo que se mantiene hasta alcanzar la zona de toma de beneficios.
- **[HOLD] BTC-USD** (Confianza: 70%): BTC-USD se mantiene estable con un PnL de +0.84% y un RSI de 1H en 59.1. Continuaremos holdeando para permitir que la tendencia de corto plazo alcance el objetivo de ganancias establecido.

---

### 📝 Bitácora & Memoria Operativa (Próximos Ciclos)

> "Mantener las posiciones actuales en BTC-USD, SOL-USD y ETH-USD durante este ciclo mientras se acercan al objetivo de take-profit (+2.0% a +3.5%). Monitorear de cerca los indicadores de 1H; si alguna posición cruza el umbral de ganancia o su RSI de 1H supera los 70 puntos, ejecutar una venta parcial o total para asegurar liquidez en efectivo. Si el impulso se debilita lateralmente, rotar el capital hacia nuevas oportunidades de momentum."
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
